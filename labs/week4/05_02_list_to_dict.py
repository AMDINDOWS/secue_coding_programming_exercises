# Exercise

# Write a Python program to convert the nested list to a list of dictionaries

# Sample lists: [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]

# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
#                   {'color_name': 'Red', 'color_code': '#FF0000'},
#                   {'color_name': 'Maroon', 'color_code': '#800000'},
#                   {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# use a for-loop

input = [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]

lst1=[]
lst2=[]

for x,i in enumerate(input):
    print(i,x)
    if x == 0:
        lst1= lst1 + i
    if x == 1:
        lst2= lst2 + i

#print(lst1,lst2)

lst3=lst1 + lst2
lst4=[]
for i in lst3:
    
    lst4.append(i)
    lst4.append([i+4])

print(lst4)

d1={}
d2={}

for i in lst1:
        d1['color_name':i]
       

print(d1)
