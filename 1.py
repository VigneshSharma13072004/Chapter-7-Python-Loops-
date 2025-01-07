# Write a program to print a table of given number using for loop 

n = int(input("Enter the number : "))

for i in range(10):
    result = n*(i+1)
    print(f"{n} * {i+1} = {result}")
