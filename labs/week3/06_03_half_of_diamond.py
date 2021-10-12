#Exercise

#Write a Python program to construct the following pattern, using a nested for loop.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
 

for i in range(1,6):
    for j in range(i,i+1,1) :
        print("* "*(i))
        j+=1
    i+=1    

for i in range(1,5):
    for j in range(i,i+1,1) :
        print("* "*(5-i))
        j+=1
    i+=1        