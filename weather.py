#!/usr/bin/python3
import requests
import dotenv
import os
import json

def get_current_forecast(lat, long, api_key, metric):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_call = base_url + f"lat={lat}&lon={long}&units={metric}&appid={api_key}".format(lat, long, metric, api_key)
    resp = requests.get(api_call)
    json_response = json.loads(resp.text)
    conditions = json_response['weather'][0]['main']
    temperature = json_response['main']['temp']
    icon = json_response['weather'][0]['icon']
    nerd_icon = ""
    match icon:
        case "01d":
            nerd_icon = ""
        case "01n":
            nerd_icon = ""
        case "02d":
            nerd_icon = ""
        case "02n":
            nerd_icon = ""
        case "03d":
            nerd_icon = ""
        case "03n":
            nerd_icon = ""
        case "04d":
            nerd_icon = ""
        case "04n":
            nerd_icon = ""
        case "09d":
            nerd_icon = ""
        case "10d":
            nerd_icon = ""
        case "10n":
            nerd_icon = ""
        case "11d":
            nerd_icon = ""
        case "11n":
            nerd_icon = ""
        case "13d":
            nerd_icon = ""
        case "13n":
            nerd_icon = ""
        case "50d":
            nerd_icon = ""
        case "50n":
            nerd_icon = ""
        case _:
            nerd_icon = ""
            
    return conditions, temperature, nerd_icon


def main():
    dotenv.load_dotenv()
    api_key = os.getenv("API_KEY")
    lat, long = os.getenv("LAT"), os.getenv("LONG")
    metric = os.getenv("METRIC")
    current_forecast = get_current_forecast(lat, long, api_key, metric)
    condition = current_forecast[0]
    temp = current_forecast[1]
    icon = current_forecast[2]
    print(condition, temp, icon)
     
if __name__ == "__main__":
    main()
