import requests
import datetime
from functions import mainfuns
from functions.headers import headers

#get the timestamp
def timestamp():
    current_time = datetime.datetime.now()
    return int(current_time.timestamp())

#request the skin
def skin(data, proxy, number):
    url = 'https://api.hamsterkombatgame.io/interlude/buy-skin'
    
    #get timestamp
    time = timestamp()
    
    #get the skin info
    skin = "skin" + number
    
    #get the payload
    payload = {"skinId": "skin7", "timestamp": time}
    
    try:
        response = requests.post(
            url=url,
            headers=headers(data=data),
            json=payload,
            proxies=proxy,
            timeout=20,
        )
        data = response.json()
        
        #print if the skin is already bought 
        if 'error_code' in data:
            mainfuns.log(f"{mainfuns.yellow}{data['error_message']}")
        
        
        #print the total coin
        mainfuns.log(f"{mainfuns.green}Total Coins: {mainfuns.white}{total_coins:.2f}")
    
        
        
    except:
        return None