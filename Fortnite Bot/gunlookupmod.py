import requests
import json
import urllib
import difflib
import math
from time import sleep
from path import getpath
global path
path, apikey, discordkey=getpath()
with open(path+"nametonum.json") as f:
    nametonum = json.loads(f.read())
with open(path+"Nickname Creator/nicknames.json") as f:
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
	sleep(1) #sleep
response = requests.get("https://fortniteapi.io/v1/loot/list?lang=en",headers={'Authorization': apikey})
f = open(path+"yeet.json", "w")
f.write(json.dumps(response.json()))
f.close()
with open(path+"yeet.json") as f:
    data = json.loads(f.read())
def lookupgun(name):
    name=nameclosest(name)
    returnstring=""
    try:
        i=nametonum[name]
        returnstring+="Name: "+str(data["weapons"][i]["rarity"]).capitalize()+" "+str(data["weapons"][i]["name"])+"\n"
        urllib.request.urlretrieve(data["weapons"][i]["images"]["background"], "temppic.jpg")
        returnstring+="\tDescription: "+str(data["weapons"][i]["description"])+"\n"
        returnstring+="\tHeadshot Multiplier: "+str(data["weapons"][i]["mainStats"]["DamageZone_Critical"])+"\n"
        returnstring+="\tHeadshot Damage: "+str(math.floor(int(data["weapons"][i]["mainStats"]["DmgPB"])*float(data["weapons"][i]["mainStats"]["DamageZone_Critical"])))+"\n"
        returnstring+="\tDamage: "+str(data["weapons"][i]["mainStats"]["DmgPB"])+"\n"
        returnstring+="\tDPS: "+str(int(data["weapons"][i]["mainStats"]["DmgPB"])*float(data["weapons"][i]["mainStats"]["FiringRate"]))+"\n"
        returnstring+="\tAmmo: "+str(data["weapons"][i]["mainStats"]["ClipSize"])+"\n"
        found=True
    except:
        returnstring+="Can't Find Gun"
        found=False
    return returnstring, found
def nameclosest(lookup):
    lookup=nicktranslate(lookup)
    words=nametonum.keys()
    name=difflib.get_close_matches(lookup, words)
    if len(name)>0:
        return difflib.get_close_matches(lookup, words)[0]
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