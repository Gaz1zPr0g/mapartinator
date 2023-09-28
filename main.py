from litemapy import Schematic, Region, BlockState
from PIL import Image
import PySimpleGUI as sg
import numpy as np
import os.path
import math

# All the colors that can be showed on the map

colorIDs = {
    (0, 217, 58): 33,
    (112, 2, 0): 35,
    (76, 76, 76): 21,
    (151, 109, 77): 10,
    (76, 50, 35): 48,
    (76, 62, 92): 47,
    (112, 112, 112): 11,
    (22, 126, 134): 55,
    (86, 44, 62): 57,
    (242, 127, 165): 20,
    (216, 175, 147): 60,
    (127, 178, 56): 1,
    (37, 22, 16): 51,
    (149, 87, 108): 38,
    (127, 204, 25): 19,
    (143, 119, 72): 13,
    (60, 77, 78): 43,
    (159, 82, 36): 37,
    (112, 108, 138): 39,
    (129, 86, 49): 34,
    (199, 199, 199): 3,
    (76, 127, 153): 23,
    (103, 117, 53): 41,
    (167, 167, 167): 6,
    (127, 63, 178): 24,
    (255, 0, 0): 4,
    (20, 180, 133): 59,
    (160, 77, 78): 42,
    (0, 124, 0): 7,
    (142, 60, 46): 50,
    (58, 142, 140): 56,
    (122, 73, 88): 46,
    (64, 64, 255): 12,
    (25, 25, 25): 29,
    (216, 127, 51): 15,
    (178, 76, 216): 16,
    (51, 76, 178): 25,
    (102, 127, 51): 27,
    (148, 63, 97): 53,
    (153, 153, 153): 22,
    (186, 133, 36): 40,
    (74, 128, 255): 32,
    (250, 238, 77): 30,
    (102, 153, 216): 17,
    (255, 252, 245): 14,
    (164, 168, 184): 9,
    (127, 167, 150): 61,
    (92, 25, 29): 54,
    (20, 180, 133): 58,
    (247, 233, 163): 2,
    (76, 82, 42): 49,
    (229, 229, 51): 18,
    (92, 219, 213): 31,
    (255, 255, 255): 8,
    (102, 76, 51): 26,
    (87, 92, 92): 45,
    (153, 51, 51): 28,
    (135, 107, 98): 44,
    (189, 48, 49): 52,
    (209, 177, 161): 36
}

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


# returns tuple of (width, height)
def get_image_size(fname):
    im = Image.open(fname)
    im.close()
    return im.size


# returns RGB pixels matrix
def get_image_pixels(fname):
    im = Image.open(fname)
    rgbim = im.convert("RGB")
    pixarr = [[0 for j in range(im.size[1])] for i in range(im.size[0])]
    im.close()

    for i in range(rgbim.size[0]):
        for j in range(rgbim.size[1]):
            pixarr[i][j] = rgbim.getpixel((i, j))
    return pixarr


def create_window():
    sg.theme("dark grey 11")

    # text and checkboxes layout
    start_message = [
        [sg.Text("Create your own map art by converting image to litematica file!")],
        [sg.Button("Select blocks", key="-BLOCK SELECTOR-")],
        [sg.Text("Obtainable blocks"),
         sg.Checkbox("carpets", enable_events=True, key="-CARPETS-"),
         sg.Checkbox("survival no silk touch", enable_events=True, key="-SURVIVAL NO SILK TOUCH-"),
         sg.Checkbox("survival silk touch", enable_events=True, key="-SURVIVAL SILK TOUCH-")],
        [sg.Text("map art previews"),
         sg.Checkbox("image preview", enable_events=True, key="-IMAGE PREVIEW-", default=True),
         sg.Checkbox("mapart preview", enable_events=True, key="-MAP ART PREVIEW-", default=True)],
    ]

    # layout for file list and search
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

    # layout for image name, size and image itself
    inserted_image = [
        [sg.Text("Your image | size", key="-IMAGE PREVIEW TEXT-"), sg.Text(key="-IMAGE SIZE-")],
        [sg.Image(key="-IMAGE INSRT-", size=(1, 1))],
    ]

    # layout for preview image
    preview_image = [
        [sg.Text("map art preview", key="-MAP PREVIEW TEXT-")],
        [sg.Image(key="-UPDATE PREVIEW-", size=(256, 256))],
    ]


    # layout for generation button and progressbar
    generate_image_button = [
        [sg.Button("Generate image", key="-GENERATE IMAGE-"),
         sg.Text("Waiting for image", key="-GENERATION CONDITION TEXT-")],

        [sg.ProgressBar(100, orientation='h', size=(20, 20), key="-GENERATION PROGRESS-")]
    ]

    # main layout
    layout = [
            [sg.Column(start_message), sg.Column(generate_image_button)],
            [sg.HSeparator()],
        
            [sg.Column(file_list),
             sg.VSeparator(),
             sg.Column(inserted_image, expand_y = True),
             sg.Column(preview_image, expand_y = True)],

            [sg.HSeparator()],
    ]

    Window = sg.Window("The mapartinator 3000", layout, finalize=True, element_justification="top")
    return Window

