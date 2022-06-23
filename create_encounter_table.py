import glob
import tqdm

path = "docs/wild_pokemon/*.md"


def create_encounter_table(id, pokemon_locations):
    if id in pokemon_locations:
        table = ["Route | Method | Level | Chance\n"]
        table += ["--- | --- | --- | ---\n"]
        for (route, method, chance, level) in pokemon_locations[id]:
            table += [f"[{route}] | {method} | {level} | {chance} \n"]

        return table
    else:
        return []

def extract_all_wild_pokemons():
    paths = glob.glob(path)

    pokemon_locations = {}


    for p in tqdm.tqdm(paths):
        pl = _extract_from_file(p)
        for p in pl:
            id_, route, method, chance, level = p
            if id_ not in pokemon_locations:
                pokemon_locations[id_] = []
            pokemon_locations[id_] += [(route, method, chance, level)]

    return pokemon_locations

def _extract_from_file(p):
    pl = []
    with open(p, "r", encoding="utf-8") as f:
        route = f.readline().replace("#", "").strip()
        i = 0
        while not f.readline().startswith("Area"):
            i += 1
            if i == 100:
                return []
        f.readline() # read --- line

        l = f.readline().strip()
        while l != "":

            line = l.split("|")
            line = [a.strip() for a in line]

            t = line[0].split("<br>")
            if t[0] !=  "&nbsp;":
                method = " ".join(t[:2])
                level = t[2].strip()

            for poke in line[1:]:
                if poke == "&nbsp;":
                    continue
                po = poke.split("<br>")
                id_ = po[0][4:7]
                chance = po[2]


                pl += [(id_, route, method, chance, level)]


            l = f.readline().strip()

    return pl

if __name__ == "__main__":
    pokemon_locations = extract_all_wild_pokemons()
    for id_ in pokemon_locations.keys():
        print("".join(create_encounter_table(id_, pokemon_locations)))
        print("")
