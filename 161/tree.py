import os


def count_dirs_and_files(directory="."):
    """Count the amount of of directories and files in passed in "directory" arg.
    Return a tuple of (number_of_directories, number_of_files)
    """
    num_dirs = 0
    num_files = 0
    for _, dirs, files in os.walk(directory):
        num_files += len(files)
        num_dirs += len(dirs)
    return num_dirs, num_files
