from msilib.schema import File
from tabnanny import filename_only
from PIL import Image, ImageDraw
import numpy
import os


def numberCrop(fname, c):
    with Image.open(f"{inputDir}/{fname}") as im:
        x = 102
        y = 354
        size = 480
        im_crop = im.crop(box=(x, y, x+size, y+size))
        im_crop.save(fp=f"{outputDir}/c{c}.png")


def symbolCrop(fname):
    with Image.open(f"{inputDir}/{fname}") as im:
        x = 136
        y = 218
        size = 418
        im_crop = im.crop(box=(x, y, x+size, y+size))
        im_crop.save(fp=f"{outputDir}/symbol.{fname}.png")


def cropFullCard(fname, objname):
    with Image.open(f"{inputDir}/{fname}") as im:
        x, y = 36, 36
        x2, y2 = 646, 1014
        im_crop = im.crop(box=(x, y, x2, y2))

        filename_w_ext = os.path.basename(fname)
        name, _ = os.path.splitext(filename_w_ext)
        scenarionumber = name[0]

        im_crop.save(fp=f"{outputDir}/obj_{scenarionumber}{objname}.png")

def convertToJpeg(fname):
    with Image.open(f"{inputDir}/{fname}") as im:
        filename_w_ext = os.path.basename(fname)
        name, _ = os.path.splitext(filename_w_ext)

        im.save(fp=f"{outputDir}/{name}.jpg")

def symbolNextCrop(fname):
    with Image.open(f"{inputDir}/{fname}").convert("RGBA") as im:
        x = 490
        y = 72
        size = 120
        cutSize = 46
        im_crop = im.crop(box=(x, y, x+size, y+size))

        im_cropArray = numpy.asarray(im_crop)

        # create mask
        polygon = [(0, 0), (0, cutSize), (size-cutSize, size),
                   (size, size), (size, 0)]
        maskIm = Image.new(
            'L', (im_cropArray.shape[0], im_cropArray.shape[1]), 0)
        ImageDraw.Draw(maskIm).polygon(polygon, outline=1, fill=1)
        mask = numpy.array(maskIm)

        # assemble new image (uint8: 0-255)
        newImArray = numpy.empty(im_cropArray.shape, dtype='uint8')

        # colors (three first columns, RGB)
        newImArray[:, :, :3] = im_cropArray[:, :, :3]

        # transparency (4th column)
        newImArray[:, :, 3] = mask*255

        # back to Image from numpy
        newIm = Image.fromarray(newImArray, "RGBA")
        newIm.save(fp=f"{outputDir}/nextSymbol.{fname}.png")


inputDir = "./FileCrop/input/png"
outputDir = "./FileCrop/output"

c = 1

# obj_{N}{L|LL}_f.png
objnames = ['A_f', 'A_b', 'AA_f', 'AA_b',
            'B_f', 'B_b', 'BB_f', 'BB_b',
            'C_f', 'C_b', 'CC_f', 'CC_b']

for i, filename in enumerate(os.listdir(inputDir)):
    #numberCrop(filename, c)
    # symbolCrop(filename)
    # symbolNextCrop(filename)

    #cropFullCard(filename, objname=objnames[i % len(objnames)])

    if filename.endswith("png") and "esq" not in filename:
        convertToJpeg(filename)

    c += 1
