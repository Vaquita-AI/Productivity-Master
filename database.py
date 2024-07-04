import os
import time
import heapq
import re
from pathlib import Path
from collections import defaultdict


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

def summarize_text(text, num_sentences=5):
    """
    Summarize the given text by extracting the most relevant sentences.

    :param text: The text to be summarized.
    :param num_sentences: The number of sentences to include in the summary.
    :return: A summary of the text.
    """
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Calculate the frequency of each word
    word_frequencies = defaultdict(int)
    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            word_frequencies[word] += 1

    # Calculate the score for each sentence
    sentence_scores = {}
    for sentence in sentences:
        for word in re.findall(r'\w+', sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]

    # Get the most relevant sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Return the summary
    return ' '.join(summary_sentences)

# Example usage:
text_to_summarize = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits associated with a human mind such as learning and problem-solving. The ideal characteristic of artificial intelligence is its ability to rationalize and take actions that have the best chance of achieving a specific goal. A subset of artificial intelligence is machine learning, which refers to the concept that computer programs can automatically learn from and adapt to new data without being assisted by humans. Deep learning techniques enable this automatic learning through the absorption of huge amounts of unstructured data such as text, images, or video.
"""
print(summarize_text(text_to_summarize))

  


def list_directory_contents(path):
    """
    Lists the files and directories in the given path.

    :param path: The directory path to list contents from.
    """
    try:
        # Get the list of all files and directories
        directory_contents = os.listdir(path)
        
        # Print the names of the files and directories
        for entry in directory_contents:
            print(entry)
            
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except NotADirectoryError:
        print(f"{path} is not a directory.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")
    except OSError as e:
        print(f"An OS error occurred: {e}")
# Example usage:
# list_directory_contents('your_directory_path')


def timestamp_rename_files(directory, extension):
    """
    Searches for files with a given extension within the directory and its subdirectories,
    and renames them by appending a timestamp to their names.

    :param directory: The root directory to search for files.
    :param extension: The file extension to look for.
    """
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                old_path = os.path.join(root, file)
                # Split the file into name and extension
                file_name, file_extension = os.path.splitext(file)
                # Create a new name with the timestamp
                new_name = f"{file_name}_{timestamp}{file_extension}"
                new_path = os.path.join(root, new_name)
                try:
                    # Rename the file
                    os.rename(old_path, new_path)
                    print(f"Renamed '{old_path}' to '{new_path}'")
                except OSError as error:
                    print(f"Error renaming file {old_path}: {error}")

# Example usage:
# Replace 'your_directory_path' with the path of the directory you want to search
# Replace '.txt' with the file extension you are targeting
# timestamp_rename_files('your_directory_path', '.txt')
