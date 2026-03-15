# 4️⃣ Unguided Challenges
# Challenge 1 — Task Manager (File-Based)
def main():
    file_name = open_file("tasks", file_descriptions="Tasks: ")
    first_task = "Study Python"
    second_task = "Exercise"
    third_task = "Read book"

    add_task(file_name, first_task)
    add_task(file_name, second_task)
    add_task(file_name, third_task)

    view_task(file_name)
    
def open_file(file_name, file_descriptions):
    with open(f"{file_name}.txt","w") as file:
        file.write(file_descriptions)
    return f"{file_name}.txt"

def add_task(file_name, task_name):
    with open(file_name,"a") as file:
        file.write("\n"+task_name)

def view_task(file_name):
    with open(file_name,"r") as file:
        content = file.read()
    print(content)


if __name__== "__main__":
    main()