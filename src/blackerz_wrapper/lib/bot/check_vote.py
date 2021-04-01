import warnings
from ..warns import Unauthorized
from ..util.base_request import request, default_baseURL

def check_voted(botId, userID, auth, **anydata):
    headers = {
        "Content-Type": "application/json",
        "Authorization": str(auth)
    }
    try:
        result = request(url=f"{str(anydata.get('baseURL') or default_baseURL)}/api/v1/bots/{str(botId)}/votes?user={str(userID)}", headers=headers).get()
        return result.json()
    except Exception as kslhn:
        return kslhn