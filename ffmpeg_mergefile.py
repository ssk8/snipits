from pathlib import Path

print('--------merge_file-------')

basepath = Path(__file__).parent.absolute()
vids_dir = 'test_dir'

files = (basepath/vids_dir).glob('*.mkv')

lines = ""

for file in files:
    print(file.name)
    lines+=f"file '{vids_dir}/{file.name}\n"

with open("merge_file.txt", "w") as merge_file:
        merge_file.writelines(lines)

print('--------Done-------\nnow try:')
print("ffmpeg -f concat -i merge_file.txt -c copy merged.mkv")
