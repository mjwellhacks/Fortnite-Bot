import json
f = open("nicknamescos.json","r")
nicknames=json.load(f)
f.close()
print(nicknames)
while True:
    inputednick=input("Nickname? ")
    inputedtranslation=input("Translation? ")
    nicknames.update({inputednick:inputedtranslation})
    f = open("nicknamescos.json","w")
    f.write(json.dumps(nicknames))
    f.close()