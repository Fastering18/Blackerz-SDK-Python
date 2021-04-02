import blackerz_wrapper as blackerz

blackerz.authorize("V1 Auth")
goblox = blackerz.bot("bot id or client")

bot_data = goblox.bot_data()
print(bot_data)

result = goblox.edit_data(short_description="Discord bot Goblox allow you to calculate number, moderate server, get account information from roblox, etc.")
print(result) # boolean indicates success or not

print(goblox.check_vote("775363892167573535")) # check if userid 775363892167573535 voted the bot


print(blackerz.get_bot("717660707650273280")) # get bot data without auth
