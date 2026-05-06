from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(40.0, 80.0), 2),
        "distance": round(random.uniform(5.0, 100.0), 2)
    }

@app.route("/data")
def get_data():
    data = generate_sensor_data()

    if data["distance"] < 20:
        data["status"] = "warning"
    else:
        data["status"] = "safe"

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
