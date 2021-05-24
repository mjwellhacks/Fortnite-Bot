import requests
import json
import urllib
import difflib
import math
from time import sleep
from path import getpath
import threading
global path
path, apikey, discordkey=getpath()
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
def updatelist():
    while True:
        response = requests.get("https://fortniteapi.io/v2/items/list?lang=en",headers={'Authorization': 'fcde20a2-71497aa3-fa8e3b78-ff54ce5d'})
        data = response.json()
        global nametonum
        nametonum={}
        i=0
        while True:
            try:
                nametonum.update({str(str(data["items"][i]["name"]).capitalize().rstrip()+" "+data["items"][i]["type"]["id"]).capitalize().rstrip():i})
                i=i+1
            except:
                print("Updated Name To Num")
                f = open("cosmeticnametonum.json", "w")
                f.write(json.dumps(nametonum))
                f.close()
                break
        sleep(30)
updateliststart = threading.Thread(target=updatelist)
updateliststart.start()
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