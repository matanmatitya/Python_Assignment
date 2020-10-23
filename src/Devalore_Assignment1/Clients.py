from ..Devalore_Assignment1 import WeatherApi as WAPI
from ..Devalore_Assignment1 import WeatherWebApp as WAPP
import requests
import json


class GenericClient:
    """
    generic client class, its single responsiblity is to get weather data (derived classes will implement accordingly)
    to provide the ability to switch between the Prod and the Dev environments, this class is defines
    the funcionalities of any client that the system will use.
    """
    def get_weather_data(self):
        pass


class ProdClient(GenericClient):
    def get_weather_data(self):
        # return a response from weather api (the "logic" - WeatherApi)
        return WAPI.check_weather()


class DevClient(GenericClient):
    def get_weather_data(self):
        # actually connects the weather web app and returns a mocked response.
        WAPP.run_app()
        try:
            resp = requests.get("http://127.0.0.1:5000/")
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        return json.dumps(resp.json(), indent=2)
