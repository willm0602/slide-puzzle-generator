#prepares an image for the slide puzzle

from PIL import Image, ImageTk, ImageDraw, ImageFont
import PIL

#adds numbers to the tiles and
#
def prep(name,size, labels):
    img = Image.open(name)

    img = img.resize((size,size),PIL.Image.ANTIALIAS) #resizes the image to the desired size
    img = img.convert('RGB')

    if labels:
        draw = ImageDraw.Draw(img) #labels each tile
        font = ImageFont.truetype("arial.ttf", 32)
        for i in range(15):
            dx = i%4
            dy = int(i/4)
            x_draw = size/8+size/4*dx
            y_draw = size/8+size/4*dy
            spot = (x_draw, y_draw)
            draw.text(spot,str(i),font=font, fill=(0,0,0))
    return(img)
