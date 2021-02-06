import blackerz-wrapper as blackerz

blackerz.authorize("UleMUVNvxLKnVydMblyOQB", "775363892167573535")
goblox = blackerz.bot("717660707650273280")

bot_data = goblox.bot_data()
print(bot_data)

result = goblox.edit_data(short_description="generated_by_python_lib")
print(result) # boolean indicates success or not