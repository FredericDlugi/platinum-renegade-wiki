import glob

files = glob.glob("docs/pokemon_changes/*.md")

for f in files:
    data = open(f, "r", encoding="utf-8").readlines()

    for i in range(len(data)):
        if data[i].startswith("## "):
            data[i] =data[i].replace(":", "")


    open(f, "w", encoding="utf-8").writelines(data)


"🌊🎣🌙☀🌅"