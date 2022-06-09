from genericpath import isfile
import json


for id in range(51, 52):
    if isfile(f"temp/{id}.json"):
        with open(f"temp/{id}.json") as f:
            jf = json.load(f)
            hp = jf["stats"][0]["base_stat"]
            atk = jf["stats"][1]["base_stat"]
            de = jf["stats"][2]["base_stat"]
            satk = jf["stats"][3]["base_stat"]
            sde = jf["stats"][4]["base_stat"]
            spe = jf["stats"][5]["base_stat"]
            bst = hp + atk + de + satk + sde + spe
            print( "         | HP  | Atk | Def | SAtk | SDef | Spd | BST")
            print( "---      | --- | --- | --- | ---  | ---  | --- | ---")
            print(f"Ultra SM | {hp:3} | {atk:3} | {de:3} | {satk:4} | {sde:4} | {spe:3} | {bst:3}")