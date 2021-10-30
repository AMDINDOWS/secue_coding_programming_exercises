"""
#1
Finish the hello_world function.
It should return exactly "Hello World!"  (without the "" quotes)
-5 marks
"""


def hello_world():
    return "Hello World!"

print(hello_world())

"""
#2
Finish the "list_flat" function below.

It should take as input 
   Input : List of lists

It should give as
   Output: flattened list

EXAMPLES:

input_A : [[1,2,3],[1,23,3],[4,5]]
output_A : [1,2,3,1,23,3,4,5]

input_B : [1,2,3, [1,2,3]]
output_B:  [1,2,3, 1,2,3]

input_C : [[1,2,3],[1,23,3],[4,5], 101,10]
output_C:  [1,2,3,1,23,3,4,5,101,10]

input_D: [1,2,3]
output_D : [1,2,3]
-15 marks
"""

def list_flat(list_):
   lst=[]
   for i in list_:
         if (type(i)==list) :
               lst.extend(i)
         else:
               lst.append(i)
   return lst 

input_C = [[1,2,3],[1,23,3],[4,5], 101,10]
print(list_flat(input_C))


input_D = [1,2,3]
print(list_flat(input_D))

input_A = [[1,2,3],[1,23,3],[4,5]]
print(list_flat(input_A))


input_B = [1,2,3, [1,2,3]]
print(list_flat(input_B))