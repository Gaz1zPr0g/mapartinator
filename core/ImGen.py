from PIL import Image
import numpy as np
import core.ImReader as ir

carpets = [
    #R    G    B
    (25,  25,  25),
    (76,  76,  76),
    (102, 76,  51),
    (153, 51,  51),
    (102, 127, 51),
    (51,  76,  178),
    (127, 204, 25),
    (76,  127, 153),
    (127, 63,  178),
    (216, 127, 51),
    (153, 153, 153),
    (178, 76,  216),
    (102, 153, 216),
    (229, 229, 51),
    (242, 127, 165),
    (255, 255, 255)
]
NoSilkTouch = [
#    R    G    B
    (25,  25,  25),
    (37,  22,  16),
    (112, 2,   0),
    (0,   124, 0),
    (92,  25,  29),
    (76,  50,  35),
    (86,  44,  62),
    (76,  82,  42),
    (60,  77,  78),
    (76,  76,  76),
    (102, 76,  51),
    (76,  62,  92),
    (142, 60,  46),
    (255, 0,   0),
    (153, 51,  51),
    (129, 86,  49),
    (87,  92,  92),
    (103, 117, 53),
    (0,   217, 58),
    (159, 82,  36),
    (102, 127, 51),
    (22,  126, 134),
    (122, 73,  88),
    (51,  76,  178),
    (148, 63,  97),
    (160, 77,  78),
    (20,  180, 133),
    (20,  180, 133),
    (143, 119, 72),
    (112, 112, 112),
    (151, 109, 77),
    (135, 107, 98),
    (58,  142, 140),
    (149, 87,  108),
    (186, 133, 36),
    (127, 204, 25),
    (76,  127, 153),
    (112, 108, 138),
    (127, 178, 56),
    (127, 63,  178),
    (64,  64,  255),
    (216, 127, 51),
    (127, 167, 150),
    (74,  128, 255),
    (153, 153, 153),
    (178, 76,  216),
    (102, 153, 216),
    (167, 167, 167),
    (229, 229, 51),
    (164, 168, 184),
    (92,  219, 213),
    (242, 127, 165),
    (216, 175, 147),
    (209, 177, 161),
    (250, 238, 77),
    (199, 199, 199),
    (247, 233, 163),
    (255, 252, 245),
    (255, 255, 255)
]
silkTouch = [
#    R    G    B
    (25, 25, 25),
    (37, 22, 16),
    (112, 2, 0),
    (0, 124, 0),
    (92, 25, 29),
    (76, 50, 35),
    (86, 44, 62),
    (76, 82, 42),
    (60, 77, 78),
    (76, 76, 76),
    (102, 76, 51),
    (76, 62, 92),
    (142, 60, 46),
    (255, 0, 0),
    (153, 51, 51),
    (129, 86, 49),
    (87, 92, 92),
    (103, 117, 53),
    (0, 217, 58),
    (159, 82, 36),
    (102, 127, 51),
    (22, 126, 134),
    (122, 73, 88),
    (189, 48, 49),
    (51, 76, 178),
    (148, 63, 97),
    (160, 77, 78),
    (20, 180, 133),
    (20, 180, 133),
    (143, 119, 72),
    (112, 112, 112),
    (151, 109, 77),
    (135, 107, 98),
    (58, 142, 140),
    (149, 87, 108),
    (186, 133, 36),
    (127, 204, 25),
    (76, 127, 153),
    (112, 108, 138),
    (127, 178, 56),
    (127, 63, 178),
    (64, 64, 255),
    (216, 127, 51),
    (127, 167, 150),
    (74, 128, 255),
    (153, 153, 153),
    (178, 76, 216),
    (102, 153, 216),
    (167, 167, 167),
    (229, 229, 51),
    (164, 168, 184),
    (92, 219, 213),
    (242, 127, 165),
    (216, 175, 147),
    (209, 177, 161),
    (250, 238, 77),
    (199, 199, 199),
    (247, 233, 163),
    (255, 252, 245),
    (255, 255, 255)
]


def get_RGB_sum(rgbl):
    return rgbl[0] + rgbl[1] + rgbl[2]


def create_color_list(filename,
                isCarpetsUsed,
                isNoSilkTouchUsed,
                iSSilkTouchUsed,
                isPrevNeeded,
                window):
    progressBar = window["-GENERATION PROGRESS-"]
    imSize = ir.get_image_size(filename)
    pixelsRGBs = ir.get_image_pixels(filename)
    colorsList = list(set(carpets * isCarpetsUsed + NoSilkTouch * isNoSilkTouchUsed + silkTouch * iSSilkTouchUsed))

    window["-GENERATION CONDITION TEXT-"].update("preparing palette...")
    # sorting palette by the rgb sum simple bubble sort but whatever
    for i in range(len(colorsList)):
        for j in range(i + 1, len(colorsList)):
            rgbS = get_RGB_sum(colorsList[j])
            prevS = get_RGB_sum(colorsList[j - 1])
            if prevS > rgbS:
                colorsList[j], colorsList[j - 1] = colorsList[j - 1], colorsList[j]



    # creating new image pixels matrix
    newPixelsRGBs = [[(0, 0, 0) for i in range(imSize[0])] for i in range(imSize[1])]

    newPixelsRGBsnp = np.array(newPixelsRGBs)

    alreadyDone = {"255 255 255": (255, 255, 255)}
    # Image generation
    # Should check if this color already was processed
    # Change .putpixel() to something that works faster

    window["-GENERATION CONDITION TEXT-"].update("changing colors...")

    for i in range(imSize[0]):
        for j in range(imSize[1]):
            rgb = f"{pixelsRGBs[i][j][0]} {pixelsRGBs[i][j][1]} {pixelsRGBs[i][j][2]}"
            revi = imSize[0] - i - 1
            revj = imSize[1] - j - 1
            if rgb in alreadyDone:
                newPixelsRGBsnp[j, i] = alreadyDone[rgb]
            else:
                colors = np.array(colorsList)
                color = np.array(pixelsRGBs[i][j])
                distances = np.sqrt(np.sum((colors - color)**2, axis=1))
                smallestId = np.where(distances == np.amin(distances))

                try:
                    newPixelsRGBsnp[j, i] = colors[smallestId]
                except:
                    newPixelsRGBsnp[j, i] = colors[smallestId[0][0]]

                alreadyDone[rgb] = newPixelsRGBsnp[j, i]

            progressBar.update_bar(int((i / imSize[0]) * 100))


    window["-GENERATION CONDITION TEXT-"].update("generating preview...")

    prevIm = Image.fromarray(newPixelsRGBsnp.astype("uint8"), "RGB")
    prevIm.save("temp_prev.png")

    window["-GENERATION CONDITION TEXT-"].update("Done")

    if isPrevNeeded:
        window["-UPDATE PREVIEW-"].update("temp_prev.png")
    progressBar.update_bar(100)
    return newPixelsRGBsnp

