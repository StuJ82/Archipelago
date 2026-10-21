import json
from pathlib import Path
from typing import Any


SONGS_DIRECTORY = Path(__file__).parent


def read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def build_songs():
    songs: dict[str, list[int]] = {}
    song_folders = read_json(SONGS_DIRECTORY / "songs.json")

    for folder_name in song_folders:
        song_directory = SONGS_DIRECTORY / folder_name
        title = read_json(song_directory / "en.json")["TITLE"]
        config = read_json(song_directory / "config.json")

        difficulties: list[int] = []
        for beatmap in config["beatmaps"]:
            difficulty = int(beatmap["difficulty"])
            if difficulty not in difficulties:
                difficulties.append(difficulty)

        songs[title] = difficulties
        songs[title].sort()



    return songs


songs = build_songs()


if __name__ == "__main__":
    print(json.dumps(songs, ensure_ascii=False, indent=2))
