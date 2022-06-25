
from genericpath import isfile
import json
import re
from typing import Dict

from create_level_up_table import get_moves


def get_learned_by(move_id):
    learned_by = []
    if isfile(f"temp/move/{move_id}.json"):
        with open(f"temp/move/{move_id}.json", encoding='utf-8') as f:
            jf = json.load(f)
            for lp in jf["learned_by_pokemon"]:
                poke_id = int(
                    re.findall(
                        r"https://pokeapi.co/api/v2/pokemon/(\d+)/",
                        lp["url"])[0])
                if poke_id < 494:
                    learned_by.append(f"{poke_id:03}")

    return learned_by


def create_learnable_table(poke_id, tm_dict, tutor_dict, learnable_dict : Dict[str, list], moves=None):
    table = []
    table += [f"Machine | Name | Power | Accuracy | PP | Type | Damage Class | Description\n"]
    table += [f"--- | --- | ---| --- | --- | --- | --- | ---\n"]

    learnables = learnable_dict[poke_id]
    if moves is not None:
        learnables = extract_new_learnable_moves(moves, learnables)
    learnables = list(dict.fromkeys(learnables))
    learnables.sort()

    for key in learnables:

        if re.match(r"Y.+", key): # is Move Tutor
            (name, power, accuracy, pp, type_, dc, desc, _) = tutor_dict[key.replace("[^1]", "")]
            if "[^1]" in key:
                name += " [^1]"
            key = "Move Tutor"
        elif re.match(r"X.+", key): # is HM
            (name, power, accuracy, pp, type_, dc, desc, _) = tm_dict[key.replace("[^1]", "")]
            key = key[1:]
        else:
            (name, power, accuracy, pp, type_, dc, desc, _) = tm_dict[key.replace("[^1]", "")]

        if "[^1]" in key:
            name += " [^1]"
            key = key.replace("[^1]", "")

        table += [f"{key} | {name} | {power} | {accuracy} | {pp} | ![][{type_}] {{: data-sort=\"{type_}\"}} | ![][{dc}] {{: data-sort=\"{dc}\"}} | {desc}\n"]

    return table

def extract_new_learnable_moves(moves,learnables: list) -> list:
    for m in moves:
        if re.match(r".*- Now compatible with ",m):

            if  "[^1]" in m:
                suff = "[^1]"
            else:
                suff = ""
            tm = re.findall(r"- Now compatible with (TM\d\d).+\n", m)
            if len(tm) == 1:
                tm = tm[0]
                if tm in learnables:
                    learnables.remove(tm)
                learnables += [tm + suff]

            hm = re.findall(r"- Now compatible with (HM\d\d).+\n", m)
            if len(hm) == 1:
                hm = f"X{hm[0]}"
                if hm in learnables:
                    learnables.remove(hm)
                learnables += [hm + suff]

            mt = re.findall(r"- Now compatible with (.+) from", m)
            if len(tm) == 1:
                mt = f"Y{mt[0]}"
                if mt in learnables:
                    learnables.remove(mt)
                learnables += [mt + suff]
        elif m == "\n":
            pass
        else:
            print(m)

    return learnables

