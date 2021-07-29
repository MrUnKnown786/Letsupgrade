print("Take input for a list and sort it in descending order")
list1 = list(map(int, input("Enter list of numbers with space :\n").split()))
list1.sort(reverse=True)
print(list1)
