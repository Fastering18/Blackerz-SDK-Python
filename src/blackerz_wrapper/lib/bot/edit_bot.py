import warnings
from ..warns import Unauthorized
from ..util.base_request import request, default_baseURL

def edit_bot_data(id, data, **anydata):
    auth = {
        "Content-Type": "application/json",
        "Authorization": data["v1Auth"]
    }
    finalData = {}
    if data.get("short_description") : finalData["shortDescription"] = data["short_description"]
    if data.get("long_description") : finalData["longDescription"] = data["long_description"]
    
    data = request(url=str(anydata.get("baseURL") or default_baseURL) + '/api/v1/bots/' + str(id) + "/edit", json=finalData, headers=auth).put()
    
    if data.status_code == 401:
        warnings.warn("Unauthorized to edit bot", Unauthorized)
        return False
    if data.status_code != 201:
        warnings.warn("An error occured when edit bot data, " + str(data.status_code) + ", " + data.reason)
        return False
    return True
