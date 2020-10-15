from PIL import Image, ImageTk, ImageDraw, ImageFont
import PIL
def resize(name,size):
    img = Image.open(name)
    img = img.resize((size,size),PIL.Image.ANTIALIAS)
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 32)
    for i in range(0,15):
        dx = i%4
        dy = int(i/4)
        spot = (32+64*dx,32+64*dy)
        draw.text(spot,str(i),font=font, fill=(0,0,0))
    return(img)
