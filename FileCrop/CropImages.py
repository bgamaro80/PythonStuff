from PIL import Image, ImageDraw
import numpy
import os

def numberCrop(fname, c):
    with Image.open(f"{inputDir}/{fname}") as im:
        x = 102
        y = 354
        size = 480
        im_crop = im.crop(box=(x,y,x+size,y+size))
        im_crop.save(fp=f"{outputDir}/c{c}.png")
            
def symbolCrop(fname):
    with Image.open(f"{inputDir}/{fname}") as im:
        x = 136
        y = 218
        size = 418
        im_crop = im.crop(box=(x,y,x+size,y+size))
        im_crop.save(fp=f"{outputDir}/symbol.{fname}.png")

def symbolNextCrop(fname):
    with Image.open(f"{inputDir}/{fname}").convert("RGBA") as im:
        x = 490
        y = 72
        size = 120
        cutSize = 46
        im_crop = im.crop(box=(x,y,x+size,y+size))
        
        im_cropArray = numpy.asarray(im_crop)
        
        # create mask
        polygon = [(0,0), (0,cutSize), (size-cutSize,size), (size,size), (size,0)]
        maskIm = Image.new('L', (im_cropArray.shape[0], im_cropArray.shape[1]), 0)
        ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
        mask = numpy.array(maskIm)
        
        # assemble new image (uint8: 0-255)
        newImArray = numpy.empty(im_cropArray.shape,dtype='uint8')

        # colors (three first columns, RGB)
        newImArray[:,:,:3] = im_cropArray[:,:,:3]

        # transparency (4th column)
        newImArray[:,:,3] = mask*255          

        # back to Image from numpy
        newIm = Image.fromarray(newImArray, "RGBA")
        newIm.save(fp=f"{outputDir}/nextSymbol.{fname}.png")
            
            
inputDir = "./input"
outputDir = "./output"

c = 1

for filename in os.listdir(inputDir):
    #numberCrop(filename, c)
    symbolCrop(filename)
    #symbolNextCrop(filename)
    c += 1