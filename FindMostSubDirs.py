import os

def get_most_subdirectories(directory):
    most_subdirectories = []

    # Walk through the directory
    for cur_dir, sub_dirs, files in os.walk(directory):
        # If there are no subdirectories in the current directory
        if not sub_dirs:
            most_subdirectories.append(cur_dir)

    return most_subdirectories

# # Example usage
# directory = "/Users/adrianhwang/Documents/Xiaohui/Duvernay"
# most_subdirs = get_most_subdirectories(directory)
#
# for subdir in most_subdirs:
#     print(subdir)