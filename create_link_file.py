import argparse
import glob
import re
import os
os.sep = "/"
poks = glob.glob("docs/img/pokemon/*.png")

for p in poks:
    name = p.replace("\\","/").split("/")[-1].replace(".png","")
    if name.isdigit():
        os.rename(p, "docs/img/pokemon/{:03}.png".format(int(name)))

imgs = glob.glob("docs/img/**/*.png")
imgs.sort()
lines = []
for img in imgs:
    img_name = img.replace("\\","/").split("/")[-1].replace(".png","")
    lines.append("[{}]: {}\n".format(img_name, img.replace("\\","/").replace("docs","")))

open("links1.md","w").writelines(lines)

