import json
from pyowm import OWM


def check_weather(
    api_key="c84c2f255787c9dfc3d1c8b3795e4686",
):  # use a public api key in default
    # this method gets the actual data from openweathermap.org
    print("Checking weather in Tel Aviv, Israel...")
    output = {}
    owm = OWM(api_key)

    if owm.is_API_online():
        print("OpenWeatherMap API is ONLINE!")
        country = "Israel"
        city = "Tel Aviv"
        print("City is " + city)
        print("Country is " + country)
        obs = owm.weather_at_place(city + "," + country)

        w = obs.get_weather()
        output["clouds"] = w.get_clouds()
        output["rain"] = w.get_rain()
        output["snow"] = w.get_snow()
        output["wind"] = w.get_wind()
        output["humidity"] = w.get_humidity()
        output["pressure"] = w.get_pressure()
        output["temperature"] = w.get_temperature("celsius")
        output["status"] = w.get_detailed_status()
        output["sunrise"] = w.get_sunrise_time()
        output["sunset"] = w.get_sunset_time()
    else:
        print("OWM API is OFFNLINE, FAILED")
        output["status"] = "FAILED"
    return json.dumps(output, indent=3)
