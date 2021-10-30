#Exercise

# Write a Python program to flatten a shallow list

#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

print("\n Flatenning Here we come:")

list1 =[[2,4,3],[1,5,6], [9], [7,9,0]]
list2=[]

for i in list1:
    for j in i:
        list2.append(j)
        
print(list2)      


