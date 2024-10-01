from PIL import Image

image = Image.open('example.jpg')
image_converter= image.convert('RGB')

red, green, blue = image_converter.split()

crop_red_image = (50, 0, image_converter.width, image_converter.height)
crop_green_image = (0, 0, image_converter.width - 50, image_converter.height)
crop_blue_image = (25, 0, image_converter.width - 25, image_converter.height)

image_merge= Image.merge('RGB', (red.crop(crop_red_image), green.crop(crop_green_image), blue.crop(crop_blue_image)))

image_merge.thumbnail((80,80))
image_merge.save('output.jpg')
