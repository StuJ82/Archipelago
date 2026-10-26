from worlds.AutoWorld import World
from .regions import create_and_connect_regions
from . import options as dodo_options
from . import items, locations, regions, rules, web_world

class DodoReMiWorld(World):
    """
    DodoRéMi is a rhythm game where players must hit notes in time with the music.
    The game features a variety of songs and difficulty levels, challenging players to improve their timing and accuracy.
    """

    game = "Dodo Re Mi"

    # The WebWorld is a definition class that governs how this world will be displayed on the website.
    web = web_world.DodoReMiWebWorld()  # Placeholder for web world implementation

    # This is how we associate the options defined in our options.py with our world.
    options_dataclass = dodo_options.DodoReMiOptions  # Placeholder for options dataclass
    options: dodo_options.DodoReMiOptions  # Placeholder for options type

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    location_name_to_id = locations.locations_to_id  # Placeholder for location name to ID mapping
    item_name_to_id = items.ITEM_NAME_TO_ID  # Placeholder for item name to ID mapping

    origin_region_name = "Main Menu"  # Starting region for the player

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name:str) -> items.DodoReMiItem:
        return items.create_item_with_correct_classification(self,name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
