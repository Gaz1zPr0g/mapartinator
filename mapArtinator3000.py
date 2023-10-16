import PySimpleGUI as sg
import os.path

import core.ImGen as ig
import core.BlockSel as bs
import core.ImReader as ir
import core.RegGenerator as rg


# Main window GUI

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
    generate_litematica_button = [
        [sg.Button("Generate litematic file", key="-GNERATE LITEMATICA-")]
    ]
    # main layout
    layout = [
        [sg.Column(start_message), sg.Column(generate_image_button), sg.Column(generate_litematica_button)],
        [sg.HSeparator()],

        [sg.Column(file_list),
         sg.VSeparator(),
         sg.Column(inserted_image, expand_y=True),
         sg.Column(preview_image, expand_y=True)],

        [sg.HSeparator()]
    ]

    Window = sg.Window("The mapartinator 3000", layout, finalize=True,
                       element_justification="top", icon="mapArtinator3000.ico")
    return Window


window = create_window()
progressBar = window["-GENERATION PROGRESS-"]


os.mkdir(os.path.join(os.path.dirname(os.path.realpath(__file__)), "litematics"))

blocks = {}
with open("block_selection.txt", "r") as conf:
    for line in conf:
        blocks[f"{line.split()[0]}"] = line[3:-1]


colorIDs = []
imageName = "-"
imSize = [0, 0]
filename = "-"

isCarpetsUsed = False
isNoSilkTouchUsed = False
iSSilkTouchUsed = False
isMapPrevNeeded = True
isImPrevNeeded = True

isImGenerated = False

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
    elif event == "-FILE LIST-":    # File was checked
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            imSize = ir.get_image_size(filename)
            if isImPrevNeeded:
                window["-IMAGE INSRT-"].update(filename=filename)
                window["-IMAGE SIZE-"].update(ir.get_image_size(filename))
                imageName = filename[filename.find('\\')+1:filename.find('.')]
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

        colorIDs = ig.create_color_list(filename, isCarpetsUsed, isNoSilkTouchUsed,
                                         iSSilkTouchUsed, isMapPrevNeeded, window)
        isImGenerated = True
    elif event == "-BLOCK SELECTOR-":
        blocks = bs.create_selector_window()
    elif event == "-GNERATE LITEMATICA-" and isImGenerated:
        imageName += 'c' * isCarpetsUsed + "st" * iSSilkTouchUsed + "nst" * isNoSilkTouchUsed
        rg.create_litematic_file(colorIDs, blocks, imSize[0], imSize[1], imageName)

    if not isImPrevNeeded:
        window["-IMAGE INSRT-"].update("")
    if not isMapPrevNeeded:
        window["-UPDATE PREVIEW-"].update("")


window.close()
