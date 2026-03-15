# 2️⃣ Guided Implementation:
# Goal: build a simple note-saving program. 

note = "Learn Python engineering."
with open("file_note.txt","w") as file:
    file.write(note)

# read the existing notes: 
with open("file_note.txt","r") as file:
    content = file.read()

# print(content)


# append to the notes
new_notes = "Practice coding daily."
with open("file_note.txt","a") as file:
    file.write("\n"+new_notes)

# read the updated file 

with open("file_note.txt", "r") as file:
    new_content = file.read()

print(new_content)
