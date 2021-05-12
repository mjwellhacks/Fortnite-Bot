import requests
import json
import urllib
import difflib
import math
from time import sleep
from path import getpath
global path
path, apikey, discordkey=getpath()
with open(path+"cosmeticnametonum.json") as f:
    nametonum = json.loads(f.read())
with open(path+"Nickname Creator/nicknamescos.json") as f:
    translations = json.loads(f.read())
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
while True:
    if connect()==True:
        break
    sleep(1)
response = requests.get("https://fortniteapi.io/v2/items/list?lang=en",headers={'Authorization': apikey})
f = open(path+"cosmetics.json", "w")
f.write(json.dumps(response.json()))
f.close()
with open(path+"cosmetics.json") as f:
    data = json.loads(f.read())
def lookupcos(name):
    if not name.title() in nametonum.keys():
        name=nameclosest(name)
    returnstring=""
    try:
        i=nametonum[name]
        returnstring+="Description: "+str(data["items"][i]["description"])+"\n"
        returnstring+="Rarity: "+str(data["items"][i]["rarity"]["id"])+"\n"
        try:
            returnstring+="Series: "+str(data["items"][i]["series"]["name"])+"\n"
        except:
            pass
        returnstring+="Released: "+str(data["items"][i]["releaseDate"])+"\n"
        returnstring+="Last Apperance: "+str(data["items"][i]["lastAppearance"])
        urllib.request.urlretrieve(data["items"][i]["images"]["full_background"], "tempcos.jpg")
        found=True
    except:
        returnstring+="Can't Find Cosmetic"
        found=False
    return returnstring, found
def nameclosest(lookup):
    lookup=nicktranslate(lookup)
    words=nametonum.keys()
    name=difflib.get_close_matches(lookup, words)
    if len(name)>0:
        return difflib.get_close_matches(lookup, words)[0]
        print(difflib.get_close_matches(lookup, words)[0])
    else:
        return ""
def nicktranslate(lookup):
    lookup=lookup.lower()
    lookuplist=lookup.split()
    for item in translations:
        if item in lookuplist:
            lookuplist[lookuplist.index(item)]=translations[item]
    iterartor=" "
    returnstring=iterartor.join(lookuplist)
    return returnstring.title()

