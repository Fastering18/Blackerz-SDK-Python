import warnings
from ..warns import Unauthorized
from ..util.base_request import request, default_baseURL

def check_voted(botId, userID, auth, **anydata):
    headers = {
        "Content-Type": "application/json",
        "Authorization": str(auth)
    }
    try:
        result = request(url="{0}/api/v1/bots/{1}/votes?user={2}".format(str(anydata.get('baseURL') or default_baseURL), str(botId), str(userID)), headers=headers).get()
        return result.json()
    except Exception as kslhn:
        return kslhn