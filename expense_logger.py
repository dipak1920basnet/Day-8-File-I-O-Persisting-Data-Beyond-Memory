# 3️⃣ Partial Guidance Exercise
# Goal: log daily expenses to a file.

expense = "Expenses:"
with open("expense.txt","w") as file:
    file.write(expense)

new_expense = "12"
with open("expense.txt","a") as file:
    file.write("\n"+new_expense)
    file.write("\n"+"5")
    file.write("\n"+"20")

with open("expense.txt","r") as file:
    content = file.read()
# print(content)

with open("expense.txt","r") as file:
    new_content = file.readlines()

total = 0
for i in new_content[1:]:
    total += int(i)

print(content)
print("total:",total)

