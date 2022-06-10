from genericpath import isfile
import json
import re

def get_ability_name(id):
    if isfile(f"temp/ability/{id}.json"):
        with open(f"temp/ability/{id}.json", encoding='utf-8') as f:
            jf = json.load(f)
            for langs in jf["names"]:
                if langs["language"]["name"] == "en":
                    return langs["name"]

def get_ability_short_effect(id):
    if isfile(f"temp/ability/{id}.json"):
        with open(f"temp/ability/{id}.json", encoding='utf-8') as f:
            jf = json.load(f)
            for langs in jf["effect_entries"]:
                if langs["language"]["name"] == "en":
                    return langs["short_effect"]



def get_ability_table(id):
    if isfile(f"temp/pokemon/{id}.json"):
        with open(f"temp/pokemon/{id}.json") as f:
            jf = json.load(f)
            abilities = jf["abilities"]
            if len(abilities) >= 2:
                id1 = re.search("https://pokeapi.co/api/v2/ability/(.*)/", abilities[0]["ability"]["url"]).group(1)
                id2 = re.search("https://pokeapi.co/api/v2/ability/(.*)/", abilities[1]["ability"]["url"]).group(1)

                ability1 = get_ability_name(id1)
                ability2 = get_ability_name(id2)
            else:
                id1 = re.search("https://pokeapi.co/api/v2/ability/(.*)/", abilities[0]["ability"]["url"]).group(1)
                ability1 = get_ability_name(id1)
                ability2 = "None"


            return f"""Version | Ability
---     | ---
All     | {ability1} / {ability2}
"""

if __name__ == "__main__":
    for id in range(1, 233):
        print(f"*[{get_ability_name(id)}]: {get_ability_short_effect(id)}")