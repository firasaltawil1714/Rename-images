from pathlib import Path

script_dir = Path(__file__).parent
target_folder = script_dir / "Images"  


def get_files(folder):

    return [f for f in folder.iterdir() if f.is_file()]

def build_new_name(file, index):

    new_name = f"photo_{index}{file.suffix}"

    return new_name


def rename_all(folder):
    files = []
    for file in folder.iterdir():
        if file.is_file():
            files.append(file)
    return files        


def main():
    if not target_folder.exists():
        print("Target folder does not exist.")
        return

    rename_all(target_folder)


if __name__ == "__main__":
    main()