from litemapy import Schematic, Region, BlockState


phys_block = [
    "White candle", "Heavy weighted pressure plate", "lantern", "Soul fire lantern",
    "Sand", "Snow", "White carpet", "Gravel", "Glow lichen",
    "Red carpet", "Orange carpet", "Yellow carpet", "Lime carpet", "Green carpet",
    "Cyan carpet", "Light blue carpet", "Blue carpet", "Purple carpet", "Magenta carpet",
    "Pink carpet", "Light gray carpet", "Gray carpet", "Black carpet", "Brown carpet",
    "Glow lichen", "Light weighted pressure plate"
]


def create_litematic_file(blockIDMap, block_palette, sizeX, sizeZ, imagename):

    region = Region(0, 0, 0, sizeX, 2, sizeZ)
    schematica = region.as_schematic(name=f"{imagename}",
                                     author="MapArtinator 3000",
                                     description="Made by RailGunToaster")
    for x in range(sizeX):
        for z in range(sizeZ):
            blockId = "minecraft:" + str(block_palette[f"{blockIDMap[x][z]}"]).lower().replace(' ', '_')
            block = BlockState(blockId)
            if str(block_palette[f"{blockIDMap[x][z]}"]) in phys_block:
                region.setblock(x, 0, z, BlockState("minecraft:dirt"))
                if str(block_palette[f"{blockIDMap[x][z]}"]) == "Glow lichen":
                    block = BlockState(blockId, properties={"down": "true"})
                    region.setblock(x, 1, z, block)
                else:
                    region.setblock(x, 1, z, block)
            elif str(block_palette[f"{blockIDMap[x][z]}"]) == "Oak leaves":
                region.setblock(x, 0, z, BlockState("minecraft:oak_log"))
                region.setblock(x, 1, z, block)
            else:
                region.setblock(x, 1, z, block)

    schematica.save(f"litematics/{imagename}.litematic")
