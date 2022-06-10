from dataclasses import dataclass
from os.path import join
import string

from create_ability_table import get_ability_table
from create_stat_table import get_stat_table

base_path = "./docs/pokemon_changes"

@dataclass
class PokemonChange:
    id: int
    name: string
    notes: list
    types: list
    defenses: list
    ability: list
    base_stats: list
    moves : list
    level_up : list

    def title_repr(self):
        return \
f"""# {self.id:03} - {self.name}
![][{self.id:03}]

"""

    def notes_repr(self):
        return \
f"""{"".join(self.notes)}"""

    def type_repr(self):
        return \
f"""## Type

{"".join(self.types)}
"""

    def defenses_repr(self):
        return \
f"""### Defenses

{"".join(self.defenses)}
"""

    def ability_repr(self):
        return \
f"""## Ability

{"".join(self.ability)}
"""

    def base_stats_repr(self):
        return \
f"""## Base Stats

{"".join(self.base_stats)}
"""

    def moves_repr(self):
        return \
f"""## Moves

{"".join(self.moves)}
"""

    def level_up_repr(self):
        return \
f"""## Level Up

{"".join(self.level_up)}
"""

    def __repr__(self):
        return self.title_repr() + self.notes_repr() + self.type_repr() + self.defenses_repr() + self.ability_repr() + self.base_stats_repr() + self.moves_repr() + self.level_up_repr()


def extract_change(id):
    assert id != 386, "Deoxys not supported"
    assert id != 413, "Wormadam not supported"
    assert id != 479, "Rotom not supported"
    assert id != 492, "Shaymin not supported"

    with open(join(base_path, f"{id:03}.md")) as f:
        file_content = f.readlines()
        id = id
        name = file_content[0].split(" - ")[1].strip()
        notes = extract_notes(file_content)
        types = extract_type(file_content)
        defenses = extract_defenses(file_content)
        ability = extract_ability(file_content)
        base_stats = extract_base_stats(file_content)
        moves = extract_moves(file_content)
        level_up = extract_level_up(file_content)
        pc = PokemonChange(id, name, notes, types, defenses, ability, base_stats, moves, level_up)

    return pc

def update_change(pc):
    with open(join(base_path, f"{pc.id:03}.md"), "r") as f:
        file_content = f.readlines()

    i, k = get_section_lines("## Type", file_content)
    if i != k:
        del file_content[i:k]
        file_content.insert(i, pc.type_repr())

    i, k = get_section_lines("## Defenses", file_content)
    if i != k:
        del file_content[i:k]
        file_content.insert(i, pc.defenses_repr())

    i, k = get_section_lines("## Ability", file_content)
    if i != k:
        del file_content[i:k]
        file_content.insert(i, pc.ability_repr())
    else:
        i, k = get_section_lines("## Defenses", file_content)
        file_content.insert(k, pc.ability_repr())

    i, k = get_section_lines("## Base Stats", file_content)
    if i != k:
        del file_content[i:k]
        file_content.insert(i, pc.base_stats_repr())
    else:
        i, k = get_section_lines("## Ability", file_content)
        file_content.insert(k, pc.base_stats_repr())

    i, k = get_section_lines("## Level Up", file_content)
    if i != k:
        del file_content[i:k]
        file_content.insert(i, pc.level_up_repr())
    else:
        i, k = get_section_lines("## Base Stats", file_content)
        file_content.insert(k, pc.level_up_repr())

    with open(join(base_path, f"{pc.id:03}.md"), "w") as f:
        f.writelines(file_content)

def get_section_lines(header, file_content):
    in_section = False
    start = 0
    for i in range(len(file_content)):
        if in_section:
            if file_content[i].startswith("#") or file_content[i].startswith("["):
                return start, i

        if header in file_content[i]:
            start = i
            in_section = True
    return 0, 0

def remove_empty_lines(lines):
    return [l for l in lines if l != "\n"]

def extract_notes(file_content):
    notes = []
    for i in range(len(file_content)):

        if "!!! note" in file_content[i]:
            notes += file_content[i:i+2]

    assert len(notes) <= 2, "No more then one note is supported right now."

    return notes

def extract_type(file_content):
    start, end = get_section_lines("## Type", file_content)
    return remove_empty_lines(file_content[start + 1:end])

def extract_defenses(file_content):
    start, end = get_section_lines("### Defenses", file_content)
    return remove_empty_lines(file_content[start + 1:end])

def extract_ability(file_content):
    start, end = get_section_lines("## Ability", file_content)
    return remove_empty_lines(file_content[start + 1:end])

def extract_base_stats(file_content):
    start, end = get_section_lines("## Base Stats", file_content)
    return remove_empty_lines(file_content[start + 1:end])


def extract_moves(file_content):
    start, end = get_section_lines("## Moves", file_content)
    return remove_empty_lines(file_content[start + 1:end])


def extract_level_up(file_content):
    start, end = get_section_lines("## Level Up", file_content)
    return remove_empty_lines(file_content[start + 1:end])

for i in range(1, 494):
    try:
        pc = extract_change(i)

        pc.level_up.append("""

--8<-- "includes/abilities.md"
""")
        update_change(pc)
    except Exception:
        print("Exception")
