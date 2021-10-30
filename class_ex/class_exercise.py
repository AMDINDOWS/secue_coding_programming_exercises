"""
#1
Finish the add_me function.
Add each of the numbers in the list and at the end convert result to Integer
## NOT ALLOWED TO USE sum() function!
Input: List
Output: Integer Result

EXAMPLES:

input_A : [1,23,3,4,5]
output_A : 36

input_B : [1,2.0,3,1,2,3]
output_B:  12

input_C : [-6,-5.78, 0]
output_C: -16

input_D: []
output_D : 0
-15 marks
"""

input_C = [-6,-5.78, 0]
def add_me(num_array):
    a=0
    for i in num_array:
        a = a+i
    return int(a)    
    
print(add_me(input_C))    


"""
#2
Finish the reverse_me function.
It should reverse the string and remove the numbers if any

Input: String
Output: String

EXAMPLES:
input_A : "asf3dd23wwr"
output_A : "rwwddfsa"

input_B : "23235"
output_B:  ""

input_C : "255g34s4wc4"
output_C: "cwsg"

"""

input_A = "asf3dd23wwr"



    
def reverse_me(msg):
    lst = list(msg)
    revlst= lst[::-1]
    print(revlst)
    st=''
    for i in revlst:
       if (i.isupper() or i.islower()):
           st+= i
        

        
    return st            

print(reverse_me(input_A))
  


    
