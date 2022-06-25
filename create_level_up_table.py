from genericpath import isfile
import json

def get_moves():
    moves = {}
    for id in range(1, 826):
        if isfile(f"temp/move/{id}.json"):
            with open(f"temp/move/{id}.json", encoding='utf-8') as f:
                jf = json.load(f)
                name = [n["name"] for n in jf["names"] if n["language"]["name"] == "en"][0]
                try:
                    desc = [n["short_effect"] for n in jf["effect_entries"] if n["language"]["name"] == "en"][0]
                    if "$effect_chance" in desc:
                        desc = desc.replace("$effect_chance", str(jf["effect_chance"]))
                except IndexError:
                    desc = "Inflicts regular damage."
                if str(jf["accuracy"]) == "None":
                    accuracy = "-"
                else:
                    accuracy = str(jf["accuracy"]) + "%"
                power = str(jf["power"]).replace("None", "-")
                pp = jf["pp"]
                type_ = jf["type"]["name"]
                dc = jf["damage_class"]["name"]
                moves[name] = (power,accuracy, pp, type_, dc, desc, id)


    # fix move changes

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Aurora Beam")
    power = "75"
    pp = "15"
    moves["[Aurora Beam]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Blaze Kick")
    power = "90"
    accuracy = "100%"
    moves["[Blaze Kick]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Bubble Beam")
    power = "75"
    pp = "15"
    moves["[Bubble Beam]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Chatter")
    power = "90"
    pp = "15"
    moves["[Chatter]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Cross Poison")
    power = "90"
    pp = "15"
    moves["[Cross Poison]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Cut")
    power = "60"
    accuracy = "100%"
    pp = "25"
    type_ = "grass"
    desc = "Has an increased chance for a critical hit."
    moves["[Cut]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Disarming Voice")
    power = "50"
    moves["[Disarming Voice]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Draining Kiss")
    power = "75"
    desc = "Drains 50% of the damage inflicted to heal the user."
    moves["[Draining Kiss]"] = (power,accuracy, pp, type_, dc, desc, id)


    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Flame Wheel")
    power = "75"
    pp = "15"
    moves["[Flame Wheel]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Fly")
    power = "100"
    accuracy = "100%"
    moves["[Fly]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Hurricane")
    desc = "Inflicts regular damage with no additional effect."
    moves["[Hurricane]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Needle Arm")
    power = "90"
    moves["[Needle Arm]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Poison Fang")
    power = "65"
    accuracy = "95%"
    moves["[Poison Fang]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Poison Tail")
    power = "90"
    pp = "15"
    moves["[Poison Tail]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Rock Climb")
    power = "80"
    accuracy = "95%"
    pp = "10"
    type_ = "rock"
    moves["[Rock Climb]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Rock Smash")
    power = "60"
    moves["[Rock Smash]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Scald")
    desc = "Has a 30% chance to burn the target. Does not thaw target."
    moves["[Scald]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Shadow Claw")
    power = "80"
    pp = "15"
    moves["[Shadow Claw]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Shadow Punch")
    power = "80"
    pp = "15"
    moves["[Shadow Punch]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Sludge")
    power = "75"
    pp = "15"
    moves["[Sludge]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Strength")
    power = "100"
    desc = "Has a 10% chance to raise the user's Attack by one stage."
    moves["[Strength]"] = (power,accuracy, pp, type_, dc, desc, id)

    (power,accuracy, pp, type_, dc, desc, id) = moves.pop("Wild Charge")
    power = "100"
    moves["[Wild Charge]"] = (power,accuracy, pp, type_, dc, desc, id)

    return moves



def update_level_up_table(table, moves):
    table[0] = f"Level | Name | Power | Accuracy | PP | Type | Damage Class | Description\n"
    table[1] = f"--- | --- | ---| --- | --- | --- | --- | ---\n"

    for i, l in enumerate(table[2:], 2):
        ls = l.split(" | ")
        level = ls[0].strip()
        name = ls[1].strip()

        key = name.replace("[^1]", "").strip()
        if f"[{key}]" in moves:
            key = f"[{key}]"
            if "[^1]" in name:
                name = f"{key} [^1]"
            else:
                name = key

        (power,accuracy, pp, type_, dc, desc, _) = moves[key]
        table[i] = f"{level} | {name} | {power} | {accuracy} | {pp} | ![][{type_}] {{: data-sort=\"{type_}\"}} | ![][{dc}] {{: data-sort=\"{dc}\"}} | {desc}\n"

    return table

if __name__ == "__main__":
    moves = get_moves()

    table = """Level | Move
---   | ---
1     | Healing Wish
1     | Growth
6     | Magical Leaf
10    | Leech Seed
14    | Quick Attack
18    | Sweet Scent
22    | Natural Gift
26    | Worry Seed
30    | Aromatherapy
34    | Energy Ball
38    | Air Slash
42    | Sweet Kiss
46    | Leaf Storm
50    | Seed Flare"""
    table = [l + "\n" for l in table.split("\n")]

    print("".join(update_level_up_table(table, moves)))