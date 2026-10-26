from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class TrapChance(Range):
    """
    Percentage chance that any bonus can be replaced by a malus in game.
    """
    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 25

class BirdsNumber(Range):
    """
    Birds are collectibles you need to access the last level.
    Set the number of them in the pool
    """
    display_name = "Birds Number"
    range_start = 50
    range_end = 150
    default = 100

class BirdsWin(Range):
    """
    Birds are collectibles you need to access the last level.
    Set the percentage you need to unlock the last level
    """
    display_name = "Birds Needed To Win"
    range_start = 50
    range_end = 100
    default = 75

class DodoReMiOptions(PerGameCommonOptions):
    trap_chance: TrapChance
    birds:BirdsNumber
    birdsPercent:BirdsWin
