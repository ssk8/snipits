from pathlib import Path
from shutil import copy

basepath = Path(__file__).parent.absolute()/"Subs"

for d in [f for f in basepath.glob("*") if f.is_dir()]:
    for sub in [f for f in d.glob("*English.srt")]:
        new_name = f"{d.name}_{sub.name}"
        copy (sub, new_name)
