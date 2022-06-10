from genericpath import isfile
import json

def get_stat_table(id):
    if isfile(f"temp/pokemon/{id}.json"):
        with open(f"temp/pokemon/{id}.json") as f:
            jf = json.load(f)
            hp = jf["stats"][0]["base_stat"]
            atk = jf["stats"][1]["base_stat"]
            de = jf["stats"][2]["base_stat"]
            satk = jf["stats"][3]["base_stat"]
            sde = jf["stats"][4]["base_stat"]
            spe = jf["stats"][5]["base_stat"]
            bst = hp + atk + de + satk + sde + spe
            return f"""Version | HP  | Atk | Def | SAtk | SDef | Spd | BST
---     | --- | --- | --- | ---  | ---  | --- | ---
All     | {hp:3} | {atk:3} | {de:3} | {satk:4} | {sde:4} | {spe:3} | {bst:3}
"""

if __name__ == "__main__":
    for id in range(51, 52):
        print(get_stat_table(id))
