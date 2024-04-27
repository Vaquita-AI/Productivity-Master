import os
import time


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
