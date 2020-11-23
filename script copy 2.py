import glob
import requests
import json

def add_type():
    pass

def get_type(pokemon_id):
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(int(pokemon_id))
    pokeapi = json.loads(requests.get(url, allow_redirects=True).content)

    if len(pokeapi["types"]) == 1:
        print("![][{}]".format(pokeapi["types"][0]["type"]["name"]))
    else:
        print("![][{}] ![][{}]".format(pokeapi["types"][0]["type"]["name"], pokeapi["types"][1]["type"]["name"]))



for f in glob.glob("docs/pokemon_changes/*.md"):
    file_lines = open(f, "r", encoding="utf-8").readlines()

    poke_id = file_lines[0].replace("# ", "").split("-")[0].strip()
    get_type(poke_id)


    #open(f, "w", encoding="utf-8").writelines(file_lines)
