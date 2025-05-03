import os
import shutil

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", "doc"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Applications": [".exe"],
    "others": [],
}


def organize_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        moved = False
        # check each file category
        for folder, extentions in FILE_TYPES.items():
            if any(file_name.endswith(ext) for ext in extentions):
                folder_path = os.path.join(directory, folder)

                # need to skip id it is not a file
                if not os.path.isfile(file_path):
                    continue

                # create the folder if doesnot exists
                os.makedirs(folder_path, exist_ok=True)

                # move the file to the respective folder
                shutil.move(file_path, os.path.join(folder_path, file_name))
                print("FILES MOVED SCUSSEFULLY")
                moved = True
        # if no match move it to the others folder
        if not moved:
            others_folder = os.path.join(directory, "others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, file_name))
            print("FILES MOVED TO OTHERS FOLDER")


print("Directory path : Just copy paste the directory path you want to Organize")
downloads_path = os.path.expanduser("~")
print(downloads_path)
directory_path = input()

organize_directory(directory_path)
