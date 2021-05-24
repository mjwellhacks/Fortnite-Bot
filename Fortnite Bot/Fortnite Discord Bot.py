import discord
from stats import lookup
import json
import urllib.request
import requests
from time import sleep
from gunlookupmod import lookupgun
from cosmeticlookupmod import lookupcos
from path import getpath
from imagemanip import usdtovbuck, vbuckdisplay
global path
path, apikey, discordkey=getpath()
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
with open(path+"link.json","r") as f:
    discordtofortnite=json.load(f)
def lookupmode(name,mode,platform):
    name=name.replace("-","%20")
    stats=lookup(name,platform)
    if stats==False:
        print('Fortnite Bot Returned: "'+"Sorry I Can't Find That User"+'"')
        return "Sorry I Can't Find That User"
    else:
        try:
            print('Fortnite Bot Returned: "'+mode+" Wins: "+str(stats["global_stats"][mode.lower()]["placetop1"])+" "+mode+" Kills: "+str(stats["global_stats"][mode.lower()]["kills"])+'"')
            return mode+" Wins: "+str(stats["global_stats"][mode.lower()]["placetop1"])+"\n"+mode+" Kills: "+str(stats["global_stats"][mode.lower()]["kills"])
        except:
            print('Fortnite Bot Returned: "'+"This Account Is Private."+'"')
            return "This Account Is Private."
def comkillslookupmode(name,platform):
    name=name.replace("-","%20")
    stats=lookup(name,platform)
    if stats==False:
        print('Fortnite Bot Returned: "'+"Sorry I Can't Find That User"+'"')
        return "Sorry I Can't Find That User", -1
    else:
        try:
            print("Fortnite Bot Returned: Combined Kills: "+str(stats["global_stats"]["solo"]["kills"]+stats["global_stats"]["duo"]["kills"]+stats["global_stats"]["squad"]["kills"]))
            return "Combined Kills: "+str(stats["global_stats"]["solo"]["kills"]+stats["global_stats"]["duo"]["kills"]+stats["global_stats"]["squad"]["kills"]), stats["global_stats"]["solo"]["kills"]+stats["global_stats"]["duo"]["kills"]+stats["global_stats"]["squad"]["kills"]
        except:
            print('Fortnite Bot Returned: "'+"This Account Is Private."+'"')
            return "This Account Is Private.", -1
def comwinslookupmode(name,platform):
    name=name.replace("-","%20")
    stats=lookup(name,platform)
    if stats==False:
        print('Fortnite Bot Returned: "'+"Sorry I Can't Find That User"+'"')
        return "Sorry I Can't Find That User", -1
    else:
        try:
            print("Fortnite Bot Returned: Combined Wins: "+str(stats["global_stats"]["solo"]["placetop1"]+stats["global_stats"]["duo"]["placetop1"]+stats["global_stats"]["squad"]["placetop1"]))
            return "Combined Wins: "+str(stats["global_stats"]["solo"]["placetop1"]+stats["global_stats"]["duo"]["placetop1"]+stats["global_stats"]["squad"]["placetop1"]), stats["global_stats"]["solo"]["placetop1"]+stats["global_stats"]["duo"]["placetop1"]+stats["global_stats"]["squad"]["placetop1"]
        except:
            print('Fortnite Bot Returned: "'+"This Account Is Private."+'"')
            return "This Account Is Private.", -1
