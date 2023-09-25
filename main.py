from litemapy import Schematic, Region, BlockState
from PIL import Image
import PySimpleGUI as sg
import os.path
import math


carpets = [
    #R    G    B    ID
    (25,  25,  25,  29),
    (76,  76,  76,  21),
    (102, 76,  51,  26),
    (153, 51,  51,  28),
    (102, 127, 51,  27),
    (51,  76,  178, 25),
    (127, 204, 25,  19),
    (76,  127, 153, 23),
    (127, 63,  178, 24),
    (216, 127, 51,  15),
    (153, 153, 153, 22),
    (178, 76,  216, 16),
    (102, 153, 216, 17),
    (229, 229, 51,  18),
    (242, 127, 165, 20),
    (255, 255, 255, 8),
]
NoSilkTouch = [
#    R    G    B    ID
    (25,  25,  25,  29),
    (37,  22,  16,  51),
    (112, 2,   0,   35),
    (0,   124, 0,   7),
    (92,  25,  29,  54),
    (76,  50,  35,  48),
    (86,  44,  62,  57),
    (76,  82,  42,  49),
    (60,  77,  78,  43),
    (76,  76,  76,  21),
    (102, 76,  51,  26),
    (76,  62,  92,  47),
    (142, 60,  46,  50),
    (255, 0,   0,   4),
    (153, 51,  51,  28),
    (129, 86,  49,  34),
    (87,  92,  92,  45),
    (103, 117, 53,  41),
    (0,   217, 58,  33),
    (159, 82,  36,  37),
    (102, 127, 51,  27),
    (22,  126, 134, 55),
    (122, 73,  88,  46),
    (51,  76,  178, 25),
    (148, 63,  97,  53),
    (160, 77,  78,  42),
    (20,  180, 133, 58),
    (20,  180, 133, 59),
    (143, 119, 72,  13),
    (112, 112, 112, 11),
    (151, 109, 77,  10),
    (135, 107, 98,  44),
    (58,  142, 140, 56),
    (149, 87,  108, 38),
    (186, 133, 36,  40),
    (127, 204, 25,  19),
    (76,  127, 153, 23),
    (112, 108, 138, 39),
    (127, 178, 56,  1),
    (127, 63,  178, 24),
    (64,  64,  255, 12),
    (216, 127, 51,  15),
    (127, 167, 150, 61),
    (74,  128, 255, 32),
    (153, 153, 153, 22),
    (178, 76,  216, 16),
    (102, 153, 216, 17),
    (167, 167, 167, 6),
    (229, 229, 51,  18),
    (164, 168, 184, 9),
    (92,  219, 213, 31),
    (242, 127, 165, 20),
    (216, 175, 147, 60),
    (209, 177, 161, 36),
    (250, 238, 77,  30),
    (199, 199, 199, 3),
    (247, 233, 163, 2),
    (255, 252, 245, 14),
    (255, 255, 255, 8)
]
silkTouch = [
#    R    G    B    ID
    (25,  25,  25,  29),
    (37,  22,  16,  51),
    (112, 2, 0, 35),
    (0, 124, 0, 7),
    (92, 25, 29, 54),
    (76, 50, 35, 48),
    (86, 44, 62, 57),
    (76, 82, 42, 49),
    (60, 77, 78, 43),
    (76, 76, 76, 21),
    (102, 76, 51, 26),
    (76, 62, 92, 47),
    (142, 60, 46, 50),
    (255, 0, 0, 4),
    (153, 51, 51, 28),
    (129, 86, 49, 34),
    (87, 92, 92, 45),
    (103, 117, 53, 41),
    (0, 217, 58, 33),
    (159, 82, 36, 37),
    (102, 127, 51, 27),
    (22, 126, 134, 55),
    (122, 73, 88, 46),
    (189, 48, 49, 52),
    (51, 76, 178, 25),
    (148, 63, 97, 53),
    (160, 77, 78, 42),
    (20, 180, 133, 58),
    (20, 180, 133, 59),
    (143, 119, 72, 13),
    (112, 112, 112, 11),
    (151, 109, 77, 10),
    (135, 107, 98, 44),
    (58, 142, 140, 56),
    (149, 87, 108, 38),
    (186, 133, 36, 40),
    (127, 204, 25, 19),
    (76, 127, 153, 23),
    (112, 108, 138, 39),
    (127, 178, 56, 1),
    (127, 63, 178, 24),
    (64, 64, 255, 12),
    (216, 127, 51, 15),
    (127, 167, 150, 61),
    (74, 128, 255, 32),
    (153, 153, 153, 22),
    (178, 76, 216, 16),
    (102, 153, 216, 17),
    (167, 167, 167, 6),
    (229, 229, 51, 18),
    (164, 168, 184, 9),
    (92, 219, 213, 31),
    (242, 127, 165, 20),
    (216, 175, 147, 60),
    (209, 177, 161, 36),
    (250, 238, 77, 30),
    (199, 199, 199, 3),
    (247, 233, 163, 2),
    (255, 252, 245, 14),
    (255, 255, 255, 8),
]



