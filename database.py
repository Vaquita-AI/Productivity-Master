import os

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
