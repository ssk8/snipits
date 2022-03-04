from pathlib import Path

basepath = Path(__file__).parent.absolute()
new_path = basepath.parent/"renamed_subs"
new_path.mkdir()

for d in [f for f in basepath.glob("*") if f.is_dir()]:
    for sub in [f for f in d.glob("*English.srt")]:
        new_name = new_path/f"{d.name}_{sub.name}"
        #(d/sub).rename(new_name)