def create_selector_window():

    def name(name):
        size = 10
        spaces = size - len(name) - 2
        return sg.Text(name + " " + " " * spaces,size=(size, 1), justification="l", pad=(0, 0))

    sg.theme("dark grey 11")
    top_text = [
        [sg.Text("Select which blocks will match next colors")],

    ]

    dropboxes_l = [
        # 0 - Grass (ID 1)
        [name("Grass"),
         sg.Combo([
                "Grass block",
                "Slime block"
         ], default_value="Grass block", size=(30, 1))],
        # 1 - Sand  (ID 2)
        [name("Sand"),
         sg.Combo([
                "Sand", "Birch planks", "Birch log vertical",
                "Birch stripped log", "Birch wood",
                "Birch stripped wood", "Birch sign",
                "Birch pressure plate", "Birch Trapdoor",
                "Birch stairs", "Birch slabs", "Birch fence",
                "Birch fence gate", "Birch door",
                "Sandstone", "Sandstone stairs", "Sandstone slabs",
                "Sandstone fence", "Chiseled sandstone", "Smooth sandstone",
                "Smooth sandstone stairs", "Smooth sandstone slabs",
                "Cut sandstone", "Cut sandstone slabs"
        ], default_value="Birch slabs", size=(30, 1))],
        # 2 - Wool  (ID 3)
        [name("Wool"),
         sg.Combo([
                "Cobweb",
                "Mushroom stem",
                "White candle"
         ], default_value="White candle", size=(30, 1))],
        # 3 - Fire  (ID 4)
        [name("Fire"),
         sg.Combo([
             "Lava", "TNT",
             "Fire", "Redstone block"
         ], default_value="Redstone block", size=(30, 1))],
        # 4 - Ice   (ID 5)
        [name("Ice"),
         sg.Combo([
             "Ice", "Frosted ice",
             "Packed ice", "Blue ice"
         ], default_value="Packed ice", size=(30, 1))],
        # 5 - Metal (ID 6)
        [name("Metal"),
         sg.Combo([
             "Block of iron", "Iron door",
             "Brewing stand", "Heavy weight pressure plate",
             "Iron trapdoor", "lantern",
             "Anvil", "Grindstone",
             "Soul fire lantern", "Lodestone"
         ], default_value="Heavy weight pressure plate", size=(30, 1))],
        # 6 - Plant (ID 7)
        [name("Plant"),
         sg.Combo([
             "Oak leaves", "Spruce leaves",
             "Birch leaves", "Jungle leaves",
             "Acacia leaves", "Dark oak leaves",
             "Mangrove leaves", "Azalea",
             "Flowering azalea", "Block of bamboo"
         ], default_value="Oak leaves", size=(30, 1))],
        # 7 - Snow  (ID 8)
        [name("Snow"),
         sg.Combo([
             "Snow", "Snow block",
             "Wool", "Stained glass",
             "White carpet", "White shulcker box",
             "Glazed terracotta", "White concrete",
             "White concrete powder", "Powder snow"
         ], default_value="Wool", size=(30, 1))],
        # 8 - Clay (only option) (ID 9)
        # 9 - Dirt  (ID 10)
        [name("Dirt"),
         sg.Combo([
             "Dirt", "Coarse dirt",
             "Dirt path", "Rooted dirt",
             "Granite",
             "Granite stairs", "Granite slabs",
             "Granite wall", "Polished granite",
             "Polished granite stairs", "Polished granite slabs",
             "Jungle planks", "Jungle log vertical",
             "Jungle stripped log", "Jungle wood",
             "Jungle stripped wood", "Jungle sign",
             "Jungle pressure plate", "Jungle trapdoor",
             "Jungle stairs", "Jungle slabs",
             "Jungle fence", "Jungle fence gate",
             "Jungle door", "Jukebox",
             "Brown mushroom block", "Packed mud"
         ], default_value="Jungle slabs", size=(30, 1))],
        # 10 - Stone (ID 11)
        [name("Stone"),
         sg.Combo([
             "Stone", "Stone stairs", "Stone slabs",
             "Andesite", "Andesite stairs",
             "Andesite wall", "Polished andesite",
             "Polished andesite stairs", "Polished andesite slabs",
             "Cobblestone", "Cobblestone stairs",
             "Cobblestone slabs", "Cobblestone wall",
             "Gravel", "Smooth stone", "Smooth stone slab",
             "Stone pressure plate",
             "Stone bricks", "Stone brick stairs",
             "Stone brick slabs", "Stone brick wall",
             "Mossy stone bricks", "Mossy stone brick stairs",
             "Mossy stone brick slabs",
             "Mossy cobblestone", "Mossy cobblestone stairs",
             "Mossy cobblestone slabs", "Mossy cobblestone wall",
             "Gold ore", "Iron ore", "Coal ore",
             "Diamond ore", "Redstone ore",
             "Emerald ore", "Copper ore",
             "Lapis lazuli ore",
             "Furnace", "Smoker", "Blast Furnace",
             "Dispenser", "Observer", "Piston",
             "Sticky piston", "Hopper", "Ender chest",
         ], default_value="Cobblestone slabs", size=(30, 1))],
        # 11 - Water (ID 12)
        [name("Water"),
         sg.Combo([
             "Kelp", "Seagrass",
             "Water", "Bubble Column",
             "Waterlogged leaves"
         ], default_value="Water", size=(30, 1))],
        # 12 - Wood (ID 13)
        [name("Wood"),
        sg.Combo([
            "Oak planks", "Oak log vertical",
            "Oak stripped log", "Oak wood",
            "Oak stripped wood", "Oak sign",
            "Oak door", "Oak pressure plate",
            "Oak trapdoor", "Oak fence",
            "Oak fence gate", "Oak stairs",
            "Oak slabs", "Petrified oak slabs"
        ], default_value="Oak slabs", size=(30, 1))],
    ]
    dropboxes_r = [

    ]

    layout = [
        [sg.Column(top_text)],
        [sg.HSeparator()],
        [sg.Col(dropboxes_l, dropboxes_r),
        sg.VSeparator()]
    ]
    window = sg.Window("box selector", layout, element_justification="top", finalize=True)

    return window


