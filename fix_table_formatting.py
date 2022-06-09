import glob
import requests
import json
import numpy as np
import argparse
import re

np.set_printoptions(precision=3)

class Table:
    def __init__(self):
        self.start_line = 0
        self.n_col = 0
        self.lines = []

    def format(self):
        # calc max length of each column
        empty_cell = "&nbsp;"

        max_len = np.zeros(self.n_col,dtype=int)
        for i in range(len(self.lines)):
            cols = [re.sub(r"\s*<br>\s*","<br>",l.strip()) for l in self.lines[i].strip().split("|")]
            cols = [empty_cell if s == "" else s for s in cols]


            for i in range(len(cols)):
                max_len[i] = max(max_len[i], len(cols[i]))

        # create formatting string
        format_string = ""
        i = 0
        for ml in max_len:
            if ml == 0:
                # there is nothing in this colum so we leave it
                max_len = max_len[:i]
                break
            format_string += "{"+"c[{}]:{}".format(i, ml)+"} | "
            i += 1


        for i in range(len(self.lines)):
            cols = [re.sub(r"\s*<br>\s*","<br>",l.strip()) for l in self.lines[i].strip().split("|")]
            cols = [empty_cell if s == "" else s for s in cols]

            for k in range(len(max_len)-len(cols)):
                cols.append(empty_cell)
            self.lines[i] = format_string.format(c=cols)

        # reduce empty cols
        #

        while self.__check_last_col_empty():
            for i in range(len(self.lines)):
                self.lines[i] = "|".join(self.lines[i].split("|")[:-1])

        self.lines = [s.rstrip()+"\n" for s in self.lines]

    def __check_last_col_empty(self):
        empty_cell = "&nbsp;"
        for line in self.lines:
            cells = line.split("|")
            last_col = cells[-1].strip()
            if last_col == "" and last_col == empty_cell:
                return True

        return False

    def print(self):
        for line in self.lines:
            print(line[:-2])

def extract_tables(lines):
    tables = []
    curr_table = None
    i = 0
    for line in lines:
        n_col = len(line.split("|"))
        if n_col >= 2:
            if curr_table is None:
                curr_table = Table()
                curr_table.start_line = i

            curr_table.lines.append(line)
            curr_table.n_col = max(curr_table.n_col, n_col)

        elif not curr_table is None:
            tables.append(curr_table)
            curr_table = None

        i+=1

    return tables


def replace_table(lines, table):
    for i in range(len(table.lines)):
        lines[i+table.start_line] = table.lines[i]

if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog="Fix table formatting")
    parser.add_argument('paths', nargs='+', help='the paths to all files where the tables should be fixed')

    args = parser.parse_args()

    for path in args.paths:
        files =  glob.glob(path)
        for f in files:
            file_lines = open(f, "r", encoding="utf-8").readlines()

            tables = extract_tables(file_lines)


            for t in tables:
                t.format()
                replace_table(file_lines, t)

            open(f,"w", encoding="utf-8").writelines(file_lines)

            print("Fixed {:2} tables in file: {}".format(len(tables), f))