import glob

def format_trainer_table(table, table_name):
    output_table = ["" for i in range(len(table))]
    pok = []
    ite = []
    nat = []
    abi = []
    mov = []
    for i in range(len(table)):
        split1 = table[i].split("|")
        print(split1)
        pok.append(split1[0].strip().replace("] ","]<br> "))
        ite.append(split1[1].strip().replace("] ","]<br> "))
        nat.append(split1[2].strip())
        abi.append(split1[3].strip())
        mov.append(split1[4].strip())

    max_len_pok = max(len(x) for x in pok)
    max_len_ite = max(len(x) for x in ite)
    max_len_nat = max(len(x) for x in nat)
    max_len_abi = max(len(x) for x in abi)
    max_len_mov = max(len(x) for x in mov)



    for i in range(len(output_table)):
        output_table[i] = "{:{}} | {:{}} | {:{}} | {:{}} | {:{}}\n".format(pok[i], max_len_pok, ite[i], max_len_ite, nat[i], max_len_nat, abi[i], max_len_abi, mov[i], max_len_mov)




    first_line = "{:{}} | {:{}} | {:{}} | {:{}} | {:{}}\n".format(table_name, max_len_pok, "Item", max_len_ite, "Nature", max_len_nat, "Ability", max_len_abi, "Moves", max_len_mov)
    second_line = "{:{}} | {:{}} | {:{}} | {:{}} | {:{}}\n".format("---", max_len_pok, "---", max_len_ite, "---", max_len_nat, "---", max_len_abi, "---", max_len_mov)

    output_table.insert(0, second_line)
    output_table.insert(0, first_line)

    return output_table

def format_wild_table(table):
    area_map={"Surf":"🌊<br> Surf", "Old Rod": "![][old-rod]<br> Old Rod", "Good Rod": "![][good-rod]<br> Good Rod", "Super Rod": "![][super-rod]<br> Super Rod",
        "Morning": "🌅<br>Morning", "Day":"🌞<br>Day", "Night":"🌙<br>Night", "Poké Radar": "![][poke-radar]<br> Poké Radar", "Honey Tree":"![][honey]<br> Honey Tree"}

    pok = []
    are = []

    for i in range(len(table)):
        split1 = table[i].split("|")
        are.append(split1[0].strip().replace("] ","]<br> "))
        pok.append([s.replace("(", "").replace("] ", "]<br> ").replace("  ", " ").strip() for s in split1[1].split(")")[:-1]])

    are = [area_map[a] for a in are]

    max_len_are = max(len(x) for x in are)

    for k in range(3):
        for i in range(len(pok)):
            if len(pok[i]) > 6:
                next_pok = pok[i][6:]
                pok[i] = pok[i][:6]
                pok.insert(i+1, next_pok)
                are.insert(i+1, "&nbsp;")

    max_len_pok = max(len(x) for x in pok)
    max_len_pok_int = max(len(y) for x in pok for y in x)


    output_table = ["" for i in range(len(pok))]

    for i in range(len(output_table)):
        output_table[i] = "{:{}} ".format(are[i], max_len_are)

    for i in range(len(output_table)):
        for k in range(len(pok[i])):
            output_table[i] += "| {:{}}".format(pok[i][k], max_len_pok_int)
        output_table[i] +="\n"

    first_line = "{:{}} | {:{}} ".format("Area", max_len_are, "Pokémon", max_len_pok_int)
    second_line = "{:{}} | {:{}} ".format("---", max_len_are, "---", max_len_pok_int)

    for i in range(1, max_len_pok):
        first_line += "| {:{}} ".format("&nbsp;", max_len_pok_int)
        second_line += "| {:{}} ".format( "---", max_len_pok_int)


    output_table.insert(0, second_line+"\n")
    output_table.insert(0, first_line+"\n")


    return output_table

for f in glob.glob("docs/wild_pokemon/*.md"):
    train_lines = open(f, "r", encoding="utf-8").readlines()

    trainer_tables = []
    table_names = []
    is_table = False
    current_table = []
    table_starts = []
    i = 0
    for line in train_lines:

        if line.startswith("Area") and line.endswith("Pokémon\n"):
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

    for i in range(len(trainer_tables)):
        len_tab = len(trainer_tables[i])
        tab = format_wild_table(trainer_tables[i])
        print(len_tab)
        for k in range(len(tab)):
            if k < (len_tab + 2):
                train_lines[k+table_starts[i]] = tab[k]
            else:
                train_lines.insert(k+table_starts[i],tab[k])

    open(f, "w", encoding="utf-8").writelines(train_lines)

"🌊🎣🌙☀🌅"