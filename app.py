from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")

        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != "404":
            weather = {
                "city": data["name"],
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"].title()
            }

    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
