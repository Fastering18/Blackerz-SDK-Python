import warnings
from ..warns import BotNotFound
from ..util.base_request import request, default_baseURL

def get_bot_data(id, **anydata):
    data = request(url="{0}/api/v1/bots/{1}".format(str(anydata.get("baseURL") or default_baseURL), str(id))).get()
    if data.status_code != 200:
        warnings.warn("Bot data not found", BotNotFound);
        return None
    return data.json()