def get_RGB_sum(rgbl):
    return rgbl[0] + rgbl[1] + rgbl[2]

# creating a window
def create_window():
    sg.theme("dark grey 11")
    start_message = [
        [sg.Text("This is masterpiece of enginnering to make it possible create ")],
        [sg.Text("Obtainable blocks"),
         sg.Checkbox("carpets", enable_events=True, key="-CARPETS-"),
         sg.Checkbox("survival no silk touch", enable_events=True, key="-SURVIVAL NO SILK TOUCH-"),
         sg.Checkbox("survival silk touch", enable_events=True, key="-SURVIVAL SILK TOUCH-")]
    ]

    file_list = [
        [
            sg.Text("image folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse()
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(44, 25), key="-FILE LIST-"
            )
        ],
    ]

    inserted_image = [
        [sg.Text("your image: "), sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Text("size "), sg.Text(size=(40, 1), key="-IMAGE SIZE-")],
        [sg.Image(key="-IMAGE INSRT-")],
    ]
    generate_image_button = [
        [sg.Button("Generate image", key="-GENERATE IMAGE-")],
        [sg.ProgressBar(1000, orientation='h', size=(20, 20), key="-GENERATION PROGRESS-")]
    ]
    layout = [
            [sg.Column(start_message), sg.Column(generate_image_button)],
            [sg.HSeparator()],
            [sg.Column(file_list), sg.VSeparator(), sg.Column(inserted_image)],
    ]

    Window = sg.Window("The mapartinator 3000", layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True)
    return Window

def get_image_size(fname):
    im = Image.open(fname)
    return im.size

def get_image_pixels(fname):
    im = Image.open(fname)
    rgbim = im.convert("RGB")
    pixarr = [[0 for j in range(im.size[1])] for i in range(im.size[0])]


    for i in range(rgbim.size[0]):
        for j in range(rgbim.size[1]):
            pixarr[i][j] = rgbim.getpixel((i, j))
    return pixarr

# creating a new image
def create_prev(fname,
                obCarpets,
                obSlkT,
                obnSlkT,
                progressBar):
    imSize = get_image_size(fname)
    pixelsRGBs = get_image_pixels(fname)
    colorsList = list(set(carpets * obCarpets + silkTouch * obSlkT + NoSilkTouch * obnSlkT))

    for i in range(len(colorsList)):
        for j in range(i + 1, len(colorsList)):
            rgbS = get_RGB_sum(colorsList[j])
            prevS = get_RGB_sum(colorsList[j - 1])
            if prevS > rgbS:
                colorsList[j], colorsList[j - 1] = colorsList[j - 1], colorsList[j]



    newPixelsRGBs = [[0 for i in range(imSize[0])] for i in range(imSize[1])]

    for i in range(imSize[0]):
        for j in range(imSize[1]):
            colorDiffs = []
            r, g, b = pixelsRGBs[i][j]
            for color in colorsList:
                cr, cg, cb, id = color
                colorDiff = math.sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
                colorDiffs.append((colorDiff, color))
            closeColor = min(colorDiffs)[1]
            newPixelsRGBs[i][j] = (closeColor[0], closeColor[1], closeColor[2])
            progressBar.update_bar(i / 2)

    prevIm = Image.new('P', (imSize[0], imSize[1]))
    for i in range(imSize[0]):
        for j in range(imSize[1]):
            prevIm.putpixel((i, j), newPixelsRGBs[i][j])
            progressBar.update_bar(500 + i/2)
    prevIm.save("D:/war thunder/test_output.png")



# saving a .litematica file
#def create_litematica():


window = create_window()
progressBar = window["-GENERATION PROGRESS-"]
bcarp = False
bnst = False
bst = False
creative = False
filename = "-"
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "-FOLDER-":     # Folder was opened for the first time
        folder = values["-FOLDER-"]
        try:
            filelist = os.listdir(folder)
        except:
            filelist = []

        filenames = [
            file
            for file in filelist
            if os.path.isfile(os.path.join(folder, file))
            and file.lower().endswith((".png", ".jpeg"))
        ]
        window["-FILE LIST-"].update(filenames)
    elif event == "-FILE LIST-": # File was checked
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE INSRT-"].update(filename=filename)
            window["-IMAGE SIZE-"].update(get_image_size(filename))
            get_image_pixels(filename)
        except:
            pass
    elif event == "-CARPETS-":
        bcarp = values["-CARPETS-"]
    elif event == "-SURVIVAL NO SILK TOUCH-":
        bnst = values["-SURVIVAL NO SILK TOUCH-"]
    elif event == "-SURVIVAL SILK TOUCH-":
        bst = values["-SURVIVAL SILK TOUCH-"]
    elif event == "-GENERATE IMAGE-" and filename != "-":
        create_prev(filename, bcarp, bnst, bst, progressBar)




window.close()

# maps size
# 128x128 pixels
# 61 color

