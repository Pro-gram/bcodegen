import barcode
from barcode.writer import ImageWriter

with open('/Users/steven/Desktop/Pillow/Generator/tnumfile.txt', 'r') as f:
    for line in f.readlines():    #Walks through each line  
        ean = barcode.get('ean', line, writer=ImageWriter())  #issn = barcode.get('issn', '123123123', writer=ImageWriter()) 
        													   #Original Line of Code 
        filename = ean.save(line)		#Saves Line 'tnumfile' as filename


from PIL import Image

im1 = Image.open('/Users/steven/Desktop/Pillow/ticket.png')
im2 = Image.open('/Users/steven/Desktop/Pillow/bcode.png')
area = (40, 1345, 551, 1625)

im1.paste(im2, area)
im1.show()

#issn = barcode.get('issn', '123123123', writer=ImageWriter())
#filename = issn.save('issn')
#filename

# put image placer in python 

# import libraries in used 
