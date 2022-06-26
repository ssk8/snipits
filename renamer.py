from pathlib import Path

print('--------rename-------')

basepath = Path(__file__).parent.absolute()

for n, f in enumerate(sorted(basepath.glob('*.mkv'))):
    name = f.name.replace("_", " ")[7:]
    new_name = basepath / f"{name}"
    print(new_name)
    #f.rename(new_name)
