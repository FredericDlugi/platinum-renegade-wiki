import glob

def format_trainer_table(table):
    output_table = ["" for i in range(len(table))]
    trainer_names = []
    pokemons = []
    for line in table:
        split1 = line.split("|")
        trainer_name=split1[0].strip()
        trainer_names.append(trainer_name)
        pokemons.append(["![]" + s.strip().replace("  "," ").replace("\n","").replace("] ","]<br> ") for s in split1[1].split("![]")[1:]])

    max_num_pok = 1
    max_trainer_name_len = len("Trainer")
    max_pok_len = len("---")

    for i in range(len(trainer_names)):
        print(pokemons[i])
        len_trainer_name = len(trainer_names[i])
        if len_trainer_name > max_trainer_name_len:
            max_trainer_name_len = len_trainer_name


        num_pok = len(pokemons[i])
        if num_pok > max_num_pok:
            max_num_pok = num_pok

        for p in pokemons[i]:
            len_pok = len(p)
            if len_pok > max_pok_len:
                max_pok_len = len_pok


    print(max_num_pok, max_pok_len, max_trainer_name_len)


    for i in range(len(trainer_names)):
        output_table[i] += "{:{}} ".format(trainer_names[i], max_trainer_name_len)
        for k in range(len(pokemons[i])):
            output_table[i] += "| {:{}} ".format(pokemons[i][k], max_pok_len)
        print(output_table[i])
        output_table[i] += "\n"

    first_line = "{:{}} ".format("Trainer", max_trainer_name_len)
    second_line = "{:{}} ".format("---", max_trainer_name_len)
    for i in range(1, num_pok + 1):
        first_line += "| {:<{}} ".format(i, max_pok_len)
        second_line += "| {:{}} ".format("---", max_pok_len)

    first_line += "\n"
    second_line += "\n"

    output_table.insert(0, second_line)
    output_table.insert(0, first_line)

    return output_table

for f in glob.glob("docs/trainer_changes/*.md"):
    print(f)
    train_lines = open(f, "r", encoding="utf-8").readlines()

    trainer_tables = []
    is_table = False
    current_table = []
    table_starts = []
    i = 0
    for line in train_lines:
        if line.startswith("Trainer") and line.endswith("| Pokémons\n"):
            table_starts.append(i)
            is_table = True
        elif is_table:
            if line == "\n":
                is_table = False
                trainer_tables.append(current_table)
                current_table = []
            else:
                if not line.startswith("---"):
                    current_table.append(line.replace("<br>",""))
        i += 1

    i = 0
    for table in trainer_tables:
        tab = format_trainer_table(table)
        for k in range(len(tab)):
            train_lines[k+table_starts[i]] = tab[k]
        i += 1

    open(f, "w", encoding="utf-8").writelines(train_lines)

"🌊🎣🌙☀🌅"