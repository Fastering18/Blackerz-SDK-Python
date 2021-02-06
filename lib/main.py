from .bot import edit_bot, bot_data
Data = {}

def authorize(Auth, authorID):
    Data["AuthorizationV1"] = Auth;
    Data["authorID"] = authorID;

def get_bot(botID):
    return bot_data.get_bot_data(botID)

class bot():
    def __init__(self, botID):
        auth = {
            "v1Auth": Data["AuthorizationV1"],
            "authorID": Data["authorID"]
        }
        self.botID = botID;
        self.authorization = auth
        self.clientType = "clientID"
    def bot_data(self):
        self.data = bot_data.get_bot_data(self.botID)
        return self.data
    def edit_data(self, **data):
        short_description = data.get('short_description', None)
        if short_description == None: return;
        
        author = self.authorization
        data = {
            "v1Auth": author["v1Auth"],
            "authorID": author["authorID"],
            "short_description": short_description
        }
        result = edit_bot.edit_bot_data(self.botID, data)
        
        return result
