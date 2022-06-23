# Platinum Renegade Wiki

This Readme should help you to edit and deploy your own version of this Wiki

## Setup

1.  Clone this repo
2.  Install python
3.  Install requirements with `pip install -r requirements.txt`

## Local Development

In the main directory of this repo run:
```
python -m mkdocs serve
```
## Fix table layout

This script fixes the table formatting and removes unused columns.
Example to run it on everything.
```sh
python fix_table_formatting.py ./docs/*.md ./docs/*/*.md
```

## Fix links

This script fixes all the link locations in a range of files.
Example to fix the links for all pokemon changes.
If you have new links that need to be added add them to `links.txt`
```sh
python fix_links.py /pokemon_changes/*.md
```

## PokeAPI related scripts

The `download_pokemon.py` script loads a lot of data from the PokeAPI and
caches it in `temp`.

### Create Level-Up tables

The `create_level_up_table.py` script was used to add move infos to all level up moves. The move-info is mostly grabbed from PokeAPI but contains the changes done by Drayano.

### Create Stat tables

The `create_stat_table.py` script was used to add stats to all pokemon regardless of change. The stats is mostly grabbed from PokeAPI but contains the changes done by Drayano.

### Create Encounter tables

The `create_encounter_table.py` script was used to add encounter locations to all Pokemons. Thanks to @Paco-m-c for the suggestion.

### Create Ability tables

The `create_ability_table.py` script was used to add the ability to all pokemon regardless of change. The stats is mostly grabbed from PokeAPI but contains the changes done by Drayano.