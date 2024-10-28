import os
from pathlib import Path

def rename_png_files(folder_path):
    """
    Recursively find all PNG files in the given folder and its subfolders.
    If a PNG file doesn't contain '#' in its name, rename it to add '#1'.

    Args:
        folder_path (str): Path to the folder to search in
    """
    # Convert the folder path to a Path object
    folder = Path(folder_path)

    # Recursively find all PNG files
    for png_file in folder.rglob('*.png'):
        # Get the current file name
        file_name = png_file.name

        # If the file name doesn't contain '#'
        if '#' not in file_name:
            # Create the new name by inserting '#1' before the extension
            new_name = f"{png_file.stem}#1{png_file.suffix}"
            new_path = png_file.parent / new_name

            try:
                # Rename the file
                png_file.rename(new_path)
                print(f"Renamed: {file_name} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {file_name}: {str(e)}")

if __name__ == "__main__":
    # Set the path to the 'layers' folder in the current directory
    layers_folder = os.path.join(os.getcwd(), 'layers')

    # Check if the folder exists
    if not os.path.exists(layers_folder):
        print(f"Error: '{layers_folder}' folder not found")
    else:
        rename_png_files(layers_folder)
        print("Processing complete!")