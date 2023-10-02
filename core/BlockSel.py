import PySimpleGUI as sg


def create_selector_window():

    def name(n):
        size = 10
        spaces = size - len(n) - 2
        return sg.Text(n + " " + " " * spaces,size=(size, 1), justification="l", pad=(0, 0))

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
        # 13 - Quartz (ID 14)
        [name("Quartz"),
         sg.Combo([
             "Diorite", "Diorite slabs",
             "Polished diorite", "Polished diorite slabs",
             "Birch log side",
             "Quartz block", "Quartz slabs"
         ], default_value="Oak slabs", size=(30, 1))],
        # 14 - Podzol (ID 34)
        [name("Podzol"),
         sg.Combo([
             "Podzol", "Spruce planks",
             "Spruce log vertical", "Spruce wood",
             "Spruce stripped log", "Spruce stripped wood",
             "Spruce slabs", "Oak log side",
             "Jungle log side", "Mangrove log side",
             "Mangrove roots", "Muddy mangrove roots"
         ], default_value="Spruce slabs", size=(30, 1))],
        # 15 - Nether (ID 35)
        [name("Nather"),
         sg.Combo([
             "Netherrack", "Nether brick",
             "Nether brick slabs", "Magma block",
             "Red nether bricks", "Red nether bricks slab"
         ], default_value="Netherrack", size=(30, 1))],
        # 16 - Crimson stem (ID 53)
        [name("Crimson stem"),
         sg.Combo([
             "Crimson planks", "Crimson slabs",

         ], default_value="Crimson planks", size=(30, 1))],
        # 17 - Warped nylium
        [name("Warped nylium"),
         sg.Combo([
             "Warped nylium",
             "Oxidized copper", "Oxidized copper slabs"
         ], default_value="Warped nylium slabs", size=(30, 1))],
        # 18 - Warped stem
        [name("Warped stem"),
         sg.Combo([
             "Warped planks", "Warped slabs",
             "Stem", "Stripped stem",
         ], default_value="Warped slabs", size=(30, 1))],
    ]
    dropboxes_r = [
        # 28 - Color red
        [name("Color red"),
         sg.Combo([
             "Red wool", "Red carpet",
             "Red stained glass"
         ])]
    ]

    layout = [
        [sg.Column(top_text)],
        [sg.HSeparator()],
        [sg.Column(dropboxes_l), sg.VSeparator(), sg.Column(dropboxes_r)]
    ]
    window = sg.Window("box selector", layout, element_justification="top", finalize=True)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()
