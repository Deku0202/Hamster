import requests
from functions import mainfuns
from functions.headers import headers

#request the user data
def info(data, proxy):
    url = 'https://api.hamsterkombatgame.io/interlude/sync'
    
    try:
        response = requests.post(
            url=url,
            headers=headers(data=data),
            proxies=proxy,
            timeout=20,
        )
        data = response.json()
        total_coins = data["interludeUser"]["balanceDiamonds"]
        
        #print the total coin
        mainfuns.log(f"{mainfuns.green}Total Coins: {mainfuns.white}{total_coins:.2f}")
        
        
    except:
        return None