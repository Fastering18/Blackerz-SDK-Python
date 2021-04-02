import requests, json, warnings
from ..util.base_request import request, default_baseURL, loopThread

def upload_servercount(client, auth, **anydata):
    #if not auth or not servers: return False, "parameters auth and servers is required"
    headers = {
        "Content-Type": "application/json",
        "Authorization": auth
    }
    data = {
        "servercount": len(client.guilds)
    }
    try:
        result = request(url=str(anydata.get("baseURL") or default_baseURL) + "/api/v1/bots/" + str(client.user.id) + "/edit/servercount", json=data,headers=headers).post()
        if result.json().error != "null": return False, result.json().error
    except Exception as keslhn:
        return False, keslhn

def servercount_manager(client, auth):
    loopThread(upload_servercount, args=[client, auth])