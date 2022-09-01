from pathlib import Path
from datetime import datetime
from src.displayable_path import DisplayablePath


OUTPUT_DIR = Path(Path.cwd(), "data", "output")

INCLUDE_DIR = Path(OUTPUT_DIR, "include")
EXCLUDE_DIR = Path(OUTPUT_DIR, "exclude")



def run():
    now = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    success_filename = f"success_{now}.csv"
    issues_filename = f"issues_{now}.csv"

    INCLUDE_DIR.mkdir(exist_ok=True, parents=True)
    EXCLUDE_DIR.mkdir(exist_ok=True, parents=True)

    output_files = [
        Path(INCLUDE_DIR, f"include_{success_filename}"),
        Path(INCLUDE_DIR, f"include_{issues_filename}"),
        Path(EXCLUDE_DIR, f"exclude_{success_filename}"),
        Path(EXCLUDE_DIR, f"exclude_{issues_filename}"),
    ]

    for file in output_files:
        with file.open("w+") as file_handler:
            file_handler.write("Hello world")

    paths = DisplayablePath.make_tree(root=OUTPUT_DIR)
    for path in paths:
        print(path.displayable())


if __name__ == "__main__":
    run()
