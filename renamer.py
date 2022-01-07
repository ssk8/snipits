from pathlib import Path

print('--------rename-------')

basepath = Path(__file__).parent.absolute()

for n, f in enumerate(sorted(basepath.glob('*.mkv'))):
    new_name = basepath / f"S02E{n+13} {f.name}"
    print(new_name)
    #f.rename(new_name)