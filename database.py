import os
import time
from pathlib import Path

def batch_rename(directory, pattern, replace_with):
    """
    Renames all files in the given directory that match the pattern to the new given pattern.
    
    :param directory: The path to the directory containing files you want to rename.
    :param pattern: The pattern to match in file names.
    :param replace_with: The string to replace the pattern with.
    """
    for filename in os.listdir(directory):
        if pattern in filename:
            new_filename = filename.replace(pattern, replace_with)
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, new_filename)
            )
            print(f"Renamed '{filename}' to '{new_filename}'")

# Example of usage:
# This will rename all files in the 'sample_directory' that have 'old' in their name to include 'new' instead.
batch_rename('sample_directory', 'old', 'new')

def pomodoro_timer(work_time=25, break_time=5):
    """
    A simple Pomodoro timer that alternates between work time and break time.

    :param work_time: The duration of the work period in minutes.
    :param break_time: The duration of the break period in minutes.
    """

    def start_timer(duration):
        end_time = time.time() + duration * 60
        while time.time() < end_time:
            mins, secs = divmod(end_time - time.time(), 60)
            timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
            print(f"\rTime left: {timer}", end="")
            time.sleep(1)
        print()

    while True:
        print("Work time! Get focused and start working.")
        start_timer(work_time)
        print("Time for a break! Relax for a bit.")
        start_timer(break_time)
        cont = input("Press 'n' if you want to stop the Pomodoro timer, or just hit Enter to continue: ")
        if cont.lower() == 'n':
            break

# Run the Pomodoro timer
pomodoro_timer()



def organize_downloads(download_path):
    """
    Organize files in the download directory into subfolders based on file extensions.

    :param download_path: The path to your downloads directory.
    """
    # Create a mapping of file extensions to directory names
    extension_paths = {
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.gif': 'Images',
        '.pdf': 'Documents',
        '.txt': 'Documents',
        '.docx': 'Documents',
        '.xlsx': 'Spreadsheets',
        '.csv': 'Spreadsheets',
        '.zip': 'Compressed',
        '.tar.gz': 'Compressed',
        '.mp4': 'Videos',
        '.mp3': 'Audio',
        # Add more file types and folders as needed
    }

    # Ensure the download_path is a Path object
    download_path = Path(download_path)

    # Loop through all files in the download directory
    for file in download_path.iterdir():
        if file.is_file():
            # Get the file extension and find the corresponding folder
            extension = file.suffix.lower()
            subfolder_name = extension_paths.get(extension, 'Others')
            folder_path = download_path / subfolder_name

            # Create the folder if it doesn't exist
            folder_path.mkdir(exist_ok=True)

            # Move the file into the corresponding folder
            file.rename(folder_path / file.name)

    print(f"Files in '{download_path}' have been organized.")

# Example usage:
# Replace 'path_to_downloads' with the actual path to your downloads folder
organize_downloads('path_to_downloads')
