
from genericpath import isfile
from os import makedirs
import requests
import tqdm

for id in tqdm.tqdm(range(1, 494)):

    if isfile(f"temp/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")

    makedirs("temp",exist_ok=True)

    fh = open(f"temp/{id}.json", "wb")
    fh.write(response.content)
    fh.close()
