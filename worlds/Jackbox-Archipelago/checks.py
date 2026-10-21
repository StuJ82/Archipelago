import json
from pathlib import Path
from typing import Any


SONGS_DIRECTORY = Path(__file__).parent


def read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as file:
        return json.load(file)


def build_checks() -> dict[str, list[str]]:
    checks: dict[str, list[str]] = {}
    song_folders = read_json(SONGS_DIRECTORY / "songs.json")

    for folder_name in song_folders:
        song_directory = SONGS_DIRECTORY / folder_name
        title = read_json(song_directory / "en.json")["TITLE"]
        config = read_json(song_directory / "config.json")

        instruments: list[str] = []
        seen_instruments: set[str] = set()
        for beatmap in config["beatmaps"]:
            for instrument in beatmap["instruments"]:
                if instrument not in seen_instruments:
                    instruments.append(instrument)
                    seen_instruments.add(instrument)

        checks[title] = instruments

    return checks


checks = build_checks()


if __name__ == "__main__":
    print(json.dumps(checks, ensure_ascii=False, indent=2))