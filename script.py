input_file = open("docs/trainer_pokemon.md", "r",encoding="utf-8")

lines = input_file.read()

pokemons = lines.split("\n### ")

for pok in pokemons:
    route = pok.split("\n")[0]
    file_name = route.lower().replace(" ","_").replace("~","").replace(".","").replace("é","e")

    print("- {}: /trainer_changes/{}.md".format(route,file_name))
    output_file = open("docs/trainer_changes/{}.md".format(file_name), "w",encoding="utf-8")
    output_file.write("# {}".format(pok))
    output_file.close()

