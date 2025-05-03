import os


def delete_files_directory(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        if file_name.endswith(".mkv"):
            os.remove(file_path)
            print("Files Deleted Scuessfully")
        else:
            print("Nothing to be deleted")


print("Enter file path you want to delete something of")
downloads_path = os.path.expanduser("~")
print(downloads_path)
directory_path = input()

delete_files_directory(directory_path)
