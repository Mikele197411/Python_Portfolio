import requests

def get_weather(url):
    result=requests.get(url)
    if(result.status_code==200):
        return result.json()
    else:
        print("Something Wrong")