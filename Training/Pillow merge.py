from PIL import Image

image1 = Image.open('autumn.jpg')
image2 = Image.open('shore.jpg')

image1 = image1.resize((426, 240))
image2 = image2.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save("merged_image.jpg","JPEG")
new_image.show()