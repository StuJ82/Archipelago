from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class DodoReMiWebWorld(WebWorld):
    game="Dodo Re Mi"
    theme="partyTime"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Dodo Re Mi for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["StuJ, Alexis"],
    )

    tutorials=[setup_en]