import barcode
import time
from barcode.writer import ImageWriter
mylist = []
with open('/Users/steven/Desktop/Pillow/Generator/tnumfile.txt', 'r') as f:
    for line in f.readlines():    #Walks through each line  
        ean = barcode.get('ean', line, writer=ImageWriter())  #issn = barcode.get('issn', '123123123', writer=ImageWriter()) 
        													   #Original Line of Code 
        filename = ean.save(line.strip())		#Saves Line 'tnumfile' as filename
        mylist.insert(0,line.strip() + '.png')



time.sleep(2)
from PIL import Image

for item in mylist:
	im1 = Image.open('/Users/steven/Desktop/Pillow/ticket.png')
	im2 = Image.open('/Users/steven/Desktop/Pillow/Generator/' + item)
	area = (30, 1380, 553, 1660)

	im1.paste(im2, area)
	im1.show()
	# im1.save(line)



# with open('/Users/steven/Desktop/Pillow/Generator/tnumfile.txt', 'r') as f:
#     for line in f.readlines():    #Walks through each line  
#     	im1 = Image.open('/Users/steven/Desktop/Pillow/ticket.png')
# 		im2 = Image.open('/Users/steven/Desktop/Pillow/' + line.strip() + '.png')
# 		area = (40, 1345, 551, 1625)

# 		im1.paste(im2, area)
# 		im1.save('hi' + line)

# im1 = Image.open('/Users/steven/Desktop/Pillow/ticket.png')
# im2 = Image.open('/Users/steven/Desktop/Pillow/bcode.png')
# area = (40, 1345, 551, 1625)

# im1.paste(im2, area)
# im1.show()

#issn = barcode.get('issn', '123123123', writer=ImageWriter())
#filename = issn.save('issn')
#filename

# put image placer in python 

# import libraries in used 
