from PIL import Image

im1 = Image.open('/Users/steven/Desktop/Pillow/ticket.png')
im2 = Image.open('/Users/steven/Desktop/Pillow/Generator/32999024.png')
area = (40, 1345, 551, 1625)

im1.paste(im2, area)
im1.show()






