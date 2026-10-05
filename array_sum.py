# 1. Calculate Array Sum: Write a program to accept N integers
#  into an array and calculate and display the sum of all the elements. 

n = int(input("Enter number of elements: "))

arr = []
total = 0

for i in range(n):
    number = int(input(f"Enter element {i + 1}: "))
    arr.append(number)
    total += number

print("Sum of all elements =", total)

