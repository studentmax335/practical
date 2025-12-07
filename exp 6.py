file = open("students.txt", "w")

n = int(input("Enter number of students: "))
for i in range(n):
    print(f"\nEnter details for student {i+1}:")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    branch = input("Enter branch: ")

    file.write(f"Name: {name}\nRoll No: {roll}\nBranch: {branch}\n\n")

file.close()

file = open("students.txt", "r")
print("\nFile content:\n")
print(file.read())
file.close()
