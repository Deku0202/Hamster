import requests
from functions import mainfuns
from functions.headers import headers

#request the skin
def task_list(data, proxy):
    url = 'https://api.hamsterkombatgame.io/interlude/list-tasks'
    
    try:
        response = requests.post(
            url=url,
            headers=headers(data=data),
            proxies=proxy,
            timeout=20,
        )
        data = response.json()

        return data['task']
        
    except:
        mainfuns.log(f"{mainfuns.red}Error connect to owner")
        return None