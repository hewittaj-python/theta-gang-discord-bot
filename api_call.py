import requests
try:
    response = requests.get("https://api.thetagang.com/trades?username=hewittaj")
    print(response.json())
    if response.status_code != 200:
        raise Exception("Error")
except:
    pass