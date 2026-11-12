from dotenv import load_dotenv
import os
import requests

# load env retrive get our key and account information
load_dotenv()
key = os.getenv("RIOTKey")

# note if key is present or not
if not key:
    raise ValueError("No API key found!")

MY_TAG = os.getenv("RIOTTag")
MY_USER = os.getenv("RIOTUsername")
HEADERS = {"X-Riot-Token": key}


def get_account(user, tag, region="americas"):
    # set url with region and account info(user and tag)
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{user}/{tag}"

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.json()


def get_match_IDs(puuid, region="americas", match_count=20, match_type="ranked"):
    # set url with region and puuid
    url = (
        f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    )
    params = {"type": match_type, "count": match_count}

    response = requests.get(url, params=params, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.json()