def get_tm_dict(move_dict):
    tm_dict = {
        "TM01": "Focus Punch",
        "TM02": "Dragon Claw",
        "TM03": "Water Pulse",
        "TM04": "Calm Mind",
        "TM05": "Roar",
        "TM06": "Toxic",
        "TM07": "Hail",
        "TM08": "Bulk Up",
        "TM09": "Bullet Seed",
        "TM10": "Hidden Power",
        "TM11": "Sunny Day",
        "TM12": "Taunt",
        "TM13": "Ice Beam",
        "TM14": "Blizzard",
        "TM15": "Hyper Beam",
        "TM16": "Light Screen",
        "TM17": "Protect",
        "TM18": "Rain Dance",
        "TM19": "Giga Drain",
        "TM20": "Safeguard",
        "TM21": "Frustration",
        "TM22": "Solar Beam",
        "TM23": "Iron Tail",
        "TM24": "Thunderbolt",
        "TM25": "Thunder",
        "TM26": "Earthquake",
        "TM27": "Return",
        "TM28": "Dig",
        "TM29": "Psychic",
        "TM30": "Shadow Ball",
        "TM31": "Brick Break",
        "TM32": "Double Team",
        "TM33": "Reflect",
        "TM34": "Shock Wave",
        "TM35": "Flamethrower",
        "TM36": "Sludge Bomb",
        "TM37": "Sandstorm",
        "TM38": "Fire Blast",
        "TM39": "Rock Tomb",
        "TM40": "Aerial Ace",
        "TM41": "Torment",
        "TM42": "Facade",
        "TM43": "Secret Power",
        "TM44": "Rest",
        "TM45": "Attract",
        "TM46": "Thief",
        "TM47": "Steel Wing",
        "TM48": "Skill Swap",
        "TM49": "Snatch",
        "TM50": "Overheat",
        "TM51": "Roost",
        "TM52": "Focus Blast",
        "TM53": "Energy Ball",
        "TM54": "False Swipe",
        "TM55": "[Scald]",
        "TM56": "Fling",
        "TM57": "[Wild Charge]",
        "TM58": "Endure",
        "TM59": "Dragon Pulse",
        "TM60": "Drain Punch",
        "TM61": "Will-O-Wisp",
        "TM62": "Bug Buzz",
        "TM63": "Embargo",
        "TM64": "Explosion",
        "TM65": "[Shadow Claw]",
        "TM66": "Payback",
        "TM67": "Recycle",
        "TM68": "Giga Impact",
        "TM69": "Rock Polish",
        "TM70": "Flash",
        "TM71": "Stone Edge",
        "TM72": "Avalanche",
        "TM73": "Thunder Wave",
        "TM74": "Gyro Ball",
        "TM75": "Swords Dance",
        "TM76": "Stealth Rock",
        "TM77": "Psych Up",
        "TM78": "Captivate",
        "TM79": "Dark Pulse",
        "TM80": "Rock Slide",
        "TM81": "X-Scissor",
        "TM82": "Sleep Talk",
        "TM83": "Hyper Voice",
        "TM84": "Poison Jab",
        "TM85": "Dazzling Gleam",
        "TM86": "Grass Knot",
        "TM87": "Swagger",
        "TM88": "[Hurricane]",
        "TM89": "U-turn",
        "TM90": "Substitute",
        "TM91": "Flash Cannon",
        "TM92": "Trick Room",
        "XHM01": "[Cut]",
        "XHM02": "[Fly]",
        "XHM03": "Surf",
        "XHM04": "[Strength]",
        "XHM05": "Defog",
        "XHM06": "[Rock Smash]",
        "XHM07": "Waterfall",
        "XHM08": "[Rock Climb]",
    }
    for key in tm_dict.keys():
        name = tm_dict[key]
        (power, accuracy, pp, type_, dc, desc, id) = move_dict[name]
        tm_dict[key] = (name, power, accuracy, pp, type_, dc, desc, id)

    return tm_dict

def get_tutor_dict(move_dict):
    r212 = [
        "Air Cutter",
        "Dive",
        "Fire Punch",
        "Fury Cutter",
        "Ice Punch",
        "Icy Wind",
        "Knock Off",
        "Ominous Wind",
        "Sucker Punch",
        "Thunder Punch",
        "Trick",
        "Vacuum Wave",
        "Zen Headbutt",
    ]

    spc = [
        "Helping Hand",
        "Last Resort",
        "Magnet Rise",
        "Snore",
        "Spite",
        "Swift",
        "Synthesis",
        "Uproar",
    ]

    sa = [
        "Ancient Power",
        "Aqua Tail",
        "Bounce",
        "Earth Power",
        "Endeavor",
        "Gastro Acid",
        "Gunk Shot",
        "Heat Wave",
        "Iron Defense",
        "Iron Head",
        "Mud-Slap",
        "Outrage",
        "Rollout",
        "Seed Bomb",
        "Signal Beam",
        "Superpower",
    ]
    free = [
        "Blast Burn",
        "Draco Meteor",
        "Frenzy Plant",
        "Hydro Cannon",
    ]
    tutor_dict = {}
    for name in (r212 + spc + sa + free):
        (power, accuracy, pp, type_, dc, desc, id) = move_dict[name]
        tutor_dict[f"Y{name}"] = (name, power, accuracy, pp, type_, dc, desc, id)

    return tutor_dict


def get_learnable_dict(tm_dict, tutor_dict):
    temp_dict = {}
    for key in tm_dict.keys():
        (_, _, _, _, _, _, _, id) = tm_dict[key]
        temp_dict[key] = get_learned_by(id)
    for key in tutor_dict.keys():
        (_, _, _, _, _, _, _, id) = tutor_dict[key]
        temp_dict[key] = get_learned_by(id)

    learnable_dict = {}
    for key in temp_dict.keys():
        learned_by = temp_dict[key]
        for poke_id in learned_by:
            if poke_id not in learnable_dict:
                learnable_dict[poke_id] = []
            learnable_dict[poke_id].append(key)

    return learnable_dict

if __name__ == "__main__":
    move_dict = get_moves()

    tm_dict = get_tm_dict(move_dict)
    tutor_dict = get_tutor_dict(move_dict)
    learnable_dict = get_learnable_dict(tm_dict, tutor_dict)


    print("".join(create_learnable_table("493", tm_dict, tutor_dict, learnable_dict)))
