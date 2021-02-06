import requests, json, warnings
from ..warns import BotNotFound

base_url = "https://blackerz.herokuapp.com"

def get_bot_data(id):
    data = requests.get(base_url + '/api/v1/bots/' + id)
    if data.status_code != 200:
        warnings.warn("Bot data not found", BotNotFound);
        return None
    return data.json()
