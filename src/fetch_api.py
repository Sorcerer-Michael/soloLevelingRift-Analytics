from dotenv import load_dotenv
import os
import requests

# load env retrive get our key
load_dotenv()
key = os.getenv('RIOTKey')

# note if key is present or not
if not key:
    raise ValueError("No API key found!")
print("Key obtained!")

# get account by riotID using url and key
url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/iliketerraria727/honi"
headers = {'X-Riot-Token': key}

response = requests.get(url, headers=headers, timeout=10)
print(response.status_code)
print(response.json())
