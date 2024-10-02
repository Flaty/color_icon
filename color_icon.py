from PIL import Image

image = Image.open('example.jpg')
image_converter= image.convert('RGB')

red, green, blue = image_converter.split()

red_crop_left = red.crop((50, 0, image_converter.width, image_converter.height))
red_crop_left_right = red.crop((25, 0, image_converter.width - 25, image_converter.height))

blue_crop_left = blue.crop((0, 0, image_converter.width - 50, image_converter.height))
blue_crop_left_right = blue.crop((25, 0, image_converter.width - 25, image_converter.height))

green_crop = green.crop((25,0,image_converter.width - 25, image_converter.height))

red_blend = Image.blend(red_crop_left,red_crop_left_right, 0.5)
blue_blend = Image.blend(blue_crop_left, blue_crop_left_right, 0.5)

image_merge = Image.merge('RGB', (red_blend, green_crop, blue_blend))
image_merge.thumbnail((80,80))

image_merge.save('output.jpg')
