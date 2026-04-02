import requests
from flask import Flask, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# Déposez votre code à partir d'ici :

@app.route("/contact")
def MaPremiereAPI():
    return render_template("contact.html")

@app.get("/paris")
def api_paris():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m"
    response = requests.get(url)
    data = response.json()
    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])
    n = min(len(times), len(temps))
    result = [
        {"datetime": times[i], "temperature_c": temps[i]}
        for i in range(n)
    ]
    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.route("/histogramme")
def monhistogramme():
    return render_template("histogramme.html")

# Ne rien mettre après ce commentaire

@app.get("/nice")
def api_nice():
    url = "https://api.open-meteo.com/v1/forecast?latitude=43.7102&longitude=7.2620&hourly=shortwave_radiation"
    response = requests.get(url)
    data = response.json()
    times = data.get("hourly", {}).get("time", [])
    radiation = data.get("hourly", {}).get("shortwave_radiation", [])
    n = min(len(times), len(radiation))
    result = [
        {"datetime": times[i], "radiation_wm2": radiation[i]}
        for i in range(n)
    ]
    return jsonify(result)

@app.route("/atelier")
def monatelier():
    return render_template("atelier.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
