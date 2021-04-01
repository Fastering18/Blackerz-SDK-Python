from .bot import edit_bot, bot_data, servercount, check_vote
Data = {}

def authorize(Auth):
    Data["AuthorizationV1"] = Auth;

def get_bot(botID):
    return bot_data.get_bot_data(botID)

def checkIfClient(client):
    return str(type(client)) == "<class 'discord.client.Client'>" and isinstance(client.guilds, (list))

class bot():
    def __init__(self, bot, **anydata):
        auth = Data["AuthorizationV1"] if "AuthorizationV1" in Data else None

        self.botID = bot
        self.authorization = anydata.get("authorization") or auth
        self.baseURL = anydata.get("base_url") or "https://blackerz.herokuapp.com"

        if self.authorization == None: 
            ValueError("authorization is None, please do blackerz.Authorize or add 'authorization' key parameter")
            return
        if checkIfClient(self.botID): servercount.servercount_manager(self.botID, self.authorization)

    def bot_data(self):
        self.data = bot_data.get_bot_data(self.botID, baseURL=self.baseURL)
        return self.data
    def edit_data(self, **data):
        short_description = data.get('short_description', None)
        long_description = data.get('long_description', None)
        
        data = {
            "v1Auth": self.authorization
        }
        if long_description: data["long_description"] = long_description
        if short_description: data["short_description"] = short_description

        result = edit_bot.edit_bot_data(self.botID.user.id if checkIfClient(self.botID) else self.botID, data, baseURL=self.baseURL)
        
        return result
    def check_vote(self, userid):
        return check_vote.check_voted(self.botID.user.id if checkIfClient(self.botID) else self.botID, userid, self.authorization, baseURL=self.baseURL)
