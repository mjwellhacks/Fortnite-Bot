import requests
import json
def lookup(name,platform):
    if platform=="epic":
        fullplatform=""
    else:
        fullplatform="&platform="+platform
    response = requests.get("https://fortniteapi.io/v1/lookup?username="+name+fullplatform,headers={'Authorization': 'key'})
    f = open("id.json", "w")
    f.write(json.dumps(response.json()))
    f.close()
    f = open("id.json", "r")
    userid=json.load(f)
    f.close()
    if userid["result"]==True:
        response = requests.get("https://fortniteapi.io/v1/stats?account="+userid["account_id"], headers={'Authorization': 'key'})
        f = open("stats.json", "w")
        f.write(json.dumps(response.json()))
        f.close()
        f = open("stats.json", "r")
        stats=json.load(f)
        f.close()
        return stats
    else:
        return False
