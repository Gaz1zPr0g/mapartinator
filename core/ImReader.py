from PIL import Image

# This file works with users image returning some useful data


def get_image_size(fname):
    im = Image.open(fname)
    im.close()
    return im.size


def get_image_pixels(fname):
    im = Image.open(fname)
    rgbim = im.convert("RGB")
    pixarr = [[0 for j in range(im.size[1])] for i in range(im.size[0])]
    im.close()

    for i in range(rgbim.size[0]):
        for j in range(rgbim.size[1]):
            pixarr[i][j] = rgbim.getpixel((i, j))
    return pixarr