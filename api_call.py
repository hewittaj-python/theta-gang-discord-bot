import requests
import json

def dump_to_json(json_object):
    """
    Dump .json object to file for testing purposes
    """
    with open("trades.json", "w") as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)

def get_user_trades(user):
    """
    Gets specified user's trades from site
    """
    trades_list = []
    try:
        response = requests.get(f"https://api.thetagang.com/trades?username={user}").json()
        dump_to_json(response)
        # for info in response_json:
        #     print(info)
        print_json(response)
        
        if response.status_code != 200:
            raise Exception("Error")
    except:
        pass


def get_homepage_trades():
    """
    Gets home page trades
    """
    pass

def print_json(json_object):
    """ 
    Create a formatted string of the .json object
    """
    text = json.dumps(json_object, indent=4)
    print(text)

def read_from_json():
    pass