def gamemode():
    response = requests.get("https://fortniteapi.io/v1/game/modes?lang=en",headers={'Authorization': apikey})
    f = open("gamemode.json", "w")
    f.write(json.dumps(response.json()))
    f.close()
    with open("gamemode.json") as f:
        data = json.loads(f.read())
    i=0
    commonlist=["Solo","Duos","Squads","Trios","Arena","Team Rumble","Creative","Battle Lab","Party Royale"]
    gamemodelist="The Current Gamemodes Are:\n"
    while True:
        try:
            if data["modes"][i]["enabled"]==True and not data["modes"][i]["name"] in commonlist:
                gamemodelist=gamemodelist+"     •"+str(data["modes"][i]["name"])+"\n"
            i=i+1
        except:
            break
    return gamemodelist
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        listmessage=message.content.split()
        if message.author.id == self.user.id:
            return
        if str(message.author.id) in discordtofortnite and len(listmessage)==1:
            listmessage.append(discordtofortnite[str(message.author.id)])
        if message.content.startswith('!soloxbl'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Solo","xbl"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        elif message.content.startswith('!solopsn'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Solo","psn"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        elif message.content.startswith('!solo'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Solo","epic"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        if message.content.startswith('!duosxbl'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Duo","xbl"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        elif message.content.startswith('!duospsn'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Duo","psn"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        elif message.content.startswith('!duos'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Duo","epic"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        if message.content.startswith('!squadsxbl'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Squad","xbl"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        elif message.content.startswith('!squadspsn'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Squad","psn"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        elif message.content.startswith('!squads'):
            if len(listmessage)==2:
                await message.reply(lookupmode(listmessage[1],"Squad","epic"), mention_author=False)
            else:
                await message.reply("Please Specify A User", mention_author=False)
        if message.content.startswith('!kills'):
            if len(listmessage)==2:
                platform=listmessage[0].replace("!kills","")
                platforms=["xbl","psn",""]
                if platform in platforms:
                    if platform=="":
                        platform="epic"
                    returnstring, kills=comkillslookupmode(listmessage[1],platform)
                    mostwanted=discord.File(path+"Achievements/Most Wanted.png")
                    killmonger=discord.File(path+"Achievements/Killmonger.png")
                    killmaster=discord.File(path+"Achievements/Kill Master.png")
                    killleader=discord.File(path+"Achievements/Kill Leader.png")
                    overkill=discord.File(path+"Achievements/Overkill.png")
                    killcrazy=discord.File(path+"Achievements/Kill Crazy.png")
                    if not kills==-1:
                        achieved=[]
                        if kills>10000:
                            achieved.append(mostwanted)
                        elif kills>5000:
                            achieved.append(killmonger)
                        elif kills>4000:
                            achieved.append(killmaster)
                        elif kills>3000:
                            achieved.append(killleader)
                        elif kills>2000:
                            achieved.append(overkill)
                        elif kills>1000:
                            achieved.append(killcrazy)
                        await message.reply(returnstring, files=achieved, mention_author=False)
                    else:
                        await message.reply(returnstring, mention_author=False) 
                else:
                    await message.reply("Please Specify A Platform", mention_author=False)
        if message.content.startswith('!wins'):
            if len(listmessage)==2:
                platform=listmessage[0].replace("!wins","")
                platforms=["xbl","psn",""]
                if platform in platforms:
                    if platform=="":
                        platform="epic"
                    returnstring, wins=comwinslookupmode(listmessage[1],platform)
                    winveteran=discord.File(path+"Achievements/Win Veteran.png")
                    wincrazed=discord.File(path+"Achievements/Win Crazed.png")
                    winsweat=discord.File(path+"Achievements/Win Sweat.png")
                    winhoarder=discord.File(path+"Achievements/Win Hoarder.png")
                    winnerwinner=discord.File(path+"Achievements/Winner Winner.png")
                    if not wins==-1:
                        achieved=[]
                        if wins>400:
                            achieved.append(winveteran)
                        elif wins>300:
                            achieved.append(wincrazed)
                        elif wins>200:
                            achieved.append(winsweat)
                        elif wins>100:
                            achieved.append(winhoarder)
                        elif wins>50:
                            achieved.append(winnerwinner)
                        await message.reply(returnstring, files=achieved, mention_author=False)
                    else:
                        await message.reply(returnstring, mention_author=False) 
                else:
                    await message.reply("Please Specify A Platform", mention_author=False)
        if message.content.startswith('!link'):
            if len(listmessage)==2:
                if message.author.id in discordtofortnite:
                    await message.reply("This Account Is Already Linked", mention_author=False)
                else:
                    discordtofortnite.update({str(message.author.id): listmessage[1]})
                    await message.reply("Account Linked", mention_author=False)
                    with open(path+"link.json","w") as f:
                        f.write(json.dumps(discordtofortnite))
                        f.close()
            else:
                await message.reply("Please Specify An Account", mention_author=False)
        if message.content.startswith('!unlink'):
            if len(listmessage)==2:
                if not str(message.author.id) in discordtofortnite:
                    await message.reply("This Account Is Not Linked", mention_author=False)
                else:
                    print(discordtofortnite[str(message.author.id)])
                    del discordtofortnite[str(message.author.id)]
                    await message.reply("Account Unlinked", mention_author=False)
                    with open(path+"link.json","w") as f:
                        f.write(json.dumps(discordtofortnite))
                        f.close()
            else:
                await message.reply("Please Specify An Account", mention_author=False)
        if message.content.startswith('!gamemode'):
            await message.reply(gamemode(), mention_author=False)
        if message.content.startswith('!lookupgun'):
            if message.content.replace("!lookupgun","")=="" or message.content.replace("!lookupgun","")==" ":
                await message.reply("Please Specify a Gun", mention_author=False)
            else:
                print(message.content.replace("!lookupgun ",""))
                lookuprequest, found=lookupgun(message.content.replace("!lookupgun ",""))
                print(lookuprequest)
                if found==False:
                    await message.reply(lookuprequest, mention_author=False)
                else:
                    await message.reply(lookuprequest, mention_author=False, file=discord.File('temppic.jpg'))
        if message.content.startswith('!lookupcosmetic'):
            if message.content.replace("!lookupcosmetic","")=="" or message.content.replace("!lookupcosmetic","")==" ":
                await message.reply("Please Specify a Cosmetic", mention_author=False)
            else:
                print(message.content.replace("!lookupcosmetic ",""))
                lookuprequest, found=lookupcos(message.content.replace("!lookupcosmetic ",""))
                print(lookuprequest)
                if found==False:
                    await message.reply(lookuprequest, mention_author=False)
                else:
                    await message.reply(lookuprequest, mention_author=False, file=discord.File('tempcos.jpg'))
        if message.content.startswith('!usdtovbuck'):
            vbucksplit=message.content.split()
            text, total=usdtovbuck(float(vbucksplit[1]))
            print(text)
            vbuckdisplay(total, text)
            await message.reply(file=discord.File(path+"vbuckchanged.png"), mention_author=False)
if __name__=="__main__":
    client = MyClient()
    client.run(discordkey)
