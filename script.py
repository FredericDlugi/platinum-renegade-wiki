import glob

paths = glob.glob("docs/wild_pokemon/*.md")

for p in paths:
    with open(p, "r", encoding="UTF-8") as f:
        title = f.readline().replace("#", "").strip()

        pa = p.replace("\\","/").replace("docs/","").replace(".md","/")
        print(f"[{title}]: ./{pa}")