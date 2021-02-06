import blackerz-wrapper as blackerz

blackerz.authorize("auth v1", "bot developer id")
your_bot = blackerz.bot("bot id")

bot_data = your_bot.bot_data()
print(bot_data)

result = your_bot.edit_data(short_description="generated_by_python_lib")
print(result) # boolean indicates success or not
