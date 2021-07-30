'''
Consider a person is represented by Pi, where i is the index of the following list.
A list shows the person to whom person Pi has given the gift.
 
Consider the below example:
gift_presented_to = [2, 1, 5, 3, 4]
 
This list is giving us the following details:
Person P1 has given gift to person P2
Person P2 has given gift to person P1
Person P3 has given gift to person P5
Person P4 has given gift to person P3
Person P5 has given gift to person P4
 
So for the given list, the list of persons from whom they have received the gift would be 
gift_received_from = [2, 1, 4, 5, 3]
 
i.e.
Person P1 has received gift from person P2
Person P2 has received gift from person P1
Person P3 has received gift from person P4
 
 
 
 
Person P4 has received gift from person P5
Person P5 has received gift from person P3
 
Your task:
 
Take input for the gift_presented_to[] list and print its respective gift_received_from[] list.
'''

gift_presented_to = list(map(int, input("Enter input of gift presented to :\n").split()))
n = len(gift_presented_to)
gift_recieved_from = [0]*n
j = 1
for i in gift_presented_to :
    gift_recieved_from[i-1] = j
    j += 1
print(gift_recieved_from)
