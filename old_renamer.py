import os
dir_path = os.path.dirname(os.path.realpath(__file__))

print('--------------------')

files = os.listdir(dir_path)
files.remove('renamer.py')
files.sort(key=lambda n:int(n.split('.')[0]))
for n, file in enumerate(files):
    if file.endswith('.py'): continue
    new_name = f"{str(n).zfill(4)}.jpg" 
    print('old: ', os.path.join(dir_path, file))
    print('new: ', os.path.join(dir_path, new_name))
    os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_name))
