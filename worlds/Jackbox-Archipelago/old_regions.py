from BaseClasses import Region
from rule_builder.rules import *

from .items import songs_to_difficulties as songs, items
from .world import DodoReMiWorld


def create_and_connect_regions(world: DodoReMiWorld) -> None:
    # creating regions for each song and difficulty level
    main_menu = Region(world.origin_region_name, world.player, world.multiworld)
    regions = [main_menu]

    for title, difficulties in songs.items():
        regions.append(Region(title, world.player,
                              world.multiworld))  # une région qui sera reliee aux autres (contient Survived, Bronze, Silver, Gold)
        world.create_entrance(main_menu, title, HasAny(f"{region.name} Unlock"), f"Main Menu to {title}")
        for difficulty in difficulties:
            region_name = f"{title} - Difficulty {difficulty}"
            region = Region(region_name, world.player, world.multiworld)
            regions.append(region)

    world.multiworld.regions += regions


def connect_regions(world: DodoReMiWorld) -> None:
    main_menu = world.get_region(world.origin_region_name)
    for title, difficulties in songs.items():
        region = title
        world.create_entrance(main_menu, region, Has(f"{region.name} Unlock"), f"Main Menu to {region.name}")
        world.create_entrance()