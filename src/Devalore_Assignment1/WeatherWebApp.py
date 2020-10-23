from flask import Flask, jsonify, request
import json
import threading
import logging
import os
from ..Devalore_Assignment1 import WeatherApi as WAPI

app = Flask(__name__)
app.logger.disabled = True
log = logging.getLogger("werkzeug")
log.disabled = True


@app.route("/")
def get_weather_from_OWM():
    # simple endpoint that returns the weather data as response.
    return jsonify(json.loads(WAPI.check_weather()))


def run_app():
    # function to run the weather web app in different thread
    os.environ["WERKZEUG_RUN_MAIN"] = "true"
    t_webApp = threading.Thread(name="Weather Web App", target=app.run)
    t_webApp.setDaemon(True)
    t_webApp.start()
