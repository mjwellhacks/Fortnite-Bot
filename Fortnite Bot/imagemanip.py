from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw
import math
from path import getpath
path, apikey, discordkey=getpath()
def vbuckdisplay(amount, text):
    font = ImageFont.truetype(path+"BurbankBigCondensed-Black.otf", 90)
    img = Image.open(path+'vbuck.png')
    draw = ImageDraw.Draw(img)
    draw.text((275, 100),str(amount)+" vbucks".upper(),(255,255,255),font=font)
    draw.text((20, 300),str(text).upper(),(255,255,255),font=font)
    img.save(path+'vbuckchanged.png')
def dollardisplay(amount):
    font = ImageFont.truetype(path+"BurbankBigCondensed-Black.otf", 90)

    img = Image.open(path+'dollar.png')

    draw = ImageDraw.Draw(img)
    draw.text((275, 100),str(amount)+" dollars".upper(),(43,255,75),font=font)
    img.save(path+'dollarchanged.png')
def solve_linear(equation,var='x'):
    expression = equation.replace("=","-(")+")"
    grouped = eval(expression.replace(var,'1j'))
    return -grouped.real/grouped.imag
def usdtovbuck(usd):
    large=int(usd/79.99)
    left = usd%79.99
    largemed=int(left/31.99)
    left = left%31.99
    medium=int(left/19.99)
    left = left%19.99
    small=left/7.99
    left = left/7.99
    returnstring=""
    if not large==0:
        returnstring+="Large Packs: "+str(large)+"\n"
    if not largemed==0:
        returnstring+="Large Medium Packs: "+str(largemed)+"\n"
    if not medium==0:
        returnstring+="Medium Packs: "+str(medium)+"\n"
    if not small==0:
        if int(small)==0:
            returnstring+="Small Packs: 1"
        else:
            returnstring+="Small Packs: "+str(math.ceil(small))
    return returnstring, str(round(large*13500+largemed*5000+medium*2800+small*1000))