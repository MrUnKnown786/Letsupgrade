print("Delete all occurrences of an element in a list")
list1 = list(map(int, input("Enter list of numbers with space :\n").split()))
a = int(input("Enter number to remove from list : "))
print("Original list is :",list1)
res = [i for i in list1 if i != a]
print("After removing the number :",res)


print("<=======================================================>\n\n")



print("Check whether a string is a pangram")
string = input("Enter String : ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
check = True
for char in alphabet:
        if char not in string.lower():
            check = False

if(check == True):
    print("Entered String is Pangram")
else:
    print("Entered String is not Panagram")
