print("Take input for a list and sort it in descending order")
list1 = list(map(int, input("Enter Numbers with Space : \n").split()))
list1.sort(reverse=True)
print(list1)
