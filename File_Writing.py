# workable file extensions .txt ; .json ; .csv

text_data = "I like some food"
text_connector = " and "
text_data1 = "I dislike some food"

file_path = "Files_Managing/Phrase_of_Mine.txt"

try:
    with open(file=file_path,mode="a") as file:
    #^^ allow to open files, and it will close them at the end
    #         ^^ file or path with a file
    #                        ^^ what exactly we want to do with it
    # "w" - write a file; "x" - write file, that not exist; "r" - read file; "a" - append a file

        file.write("\n" + text_data + text_connector + text_data1)

        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")

