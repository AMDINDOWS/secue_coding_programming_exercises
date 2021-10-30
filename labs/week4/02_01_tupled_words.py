# create a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

input = "Python is smooth "

for i in input:
    if i == " ":
        list1=input.split(" ")
        for j in list1:
            if(j==0):
                tup1=tuple(j)
                print(tup1) 
            elif (j==1):
                tup2=tuple(j)
                print(tup2) 
            elif (j== 2):
                tup3=tuple(j)
                print(tup3)  
                
            