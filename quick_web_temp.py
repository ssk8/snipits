from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return get_temp()

def get_temp():
    probe_adress = "/sys/bus/w1/devices/28-0000067040a8/w1_slave"

    with open(probe_adress, 'r') as file:
            raw_reading = file.read()

            temp = int(raw_reading[~5:])/1000
            return f"Temp is {temp:.2f}°C"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="8080", debug=True) 
