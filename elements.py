# 2. Find the smallest and Largest Element: Write a program to accept N integers
#  into an array and find and display the largest element, second largest element,
#  smallest element, second smallest element present in the array. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    number = int(input(f"Enter element {i + 1}: "))
    arr.append(number)

arr.sort()

print("Smallest element =", arr[0])
print("Second smallest element =", arr[1])
print("Largest element =", arr[-1])
print("Second largest element =", arr[-2])