from dotenv import load_dotenv
import os
import requests
import json
from urllib.parse import quote

# load env retrive get our key and account information
load_dotenv()
MY_KEY = os.getenv("RIOT_API_KEY")
MY_TAG = os.getenv("RIOT_PLAYER_TAG")
MY_USER = os.getenv("RIOT_PLAYER_USERNAME")

checklist = ["RIOT_API_KEY", "RIOT_PLAYER_TAG", "RIOT_PLAYER_USERNAME"]

# note if user info is present or not
for info in checklist:
    if not os.getenv(info):
        raise ValueError(f"Missing: {info}")

HEADERS = {"X-Riot-Token": MY_KEY}

# Other constants
RAW_DIR = "data/raw"


# account info (includes puuid, riot tag, and username)
def get_account(user, tag, region="americas"):
    # set url with region and account info(user and tag)
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{quote(user)}/{quote(tag)}"

    response = requests.get(
        url, headers=HEADERS, timeout=10
    )  # get and store string data
    response.raise_for_status()  # check for errors

    # save info to python dictionary
    return response.json()


# by default will return the last 20 match ids
def get_match_ids(puuid, region="americas", match_count=20, match_type="ranked"):
    # set url with region and puuid
    url = (
        f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
    )
    params = {"type": match_type, "count": match_count}

    response = requests.get(url, params=params, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.json()


# gets ALL info acording to match id (things like wins, metadata, kills) this is for all "participants"
def get_match_info(match_id, region="americas"):
    # set url with matchid and region
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}"

    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    return response.json()


def save_raw_match(match_id, match_data, folder="data/raw"):
    # make sure directory already exists
    os.makedirs(folder, exist_ok=True)

    # open and write to file
    with open(f"{folder}/{match_id}.json", "w") as file:
        json.dump(match_data, file, indent=2)
