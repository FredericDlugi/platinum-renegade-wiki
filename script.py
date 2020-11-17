input_file = open("docs/pokemon_changes.md", "r")
output_file = open("docs/pokemon_changes1.md", "w")

lines = input_file.readlines()

for i in range(len(lines)):
    for k in range(1, 101):
        if lines[i].startswith("{} - ".format(k)):
            lines[i] = lines[i].replace("{} - ".format(k), "{:3}   | ".format(k))

output_file.writelines(lines)
