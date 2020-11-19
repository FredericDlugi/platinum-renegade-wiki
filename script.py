import glob

wild_path = glob.glob("docs/wild_pokemon/*.md")
train_path = glob.glob("docs/trainer_changes/*.md")

routes_wild = [path.replace("docs/wild_pokemon\\", "").replace(".md","") for path in wild_path]
routes_trai = [path.replace("docs/trainer_changes\\", "").replace(".md","") for path in train_path]

routes_both = set(routes_wild).intersection(routes_trai)

print(routes_both)
for route in routes_both:
    link_wild = ""
    file_wild = open("docs/wild_pokemon/{}.md".format(route), "r", encoding="utf-8")
    file_trai = open("docs/trainer_changes/{}.md".format(route), "r", encoding="utf-8")

    lines_wild = file_wild.readlines()
    lines_trai = file_trai.readlines()

    file_wild.close()
    file_trai.close()

    new_line_trai = "    There are wild Pokémon on this route. You can find out more [here](trainer_changes/{}/).\n".format(route)
    lines_trai.insert(1, "\n")
    lines_trai.insert(1, new_line_trai)
    lines_trai.insert(1, "note !!!\n")
    lines_trai.insert(1, "\n")

    new_line_wild = "    There are trainer on this route. You can find out more [here](wild_pokemon/{}/).\n".format(route)
    lines_wild.insert(1, "\n")
    lines_wild.insert(1, new_line_wild)
    lines_wild.insert(1, "note !!!\n")
    lines_wild.insert(1, "\n")


    file_wild = open("docs/wild_pokemon/{}.md".format(route), "w", encoding="utf-8")
    file_trai = open("docs/trainer_changes/{}.md".format(route), "w", encoding="utf-8")

    file_wild.writelines(lines_wild)
    file_trai.writelines(lines_trai)
"🌊🎣🌙☀🌅"