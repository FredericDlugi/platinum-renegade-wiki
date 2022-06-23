
from genericpath import isfile
from os import makedirs
import requests
import tqdm

makedirs("temp/pokemon/",exist_ok=True)
makedirs("temp/ability/",exist_ok=True)
makedirs("temp/move/",exist_ok=True)
makedirs("temp/item/",exist_ok=True)

for id in tqdm.tqdm(range(1, 494)):

    if isfile(f"temp/pokemon/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")

    if response == "Not Found":
        continue

    fh = open(f"temp/{id}.json", "wb")
    fh.write(response.content)
    fh.close()

for id in tqdm.tqdm(range(1, 234)):

    if isfile(f"temp/ability/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/ability/{id}")

    if response == "Not Found":
        continue

    fh = open(f"temp/ability/{id}.json", "wb")
    fh.write(response.content)
    fh.close()

for id in tqdm.tqdm(range(1, 826)):

    if isfile(f"temp/move/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/move/{id}")

    if response == "Not Found":
        continue

    fh = open(f"temp/move/{id}.json", "wb")
    fh.write(response.content)
    fh.close()

for id in tqdm.tqdm(range(1,1607)):

    if isfile(f"temp/item/{id}.json"):
        continue

    response = requests.get(f"https://pokeapi.co/api/v2/item/{id}")

    if response == "Not Found":
        continue

    fh = open(f"temp/item/{id}.json", "wb")
    fh.write(response.content)
    fh.close()