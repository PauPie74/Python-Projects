# https://www.tutorialspoint.com/python_pillow/python_pillow_quick_guide.htm

from PIL import Image

im = Image.open("autumn.jpg")

im.show()

imr = im.rotate(45)
imr.show()

r, g, b = im.split()
im = Image.merge("RGB", (b, g, r))
im.show()

im = Image.merge("RGB", (g, b, r))
im.show()

from PIL import Image, ImageFilter

ImageFilter.GaussianBlur(radius=20)

blurImage = im.filter(ImageFilter.GaussianBlur(10))
blurImage.show()

cropped = im.crop((1,2,900,900))
cropped.show()

flippedImage = im.transpose(Image.FLIP_LEFT_RIGHT)
flippedImage.show()

resized_im = im.resize((round(im.size[0]*0.1), round(im.size[1]*0.1)))
resized_im.show()

from PIL import Image, ImageDraw, ImageFont

width, height = im.size

draw = ImageDraw.Draw(im)
text = "watermark"

font = ImageFont.truetype('arial.ttf', 100)
textwidth, textheight = draw.textsize(text, font)

margin = 10
x = width - textwidth - margin
y = height - textheight - margin

draw.text((x, y), text, font=font)
im.show()


from PIL.ImageFilter import (
   BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
   EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

img1 = im.filter(CONTOUR)
img1.show()

from PIL import Image, ImageDraw

img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)

draw.rectangle(
   (150, 125, 300, 200),
   fill=(0, 255, 0),
   outline=(0, 0, 255))
img.show()