import glob
import time
import sys

base_dir = '/sys/bus/w1/devices/'
# Get all the filenames begin with 28 in the path base_dir.
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
def read_rom():
    name_file=device_folder+'/name'
    f = open(name_file,'r')
    return f.readline()
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    # Analyze if the last 3 characters are 'YES'.
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    # Find the index of 't=' in a string.
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        # Read the temperature .
        temp_string = lines[1][equals_pos+2:]
        return float(temp_string) / 1000.0
 
    print(' rom: '+ read_rom())

def main():
    file_name = sys.argv[-1] 
    if __file__.endswith(file_name):
       print("add a new filename please") 
       return
    file_name+=".txt"
    while True:
        data = f"{time.time():.0f} {read_temp():06.3f}\n"
        print(data, end="")
        with open(file_name, "a") as text_file:
            text_file.write(data)
        time.sleep(1)

if __name__ == "__main__":
    main()
