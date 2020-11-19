import argparse
import glob
import re

def fix_links(file_name, links):
    input_file = open(file_name, "r")
    data = input_file.read()
    input_file.close()
    # remove all links
    for link in links:
        link_id = link.split("]:")[0].replace("[","")
        data = re.sub(r"\[{}\]\:.*\n".format(link_id), "", data)
    data=data.strip()+"\n\n"
    # add neccasery links
    for link in links:
        link_id = link.split(":")[0]
        if data.count(link_id):
            data += link

    output_file = open(file_name, "w")
    output_file.write(data)



parser = argparse.ArgumentParser(prog="Fix links")
parser.add_argument('-l', default="links.md", help='The location of the link.md file')
parser.add_argument('paths', nargs='+', help='the paths to all files where the link should be fixed')

args = parser.parse_args()

links = open(args.l).readlines()
for link in links:
    link_id = link.split(":")[0]
    count = 0
    for other in links:
        if other.startswith(link_id):
            count += 1
    if count > 1:
        print("ERROR: the link with id {} is duplicated.".format(link_id))
        exit()

print("Found {} file with {:d} links".format(args.l, len(links)))

for path in args.paths:
    files =  glob.glob(path)
    for f in files:
        print("Fixed links for: {}".format(f))
        fix_links(f, links)

