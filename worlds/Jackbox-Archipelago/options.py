from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class TrapChance(Range):
    """
    Percentage chance that any bonus can be replaced by a malus in game.
    """
    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 50



class DodoReMiOptions(PerGameCommonOptions):
    trap_chance: TrapChance
