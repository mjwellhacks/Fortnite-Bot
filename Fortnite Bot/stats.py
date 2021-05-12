import requests
import json
from path import getpath
path, apikey, discordkey=getpath()
def lookup(name,platform):
    if platform=="epic":
        fullplatform=""
    else:
        fullplatform="&platform="+platform
    response = requests.get("https://fortniteapi.io/v1/lookup?username="+name+fullplatform,headers={'Authorization': apikey})
    f = open(path+"id.json", "w")
    f.write(json.dumps(response.json()))
    f.close()
    f = open(path+"id.json", "r")
    userid=json.load(f)
    f.close()
    if userid["result"]==True:
        response = requests.get("https://fortniteapi.io/v1/stats?account="+userid["account_id"], headers={'Authorization': apikey})
        f = open(path+"stats.json", "w")
        f.write(json.dumps(response.json()))
        f.close()
        f = open(path+"stats.json", "r")
        stats=json.load(f)
        f.close()
        return stats
    else:
        return False