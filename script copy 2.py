import glob
import requests
import json
import numpy as np
np.set_printoptions(precision=3)

def add_type():
    pass

def get_type(pokemon_id):
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(int(pokemon_id))
    pokeapi = json.loads(requests.get(url, allow_redirects=True).content)

    if len(pokeapi["types"]) == 1:
        type_ = [pokeapi["types"][0]["type"]["name"]]
        return type_, get_effectiveness(type_[0])
    else:
        type_ = [pokeapi["types"][0]["type"]["name"], pokeapi["types"][1]["type"]["name"]]
        return type_, get_effectiveness(type_[0], type_[1])


def get_effectiveness(type_a, type_b = None):
    type_to_id = {
        "normal" : 1,
        "fighting" : 2,
        "flying" : 3,
        "poison" : 4,
        "ground": 5,
        "rock": 6,
        "bug": 7,
        "ghost": 8,
        "steel": 9,
        "fire": 10,
        "water": 11,
        "grass": 12,
        "electric": 13,
        "psychic": 14,
        "ice": 15,
        "dragon": 16,
        "dark": 17,
        "fairy": 18
    }

    id_to_type = [
        "normal",
        "fighting",
        "flying",
        "poison",
        "ground",
        "rock",
        "bug",
        "ghost",
        "steel",
        "fire",
        "water",
        "grass",
        "electric",
        "psychic",
        "ice",
        "dragon",
        "dark",
        "fairy"
        ]

    e_m =np.array([#normal fighting flying poison ground rock  bug ghost steel fire water grass electric psychic  ice dragon dark fairy
                    [    1,     2.0,     1,     1,     1,   1,   1,  0.0,    1,   1,    1,    1,       1,      1,   1,     1,   1,    1], #normal
                    [    1,       1,   2.0,     1,     1, 0.5, 0.5,    1,    1,   1,    1,    1,       1,      1,   1,     1, 0.5,  2.0], #fighting
                    [    1,     0.5,     1,     1,   0.0, 2.0, 0.5,    1,    1,   1,    1,  0.5,     2.0,      1, 2.0,     1,   1,    1], #flying
                    [    1,     0.5,     1,   0.5,   2.0,   1, 0.5,    1,    1,   1,    1,  0.5,       1,    2.0,   1,     1,   1,  0.5], #poison
                    [    1,       1,     1,   0.5,     1, 0.5,   1,    1,    1,   1,  2.0,  2.0,       0,      1, 2.0,     1,   1,    1], #ground
                    [  0.5,     2.0,   0.5,   0.5,   2.0,   1,   1,    1,  2.0, 0.5,  2.0,  2.0,       1,      1,   1,     1,   1,    1], #rock
                    [    1,     0.5,   2.0,     1,   0.5, 2.0,   1,    1,    1, 2.0,    1,  0.5,       1,      1,   1,     1,   1,    1], #bug
                    [    0,       0,     1,   0.5,     1,   1, 0.5,  2.0,    1,   1,    1,    1,       1,      1,   1,     1, 2.0,    1], #ghost
                    [  0.5,     2.0,   0.5,     0,   2.0, 0.5, 0.5,    1,  0.5, 2.0,    1,  0.5,       1,    0.5, 0.5,   0.5,   1,  0.5], #steel
                    [    1,       1,     1,     1,   2.0, 2.0, 0.5,    1,  0.5, 0.5,  2.0,  0.5,       1,      1, 0.5,     1,   1,  0.5], #fire
                    [    1,       1,     1,     1,     1,   1,   1,    1,  0.5, 0.5,  0.5,  2.0,     2.0,      1, 0.5,     1,   1,    1], #water
                    [    1,       1,   2.0,   2.0,   0.5,   1, 2.0,    1,    1, 2.0,  0.5,  0.5,     0.5,      1, 2.0,     1,   1,    1], #grass
                    [    1,       1,   0.5,     1,   2.0,   1,   1,    1,  0.5,   1,    1,    1,     0.5,      1,   1,     1,   1,    1], #electric
                    [    1,     0.5,     1,     1,     1,   1, 2.0,  2.0,    1,   1,    1,    1,       1,    0.5,   1,     1, 2.0,    1], #psychic
                    [    1,     2.0,     1,     1,     1, 2.0,   1,    1,  2.0, 2.0,    1,    1,       1,      1, 0.5,     1,   1,    1], #ice
                    [    1,       1,     1,     1,     1,   1,   1,    1,    1, 0.5,  0.5,  0.5,     0.5,      1, 2.0,   2.0,   1,  2.0], #dragon
                    [    1,     2.0,     1,     1,     1,   1, 2.0,  0.5,    1,   1,    1,    1,       1,      0,   1,     1, 0.5,  2.0], #dark
                    [    1,     0.5,     1,   2.0,     1,   1, 0.5,    1,  2.0,   1,    1,    1,       1,      1,   1,     0, 0.5,    1] #fairy
                ])

    a_id = type_to_id[type_a]
    a_e = e_m[a_id-1, :]
    if not (type_b is None):
        b_id = type_to_id[type_b]
        b_e = e_m[b_id-1, :]
    else:
        b_e = np.ones(len(e_m[0, :]))

    e = a_e * b_e

    eff = {0:[],0.25:[],0.5:[],1:[],2:[],4:[]}
    for i in range(len(e)):
        eff[e[i]].append(id_to_type[i])

    return eff

def get_type_lines(t, eff):

    type_lines = []
    type_lines.append("## Type\n")
    type_lines.append("\n")
    if len(t) == 1:
        type_lines.append("![][{}]\n".format(t[0]))
    else:
        type_lines.append("![][{}]  ![][{}]\n".format(t[0],t[1]))

    type_lines.append("\n")
    type_lines.append("### Defenses\n")
    type_lines.append("\n")

    type_lines.append("Immune ×0 | Resistant ×¼ | Resistant ×½ | Normal ×1 | Weak ×2 | Weak ×4\n")
    type_lines.append("---       | ---          | ---          | ---       | ---     | ---\n")
    eff_line = ""
    for i in [0,0.25,0.5,1.0,2.0,4.0]:
        for t in eff[i]:
            eff_line += "![][{}]<br> ".format(t)
        eff_line += "| "

    type_lines.append(eff_line+"\n")

    type_lines.append("\n")

    return type_lines

for f in glob.glob("docs/pokemon_changes/*.md"):
    file_lines = open(f, "r", encoding="utf-8").readlines()

    poke_id = file_lines[0].replace("# ", "").split("-")[0].strip()

    t, eff = get_type(poke_id)

    type_lines = get_type_lines(t, eff)
    print("".join(type_lines))


    #open(f, "w", encoding="utf-8").writelines(file_lines)
