import uuid
from pathlib import Path
from typing import Iterable

CURRENT_FILE = Path(__file__)
CURRENT_DIR = CURRENT_FILE.parent


def generate_new_name(file: Path):
    return str(uuid.uuid4())


def rename_all_files_in_dir(
    dir_path: Path = CURRENT_DIR,
    protected_files: Iterable[Path] = (CURRENT_FILE,),
):
    for maybe_file in dir_path.iterdir():
        if maybe_file in protected_files:
            continue
        if maybe_file.is_file():
            maybe_file.rename(Path(dir_path) / generate_new_name(maybe_file))
        elif maybe_file.is_dir():
            rename_all_files_in_dir(maybe_file, protected_files)


if __name__ == "__main__":
    rename_all_files_in_dir()
