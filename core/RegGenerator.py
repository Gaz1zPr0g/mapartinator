from litemapy import Schematic, Region, BlockState


phys_block = [
    "White candle", "Heavy weight pressure plate", "lantern", "Soul fire lantern",
    "Sand", "Snow", "White carpet", "White concrete powder", "Gravel", "Glow lichen",
    "Red carpet", "Orange carpet", "Yellow carpet", "Lime carpet", "Green carpet",
    "Cyan carpet", "Light blue carpet", "Blue carpet", "Purple carpet", "Magenta carpet",
    "Pink carpet", "Light gray carpet", "Gray carpet", "Black carpet", "Brown carpet"
],


def create_litematic_file(blockIDMap, block_palette, sizeX, sizeZ, imagename):

    region = Region(0, 0, 0, sizeX, 2, sizeZ)
    schematica = region.as_schematic(name=f"{imagename}",
                                     author="MapArtinator 3000",
                                     description="Made by RailGunToaster")
    for x in range(sizeX):
        for z in range(sizeZ):
            blockId = "minecraft:" + str(block_palette[f"{blockIDMap[x][z]}"]).lower().replace(' ', '_')
            block = BlockState(blockId)
            if block_palette[f"{blockIDMap[x][z]}"] in phys_block:
                region.setblock(x, 0, z, "minecraft:dirt")
                region.setblock(x, 1, z, block)
            else:
                region.setblock(x, 1, z, block)

    schematica.save(f"{imagename}.litematic")
