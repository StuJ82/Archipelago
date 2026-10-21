from items import songs
from pprint import pprint

locations = {}
compteur=0
for title, difficulties in songs.items():
    locations[title] = []
    locations[title].append(title + " - Survived")
    locations[title].append(title + " - Bronze")
    locations[title].append(title + " - Silver")
    locations[title].append(title + " - Gold")

    for difficulty in difficulties:
        locations[title].append(f"{title} - Difficulty: {difficulty} - Survived")
        locations[title].append(f"{title} - Difficulty: {difficulty} - Full Combo")
    compteur+=len(locations[title])
pprint(locations, sort_dicts=False)
print(f"Total number of locations: {compteur}")
