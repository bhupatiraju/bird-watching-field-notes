import requests
from dotenv import load_dotenv
import os

load_dotenv()
eBird_key = os.getenv("EBIRD_KEY")


def search_bird(name):
    headers = {
        "authority": "api.ebird.org",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://ebird.org",
        "pragma": "no-cache",
        "referer": "https://ebird.org/",
        "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    }

    params = {
        "locale": "en_IN",
        "cat": "species",
        "key": eBird_key,
        "q": name,
    }

    return requests.get(
        "https://api.ebird.org/v2/ref/taxon/find", params=params, headers=headers
    ).json()
