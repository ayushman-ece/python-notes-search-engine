
from pathlib import Path


def search_file(file_path, keyword):
    path = Path(file_path).expanduser()

    if not path.exists() or not path.is_file():
        raise ValueError("The text file does not exist.")

    if not keyword.strip():
        raise ValueError("Search keyword cannot be empty.")

    matches = []

    with path.open("r", encoding="utf-8", errors="replace") as file:
        for line_number, line in enumerate(file, start=1):
            if keyword.casefold() in line.casefold():
                matches.append({
                    "line_number": line_number,
                    "text": line.rstrip("\r\n")
                })

    return matches
