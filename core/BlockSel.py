import PySimpleGUI as sg


def create_selector_window():

    def name(n):
        size = 15
        spaces = size - len(n) - 2
        return sg.Text(n + " " + " " * spaces,size=(size, 1), justification="l", pad=(0, 0))

    # creating block palette by importing config file
    blocks = {"0": "Air"}
    with open("block_selection.txt", "r") as conf:
        for line in conf:
            blocks[f"{line.split()[0]}"] = line[3:-1]

    sg.theme("dark grey 11")
    top_text = [
        [sg.Text("Select which blocks will match next colors")],
    ]

    dropboxes_l1 = [
        # 1 - Grass
        [sg.Text("█", text_color="#7fb238"),
         name("Grass"),
         sg.Combo([
                "Grass block",
                "Slime block"
         ], default_value="Grass block", size=(30, 1), k="1")],

        # 2 - Sand
        [sg.Text("█", text_color="#f7e9a3"),
         name("Sand"),
         sg.Combo([
                "Sand", "Birch planks", "Birch log vertical",
                "Birch stripped log", "Birch wood",
                "Birch stripped wood", "Birch sign",
                "Birch pressure plate", "Birch Trapdoor",
                "Birch stairs", "Birch slab", "Birch fence",
                "Birch fence gate", "Birch door",
                "Sandstone", "Sandstone stairs", "Sandstone slab",
                "Sandstone fence", "Chiseled sandstone", "Smooth sandstone",
                "Smooth sandstone stairs", "Smooth sandstone slab",
                "Cut sandstone", "Cut sandstone slab"
         ], default_value="Birch slab", size=(30, 1), k="2")],

        # 3 - Wool  (ID 3)
        [sg.Text("█", text_color="#c7c7c7"),
         name("Wool"),
         sg.Combo([
                "Cobweb",
                "Mushroom stem",
                "White candle"
         ], default_value="White candle", size=(30, 1), k="3")],

        # 4 - Fire  (ID 4)
        [sg.Text("█", text_color="#ff0000"),
         name("Fire"),
         sg.Combo([
             "Lava", "TNT",
             "Fire", "Redstone block"
         ], default_value="Redstone block", size=(30, 1), k="4")],

        # 5 - Ice   (ID 5)
        [sg.Text("█", text_color="#a0a0ff"),
         name("Ice"),
         sg.Combo([
             "Ice", "Frosted ice",
             "Packed ice", "Blue ice"
         ], default_value="Packed ice", size=(30, 1), k="5")],

        # 6 - Metal (ID 6)
        [sg.Text("█", text_color="#a7a7a7"),
         name("Metal"),
         sg.Combo([
             "Block of iron", "Iron door",
             "Brewing stand", "Heavy weight pressure plate",
             "Iron trapdoor", "lantern",
             "Anvil", "Grindstone",
             "Soul fire lantern", "Lodestone"
         ], default_value="Heavy weight pressure plate", size=(30, 1), k="6")],

        # 7 - Plant (ID 7)
        [sg.Text("█", text_color="#007c00"),
         name("Plant"),
         sg.Combo([
             "Oak leaves", "Spruce leaves",
             "Birch leaves", "Jungle leaves",
             "Acacia leaves", "Dark oak leaves",
             "Mangrove leaves", "Azalea",
             "Flowering azalea", "Block of bamboo"
         ], default_value="Oak leaves", size=(30, 1), k="7")],

        # 8 - Snow  (ID 8)
        [sg.Text("█", text_color="#ffffff"),
         name("Snow"),
         sg.Combo([
             "Snow", "Snow block",
             "Wool", "Stained glass",
             "White carpet", "White shulcker box",
             "Glazed terracotta", "White concrete",
             "White concrete powder", "Powder snow"
         ], default_value="Wool", size=(30, 1), k="8")],

        # 9 - Clay (only option) (ID 9)
        # 10 - Dirt  (ID 10)
        [sg.Text("█", text_color="#976d4d"),
         name("Dirt"),
         sg.Combo([
             "Dirt", "Coarse dirt",
             "Dirt path", "Rooted dirt",
             "Granite",
             "Granite stairs", "Granite slab",
             "Granite wall", "Polished granite",
             "Polished granite stairs", "Polished granite slab",
             "Jungle planks", "Jungle log vertical",
             "Jungle stripped log", "Jungle wood",
             "Jungle stripped wood", "Jungle sign",
             "Jungle pressure plate", "Jungle trapdoor",
             "Jungle stairs", "Jungle slab",
             "Jungle fence", "Jungle fence gate",
             "Jungle door", "Jukebox",
             "Brown mushroom block", "Packed mud"
         ], default_value="Jungle slab", size=(30, 1), k="10")],

        # 11 - Stone (ID 11)
        [sg.Text("█", text_color="#707070"),
         name("Stone"),
         sg.Combo([
             "Stone", "Stone stairs", "Stone slab",
             "Andesite", "Andesite stairs",
             "Andesite wall", "Polished andesite",
             "Polished andesite stairs", "Polished andesite slab",
             "Cobblestone", "Cobblestone stairs",
             "Cobblestone slab", "Cobblestone wall",
             "Gravel", "Smooth stone", "Smooth stone slab",
             "Stone pressure plate",
             "Stone bricks", "Stone brick stairs",
             "Stone brick slab", "Stone brick wall",
             "Mossy stone bricks", "Mossy stone brick stairs",
             "Mossy stone brick slab",
             "Mossy cobblestone", "Mossy cobblestone stairs",
             "Mossy cobblestone slab", "Mossy cobblestone wall",
             "Gold ore", "Iron ore", "Coal ore",
             "Diamond ore", "Redstone ore",
             "Emerald ore", "Copper ore",
             "Lapis lazuli ore",
             "Furnace", "Smoker", "Blast Furnace",
             "Dispenser", "Observer", "Piston",
             "Sticky piston", "Hopper", "Ender chest",
         ], default_value="Cobblestone slab", size=(30, 1), k="11")],

        # 12 - Water (ID 12)
        [sg.Text("█", text_color="#4040ff"),
         name("Water"),
         sg.Combo([
             "Kelp", "Seagrass",
             "Water", "Bubble Column",
             "Waterlogged leaves"
         ], default_value="Water", size=(30, 1), k="12")],

        # 13 - Wood (ID 13)
        [sg.Text("█", text_color="#8f7748"),
         name("Wood"),
         sg.Combo([
            "Oak planks", "Oak log vertical",
            "Oak stripped log", "Oak wood",
            "Oak stripped wood", "Oak sign",
            "Oak door", "Oak pressure plate",
            "Oak trapdoor", "Oak fence",
            "Oak fence gate", "Oak stairs",
            "Oak slab", "Petrified oak slab"
         ], default_value="Oak slab", size=(30, 1), k="13")],

        # 14 - Quartz (ID 14)
        [sg.Text("█", text_color="#fffff5"),
         name("Quartz"),
         sg.Combo([
             "Diorite", "Diorite slab",
             "Polished diorite", "Polished diorite slab",
             "Birch log side",
             "Quartz block", "Quartz slab"
         ], default_value="Diorite slab", size=(30, 1), k="14")],
    ]
    dropboxes_l2 = [
        # 34 - Podzol (ID 34)
        [sg.Text("█", text_color="#815631"),
         name("Podzol"),
         sg.Combo([
             "Podzol", "Spruce planks",
             "Spruce log vertical", "Spruce wood",
             "Spruce stripped log", "Spruce stripped wood",
             "Spruce slab", "Oak log side",
             "Jungle log side", "Mangrove log side",
             "Mangrove roots", "Muddy mangrove roots"
         ], default_value="Spruce slab", size=(30, 1), k="34")],

        # 35 - Nether (ID 35)
        [sg.Text("█", text_color="#700200"),
         name("Nether"),
         sg.Combo([
             "Netherrack", "Nether brick",
             "Nether brick slab", "Magma block",
             "Red nether bricks", "Red nether bricks slab"
         ], default_value="Netherrack", size=(30, 1), k="35")],

        # 53 - Crimson stem (ID 53)
        [sg.Text("█", text_color="#943f61"),
         name("Crimson stem"),
         sg.Combo([
             "Crimson planks", "Crimson slab",
         ], default_value="Crimson slab", size=(30, 1), k="53")],

        # 55 - Warped nylium
        [sg.Text("█", text_color="#167e86"),
         name("Warped nylium"),
         sg.Combo([
             "Warped nylium",
             "Oxidized copper", "Oxidized cut copper slab",
             "Waxed oxidized copper", "Waxed oxidized cut copper slab"
         ], default_value="Warped nylium slab", size=(30, 1), k="55")],

        # 56 - Warped stem
        [sg.Text("█", text_color="#3a8e8c"),
         name("Warped stem"),
         sg.Combo([
             "Warped planks", "Warped slab",
             "Stem", "Stripped stem",
             "Waxed weathered copper", "Waxed weathered cut copper slab"
         ], default_value="Warped slab", size=(30, 1), k="56")],

        # 30 - Gold
        [sg.Text("█", text_color="#faee4d"),
         name("Gold"),
         sg.Combo([
             "Gold block", "Light weighted pressure plate"
         ], default_value="Light weighted pressure plate", size=(30, 1), k="30")],

        # 36 - White terracotta
        [sg.Text("█", text_color="#d1b1a1"),
         name("White terracotta"),
         sg.Combo([
             "White terracotta", "Calcite"
         ], default_value="White terracotta", size=(30, 1), k="36")],

        # 43 - Gray terracotta
        [sg.Text("█", text_color="#392923"),
         name("Gray terracotta"),
         sg.Combo([
             "Gray terracotta", "Tuff"
         ], default_value="Gray terracotta", size=(30, 1), k="43")],

        # 44 - Light grey terracotta
        [sg.Text("█", text_color="#876b62"),
         name("Light gray terracotta"),
         sg.Combo([
             "Light gray terracotta", "Mud brick slab",
             "Waxed exposed copper", "Waxed exposed cut copper slab"
         ], default_value="Light gray terracotta", size=(30, 1), k="44")],

        # 45 - Cyan terracotta
        [sg.Text("█", text_color="#575c5c"),
         name("Cyan terracotta"),
         sg.Combo([
             "Cyan terracotta", "Mud"
         ], default_value="Cyan terracotta", size=(30, 1), k="45")],

        # 48 - Brown terracotta
        [sg.Text("█", text_color="#4c3223"),
         name("Brown terracotta"),
         sg.Combo([
             "Brown terracotta", "Dripstone block"
         ], default_value="Brown terracotta", size=(30, 1), k="48")],

        # 59 - Deepslate
        [sg.Text("█", text_color="#646464"),
         name("Deepslate"),
         sg.Combo([
             "Cobbled deepslate", "Cobbled deepslate slab",
             "Deepslate", "Polished deepslate", "Chiseled deepslate",
             "Deepslate bricks", "Deepslate brick slab",
             "Deepslate tiles", "Deepslates tile slab"
                                "Deepslate slab", "Dripstone block"
         ], default_value="Cobbled deepslate slab", size=(30, 1), k="59")],

        # 61 - Glow lichen
        [sg.Text("█", text_color="#7fa796"),
         name("Glow lichen"),
         sg.Combo([
             "Glow lichen", "Verdant froglight"
         ], default_value="Glow lichen", size=(30, 1), k="61")]
    ]
    dropboxes_r = [
        # 28 - Color red
        [sg.Text("█", text_color="#993333"),
         name("Red"),
         sg.Combo([
             "Red wool", "Red carpet",
             "Red glass", "Red concrete",
             "Red glazed terracotta"
         ], default_value="Red carpet", size=(30, 1), k="28")],

        # 15 - Orange color
        [sg.Text("█", text_color="#d87f33"),
         name("Orange"),
         sg.Combo([
             "Acacia planks", "Acacia slab",
             "Orange wool", "Orange carpet",
             "Orange concrete", "Orange glazed terracotta",
             "Orange glass", "Red sand"
         ], default_value="Orange carpet", size=(30, 1), k="15")],

        # 18 - Yellow color
        [sg.Text("█", text_color="#e5e533"),
         name("Yellow"),
         sg.Combo([
             "Yellow wool", "Yellow carpet",
             "Yellow concrete", "Yellow glazed terracotta",
             "Yellow glass", "Hay bale"
         ], default_value="Yellow carpet", size=(30, 1), k="18")],

        # 19 - Light green
        [sg.Text("█", text_color="#7fcc19"),
         name("Lime"),
         sg.Combo([
             "Lime wool", "Lime carpet",
             "Lime concrete", "Lime glazed terracotta",
             "Lime glass", "Melon"
         ], default_value="Lime carpet", size=(30, 1), k="19")],

        # 27 - Green
        [sg.Text("█", text_color="#667f33"),
         name("Green"),
         sg.Combo([
             "Green wool", "Green carpet",
             "Green concrete", "Green glazed terracotta",
             "Green glass", "Moss block", "Moss carpet",
         ], default_value="Green carpet", size=(30, 1), k="27")],

        # 23 - Cyan
        [sg.Text("█", text_color="#4c7f99"),
         name("Cyan"),
         sg.Combo([
             "Cyan wool", "Cyan carpet",
             "Cyan concrete", "Cyan glazed terracotta",
             "Cyan glass"
         ], default_value="Cyan carpet", size=(30, 1), k="23")],

        # 17 - Light blue
        [sg.Text("█", text_color="#6699d8"),
         name("Light blue"),
         sg.Combo([
             "Light blue wool", "Light blue carpet",
             "Light blue concrete", "Light blue glazed terracotta",
             "Light blue glass"
         ], default_value="Light blue carpet", size=(30, 1), k="17")],

        # 25 - Blue
        [sg.Text("█", text_color="#334cb2"),
         name("Blue"),
         sg.Combo([
             "Blue wool", "Blue carpet",
             "Blue concrete", "Blue glazed terracotta",
             "Blue glass"
         ], default_value="Blue carpet", size=(30, 1), k="25")],

        # 24 - Purple
        [sg.Text("█", text_color="#7f3fb2"),
         name("Purple"),
         sg.Combo([
             "Purple wool", "Purple carpet",
             "Purple concrete", "Purple glazed terracotta",
             "Purple glass"
         ], default_value="Purple carpet", size=(30, 1), k="24")],

        # 16 - Magenta
        [sg.Text("█", text_color="#b24cd8"),
         name("Magenta"),
         sg.Combo([
             "Magenta wool", "Magenta carpet",
             "Magenta concrete", "Magenta glazed terracotta",
             "Magenta glass", "Purpur slab", "Purpur block",
             "Purpur pillar"
         ], default_value="Magenta carpet", size=(30, 1), k="16")],

        # 20 - Pink
        [sg.Text("█", text_color="#f27fa5"),
         name("Pink"),
         sg.Combo([
             "Pink wool", "Pink carpet",
             "Pink concrete", "Pink glazed terracotta",
             "Pink glass"
         ], default_value="Pink carpet", size=(30, 1), k="20")],

        # 22 - Light gray
        [sg.Text("█", text_color="#999999"),
         name("Light gray"),
         sg.Combo([
             "Light gray wool", "Light gray carpet",
             "Light gray concrete", "Light gray glazed terracotta",
             "Light gray glass"
         ], default_value="Light gray carpet", size=(30, 1), k="22")],

        # 21 - Grey
        [sg.Text("█", text_color="#4c4c4c"),
         name("Grey"),
         sg.Combo([
             "Grey wool", "Grey carpet",
             "Grey concrete", "Grey glazed terracotta",
             "Grey glass"
         ], default_value="Grey carpet", size=(30, 1), k="21")],

        # 29 - Black
        [sg.Text("█", text_color="#191919"),
         name("Black"),
         sg.Combo([
             "Black wool", "Black carpet",
             "Black concrete", "Black glazed terracotta",
             "Black glass"
         ], default_value="Black carpet", size=(30, 1), k="29")],

        # 26 - Brown
        [sg.Text("█", text_color="#664c33"),
         name("Brown"),
         sg.Combo([
             "Brown wool", "Brown carpet",
             "Brown concrete", "Brown glazed terracotta",
             "Brown glass"
         ], default_value="Brown carpet", size=(30, 1), k="26")],
    ]

    layout = [
        [sg.Column(top_text)],
        [sg.HSeparator()],
        [sg.Column(dropboxes_l1), sg.Column(dropboxes_l2), sg.VSeparator(), sg.Column(dropboxes_r)]
    ]
    window = sg.Window("BlockSelector", layout, element_justification="top", finalize=True)
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif int(event) in range(1, 62):
            blocks[event] = values[event]

    window.close()
    return blocks
