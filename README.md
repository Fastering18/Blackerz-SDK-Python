# Python Blackerz API-Wrapper
Python SDK for interact with our API

__Example Post Bot Description__
```py
import blackerz_api_wrapper as blackerz

blackerz.authorize("V1auth", "bot developer id")
goblox = blackerz.bot("bot_id")

bot_data = goblox.bot_data()
print(bot_data)

result = goblox.edit_data(short_description="generated_by_python_lib")
print(result) # boolean indicates success or not
```  

Get your **V1 auth** by login to our website then visit your profile, here the link  
https://blackerz.herokuapp.com/

<br>

Made by Fastering18, join our support server https://discord.gg/t7zJBwynFU for more information.