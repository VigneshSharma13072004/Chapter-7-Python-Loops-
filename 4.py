# write a program to find the given number is prime or not
n = int(input("Enter the number : "))
for i in range(2,n):
 if (n%i==0):
   print(f"{n} is not prime number ")
 else:
  print(f" {n} is prime number")