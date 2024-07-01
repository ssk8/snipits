from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return f"Temp is {get_temp():.1f}°C"

@app.route('/json')
def json():
    return {'temp_c':get_temp(),'unit_c':'°C'}


def get_temp():
    probe_adress = "/sys/bus/w1/devices/28-0000067040a8/w1_slave"

    with open(probe_adress, 'r') as file:
            raw_reading = file.read()

            temp = int(raw_reading[~5:])/1000
            return temp

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8080", debug=True) 

