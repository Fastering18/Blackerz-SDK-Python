import requests, json, warnings
from ..warns import Unauthorized

base_url = "https://blackerz.herokuapp.com"


def edit_bot_data(id, data):
    auth = {
        "Content-Type": "application/json",
        "Authorization": data["v1Auth"],
        "clientId": data["authorID"]
    }
    finalData = {}
    if "short_description" in data : finalData["shortDescription"] = data["short_description"]
    
    data = requests.post(base_url + '/api/v1/bots/' + str(id) + "/edit", json = finalData, headers = auth)
    
    if data.status_code == 401:
        warnings.warn("Bot data not found", Unauthorized)
        return False
    if data.status_code != 201:
        warnings.warn("An error occured when edit bot data, " + str(data.status_code) + ", " + data.reason)
        return False
    return True
