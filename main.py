from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def getBinMsg(msg):
    lst = []
    for char in msg:
        lst.append(ord(char))

    msg = ""
    for each in lst:
        msg += "{0:b}".format(each)

    return msg 

def writeLines(draw, msg, img_size, txt_color, font, text_size):
    leng = len(msg)
    idx = 0
    for x in range(1, img_size[0] - 1, text_size):
        for y in range(1, img_size[1] - 1, text_size):
            draw.text((y,x),msg[idx % leng], txt_color, font=font)
            idx += 1

name = input("What will be the name of this image be?: ")
wid = int(input("What is the width of this image?: "))
ht = int(input("What is the height of this image?: "))
img_size = (wid, ht)
txt_color = input("What's the color of the text?: ")
back = input("What is the background for this immage?: ")
msg = input("What is the message to be converted?: ")
msg = getBinMsg(msg)
text_size = int(input("What size will the font be?: "))


try:
    img = Image.new("RGB", img_size, back)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype("arial.ttf", text_size)
    # draw.text((x, y),"Sample Text",(r,g,b))
    writeLines(draw, msg, img_size, txt_color, font, text_size)
    name += ".jpg"
    img.save(name)
except Exception as e:
    print("\n" + "Error occured: " + str(e))

print("\n" + "Image " + name + " has been succesfully created!")