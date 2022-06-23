
from glob import glob
import json
from json import JSONDecodeError

from tqdm import tqdm


output = open("includes/held_items.md","w", encoding="utf-8")
for path in tqdm(glob("temp/item/*.json")):
    with open(path, "r", encoding="utf-8") as f:
        try:
            fjson = json.load(f)
            for attr in fjson["attributes"]:
                if attr["name"] == "holdable-active":
                    for n in fjson["names"]:
                        if n["language"]["name"] == "en":
                            name = n["name"]
                    for n in fjson["effect_entries"]:
                        if n["language"]["name"] == "en":
                            short_effect = n["short_effect"]
                    output.write(f"*[{name}]: {short_effect}\n")
        except JSONDecodeError:
            print(f"{path} could not be decoded.")