# creating a new image
def create_color_list(filename,
                isCarpetsUsed,
                isNoSilkTouchUsed,
                iSSilkTouchUsed,
                isPrevNeeded):
    imSize = get_image_size(filename)
    pixelsRGBs = get_image_pixels(filename)
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


# saving a .litematica file
# should create foundation under falling blocks and check for palettes
#def create_litematica():


# main part
window = create_window()
progressBar = window["-GENERATION PROGRESS-"]

isCarpetsUsed = False
isNoSilkTouchUsed = False
iSSilkTouchUsed = False
isMapPrevNeeded = True
isImPrevNeeded = True

pexelsArr = np.array(object="")

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
            if isImPrevNeeded:
                window["-IMAGE INSRT-"].update(filename=filename)
                window["-IMAGE SIZE-"].update(get_image_size(filename))
        except:
            pass
    elif event == "-CARPETS-":
        isCarpetsUsed = values["-CARPETS-"]

    elif event == "-SURVIVAL NO SILK TOUCH-":
        isNoSilkTouchUsed = values["-SURVIVAL NO SILK TOUCH-"]

    elif event == "-SURVIVAL SILK TOUCH-":
        iSSilkTouchUsed = values["-SURVIVAL SILK TOUCH-"]

    elif event == "-IMAGE PREVIEW-":
        isImPrevNeeded = values["-IMAGE PREVIEW-"]

    elif event == "-MAP ART PREVIEW-":
        isMapPrevNeeded = values["-MAP ART PREVIEW-"]

    elif (event == "-GENERATE IMAGE-" and
          filename != "-" and
          (isCarpetsUsed or isNoSilkTouchUsed or iSSilkTouchUsed)):

        pixelsArr = create_color_list(filename, isCarpetsUsed, isNoSilkTouchUsed, iSSilkTouchUsed, isMapPrevNeeded)
    elif (event == "-BLOCK SELECTOR-"):
        blockSelectorWindow = create_selector_window()


    if not isImPrevNeeded:
        window["-IMAGE INSRT-"].update("")
    if not isMapPrevNeeded:
        window["-UPDATE PREVIEW-"].update("")







window.close()

# maps size
# 128x128 pixels

