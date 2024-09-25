import requests
import time
from functions import mainfuns
from functions.headers import headers

#Dict for the task name
task_names = {
    'hamster_youtube_global_video_e43': 'Youtube Ads',
    'hamster_youtube_local_video_e45': 'Youtube Ads',
    'subscribe_hk_facebook_interlude': 'Follow on Facebook',
    'subscribe_telegram_channel_interlude': 'Subscribe Instagram Channel',
    'subscribe_x_account_interlude': 'Follow on Twitter',
    'subscribe_hk_instagram_interlude': 'Follwo on Instagram'
}

#check test name 
def task_name(id):
    for task_name in task_names:
        if id == task_name:
            return task_names[task_name]


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

        return data['tasks']
        
    except:
        mainfuns.log(f"{mainfuns.red}Error connect to owner")
        return None
    
#check the task
def check_task(data, proxy, taskid):
    url ='https://api.hamsterkombatgame.io/interlude/check-task'
    
    
    #get task name
    TaskName = task_name(taskid)
    
    #task id
    payload = {"taskId": taskid}
    
    try:
        response = requests.post(
            url=url,
            headers=headers(data=data),
            json=payload,
            proxies=proxy,
            timeout=20
        )
        
        result = response.json()
                
        
        if result['task']['isCompleted'] == True:
            mainfuns.log(f"{mainfuns.white}{TaskName}: {mainfuns.green}Completed")
        return result
    
        
    except:
        mainfuns.log(f"{mainfuns.red}Error connect to owner")
        return None