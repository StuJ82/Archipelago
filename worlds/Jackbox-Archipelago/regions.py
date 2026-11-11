from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

if TYPE_CHECKING:
    from .world import DodoReMiWorld


def get_difficulty_unlock_items(
    song: str,
    difficulty: int,
    song_unlock_items: list[dict[str, int]],
) -> tuple[str, ...]:
    """Retourne les items nécessaires pour débloquer cette difficulté.

    Certaines difficultés demandent plusieurs items numérotés (« Part 1/2 »,
    « Part 2/2 ») : ils sont tous requis. Une difficulté sans item associé
    est considérée comme accessible sans déblocage.
    """
    unlock_name = f"{song} - Difficulty {difficulty} Unlock"
    return tuple(
        item_name
        for song_items in song_unlock_items
        for item_name in song_items
        if item_name == unlock_name or item_name.startswith(f"{unlock_name}: Part ")
    )


def create_and_connect_regions(world: DodoReMiWorld) -> None:
    # L'import différé évite le cycle world.py -> regions.py -> items.py -> world.py.
    from .items import items as song_unlock_items
    from .items import songs_to_difficulties

    # Créer d'abord toutes les régions; les connexions sont ajoutées ensuite.
    main_menu = Region(world.origin_region_name, world.player, world.multiworld)
    regions = [main_menu]
    song_regions = {}
    difficulty_regions = {}

    for song, difficulties in songs_to_difficulties.items():
        song_region = Region(song, world.player, world.multiworld)
        regions.append(song_region)
        song_regions[song] = song_region

        for difficulty in difficulties:
            difficulty_region = Region(
                f"{song} - Difficulty {difficulty}",
                world.player,
                world.multiworld,
            )
            regions.append(difficulty_region)
            difficulty_regions[song, difficulty] = difficulty_region

    world.multiworld.regions += regions

    # Le menu ouvre la région d'une chanson dès qu'au moins une de ses
    # difficultés est débloquée. Pour une difficulté à plusieurs parties,
    # toutes les parties correspondantes doivent être possédées.
    for song, difficulties in songs_to_difficulties.items():
        song_region = song_regions[song]
        unlock_sets = tuple(
            get_difficulty_unlock_items(song, difficulty, song_unlock_items)
            for difficulty in difficulties
        )
        main_menu.connect(
            song_region,
            f"Main Menu to {song}",
            # La valeur par défaut capture les items de cette chanson, plutôt
            # que ceux de la dernière chanson parcourue par la boucle.
            lambda state, required_unlock_sets=unlock_sets: any(
                not group_items
                or all(state.has(item_name, world.player) for item_name in group_items)
                for group_items in required_unlock_sets
            ),
        )

        for difficulty in difficulties:
            difficulty_unlock_items = get_difficulty_unlock_items(
                song,
                difficulty,
                song_unlock_items,
            )
            if difficulty_unlock_items:
                # L'accès à la région de difficulté exige tous ses items de
                # déblocage (par exemple les deux parties d'une difficulté 3).
                song_region.connect(
                    difficulty_regions[song, difficulty],
                    f"{song} to Difficulty {difficulty}",
                    # Capturer cette difficulté évite le problème de fermeture
                    # tardive des variables de boucle.
                    lambda state, required_unlock_items=difficulty_unlock_items: all(
                        state.has(item_name, world.player)
                        for item_name in required_unlock_items
                    ),
                )
            else:
                # Cas des chansons/difficultés sans item de déblocage.
                song_region.connect(
                    difficulty_regions[song, difficulty],
                    f"{song} to Difficulty {difficulty}",
                )
