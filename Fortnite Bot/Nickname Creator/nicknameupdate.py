import json
f = open("nicknames.json","r")
nicknames=json.load(f)
f.close()
print(nicknames)
while True:
    inputednick=input("Nickname? ")
    inputedtranslation=input("Translation? ")
    nicknames.update({inputednick:inputedtranslation})
    f = open("nicknames.json","w")
    f.write(json.dumps(nicknames))
    f.close()