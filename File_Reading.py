
file_path = "Files_Managing/Food_List.txt"

try:
    with open(file_path, "r") as file:
        content = file.read() # for .txt file
        # content = json.load(file) for .json file
        # you can get all at once or specify with [name]
        # content = csv.reader(file) for .csv file, but it returns memory address
        # to be able to interact with the data you need a for loop
        print(content)
except FileNotFoundError:
    print("File was not found")
except PermissionError:
    print("Access to the file had been denied //no permission//")