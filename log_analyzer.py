def main():
    file_description = "Server log: "
    file_name = open_file("server_log", file_description)

    log_list = ["ERROR","INFO","INFO","WARNING","ERROR","INFO"]

    for i in log_list:
        append_file(file_name, i)

    duplicates_count = count_duplicates(file_name)
    print_duplicate_count(duplicates_count)
    

def open_file(file_name, file_descriptions):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_descriptions)
    return f"{file_name}.txt"
    
def append_file(file_name, task):
    with open(file_name,"a") as file:
        file.write("\n"+task)

def count_duplicates(file_name):
    duplicates = {}
    with open(file_name, "r") as file:
        content = file.readlines()
    for i in content[1:]:
        i = i.strip()
        try:
            duplicates[i] += 1
        except KeyError:
            duplicates[i] = 1
    return duplicates

def print_duplicate_count(duplicates_count:dict):
    for key in duplicates_count:
        print(f"{key}: {duplicates_count[key]}")

if __name__ == "__main__":
    main()