from litemapy import Schematic, Region, BlockState


phys_block = [

],


def create_litematic_file(block_palette, colorIDs, sizeX, sizeZ, imagename):
    region = Region(0, 0, 0, sizeX, 2, sizeZ)
    schematica = region.as_schematic(name=f"{imagename}",
                                     author="MapArtinator 3000",
                                     description="Made by RailGunToaster")
    for x in range(sizeX):
        for z in range(sizeZ):
