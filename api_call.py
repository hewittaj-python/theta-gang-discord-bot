import requests
import json

def dump_to_json(json_object, filename):
    """
    Dump .json object to file for testing purposes
    """
    with open(f"{filename}", "w") as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)

def get_user_trades(user):
    """
    Gets specified user's trades from site
    """
    trades_list = []
    try:
        response = requests.get(f"https://api.thetagang.com/trades?username={user}").json()
        dump_to_json(response, f"{user}_trades.json")
        
        if response.status_code != 200:
            raise Exception("Error")
    except:
        pass


def get_latest_homepage_trades():
    """
    Gets home page trades
    """
    trades_list = []
    try:
        start_page_number = 0
        response = requests.get(f" https://api.thetagang.com/timeline?page={start_page_number}").json()
        dump_to_json(response, "homepage_trades.json")
        
        if response.status_code != 200:
            raise Exception("Error")
    except:
        pass


def read_from_json():
    pass