import requests,json


def IP_location(ip):
    URL = 'http://freeapi.ipip.net/' + ip
    try:
        r = requests.get(URL, timeout=3)
        json_data = r.json()
        if json_data[2]:
            return (json_data[2])
        else:
            return "未知"
    except requests.RequestException as e:
        return "未知"


#print(IP_location("202.103.224.68"))

