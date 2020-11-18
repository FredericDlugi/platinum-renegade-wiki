input_file = open("docs/pokemon_changes.md", "r")

lines = input_file.read()

pokemons = lines.split("### ")

for pok in pokemons:
    dex_id = pok.split(" -")[0]
    if dex_id.isdigit():
        output_file = open("docs/pokemons_changes/{}.md".format(dex_id), "w+")
        output_file.write("# {}".format(pok))
        output_file.close()

