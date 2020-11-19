import glob

def format_trainer_table(table, table_name):
    output_table = ["" for i in range(len(table))]
    pok = []
    ite = []
    nat = []
    abi = []
    mov = []
    for i in range(len(table)):
        split1 = table[i].split("|")
        print(split1)
        pok.append(split1[0].strip().replace("] ","]<br> "))
        ite.append(split1[1].strip().replace("] ","]<br> "))
        nat.append(split1[2].strip())
        abi.append(split1[3].strip())
        mov.append(split1[4].strip())

    max_len_pok = max(len(x) for x in pok)
    max_len_ite = max(len(x) for x in ite)
    max_len_nat = max(len(x) for x in nat)
    max_len_abi = max(len(x) for x in abi)
    max_len_mov = max(len(x) for x in mov)



    for i in range(len(output_table)):
        output_table[i] = "{:{}} | {:{}} | {:{}} | {:{}} | {:{}}\n".format(pok[i], max_len_pok, ite[i], max_len_ite, nat[i], max_len_nat, abi[i], max_len_abi, mov[i], max_len_mov)




    first_line = "{:{}} | {:{}} | {:{}} | {:{}} | {:{}}\n".format(table_name, max_len_pok, "Item", max_len_ite, "Nature", max_len_nat, "Ability", max_len_abi, "Moves", max_len_mov)
    second_line = "{:{}} | {:{}} | {:{}} | {:{}} | {:{}}\n".format("---", max_len_pok, "---", max_len_ite, "---", max_len_nat, "---", max_len_abi, "---", max_len_mov)

    output_table.insert(0, second_line)
    output_table.insert(0, first_line)

    return output_table

for f in glob.glob("docs/trainer_changes/*.md"):
    train_lines = open(f, "r", encoding="utf-8").readlines()

    trainer_tables = []
    table_names = []
    is_table = False
    current_table = []
    table_starts = []
    i = 0
    for line in train_lines:
        if line.endswith("Moves\n"):
            table_starts.append(i)
            table_names.append(line.split("|")[0].strip())
            is_table = True
        elif is_table:
            if line == "\n":
                is_table = False
                trainer_tables.append(current_table)
                current_table = []
            else:
                if not line.startswith("---"):
                    current_table.append(line.replace("<br>",""))
        i += 1

    for i in range(len(table_names)):
        tab = format_trainer_table(trainer_tables[i], table_names[i])
        for k in range(len(tab)):
            train_lines[k+table_starts[i]] = tab[k]

    open(f, "w", encoding="utf-8").writelines(train_lines)

"🌊🎣🌙☀🌅"