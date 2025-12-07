try:

file_name=input("Enter file name: ")

with open(file name,'r') as file:

content=file.read()

print("content", content)

except FileNotFoundError:

try:

print("File not found. Please check the file name and try again.")

num=int(input("Enter a number to divide 100 by: ")) result=100/num print("Result:",result)

except ValueError:

print("Error: Please enter a valid integer.")

except ZeroDivisionError:

print("Error:Denominator cannot be zero.")