from pathlib import Path

basepath = Path(__file__).parent.absolute()

for d in basepath.glob("*S02*"):
    sub = list(d.glob("6_English.srt"))[0]
    sub.rename(basepath / f"{d.name}.srt")
