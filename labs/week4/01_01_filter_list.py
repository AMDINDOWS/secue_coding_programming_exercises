# Exercise

# stage 1
# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3
print(" \nStage 1")
List_1 = ['my', 'name', 'is', 'khan','1']
flag = 0
for i in  List_1:
    if len(i) >= 2:
        flag = flag +1
       
print(f"The answer is : {flag}")    
str=''    
print("\nStage 2 : ")
List_2=['121','xyz','aba','dac','adm','323']
count=0
for i in List_2:
    if len(i)>=2:
        
        str=''.join(i)
       
        if str[0] == str[-1] :
            count+=1

print(f"The second ans is :{count}")            







## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
