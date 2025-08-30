import os
#      ^^ stands for operating system and is needed to work with system files

file_path = "Files_Managing/Food_List.txt" # file extension must be correct, same with a file name
#            ^^ this if called relative file path, because it is short and is found inside the same folder/s
# Example of absolute file path: C:/Users/User/Desktop/File.txt

if os.path.exists(file_path):
    #       ^^ one of the literal functions that I know
    print(f"File path {file_path} is found")
    if os.path.isfile(file_path):
        print("This if a file")
    elif os.path.isdir(file_path):
        print("This is a file directory")
    #           ^^ How I understand it could be used for something
else:
    print(f"File path {file_path} is not found")