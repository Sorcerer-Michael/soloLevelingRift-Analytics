from src.riot_api import (
    get_account,
    get_match_ids,
    get_match_info,
    save_raw_match,
    MY_TAG,
    MY_USER,
    RAW_DIR,
)
import os
import time

if __name__ == "__main__":
    account = get_account(MY_USER, MY_TAG)
    match_ids = get_match_ids(account["puuid"])

    for match_id in match_ids:
        # check if file already exists.
        if os.path.exists(f"{RAW_DIR}/{match_id}.json"):
            continue
        save_raw_match(match_id, get_match_info(match_id))
        time.sleep(1)
