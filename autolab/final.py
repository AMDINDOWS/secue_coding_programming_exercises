"""
#1
Write a function that accepts filters a single lists into 4 sepereate lists.
Assume the input list will contain the following datatypes: ints, floats, str, tuples
You should return 4 sepereate lists each one of which contains _only_ one data type 

You need to return all four lists in a specific order:
[int_list, float_list, str_list, tuple_list]


example input: [1,'hi', 2.0, (1,2,3,'hi'), 1,1,1, 'h', 2.323]
output: ([1,1,1,1], [2.0, 2.323], ['hi', 'h'], [(1,2,3,'hi')])

If a datatype is missing from the input (i.e: no str's are found) you should return an empty list for that type

"""


def sort_and_filter_lists(lst):
    l1=[]
    l2=[]
    l3=[]
    l4=()
    list_final=[]
    for i in (lst):
        if isinstance(i,int):
            a=i
            l1.append(a)
        elif isinstance(i,str):
            a=i
            l2.append(a)
        elif isinstance(i,float):
            a=i
            l3.append(a)
        elif isinstance(i,tuple):
            l4+=i
        else:
            continue
    list_final.append(l1)
    list_final.append(l2)
    list_final.append(l3)
    list_final.append(l4)


    return list_final
print(sort_and_filter_lists([1,'hi', 2.0, (1,2,3,'hi'), 1,1,1, 'h', 2.323]))



            


    


"""
#2
Write a function that "encrypts" a string with the following rules

Every letter is mapped to another letter by moving it forward in the alphabet 'n' spaces. 
It should wrap around the alphabet.
So if n=3, then A-->D, B-->E, C-->F.... X--> B, Z-->C and so on. 
If n=4 then A-->E, B-->F etc.  

Further your function must reverse the string and make all letters lowercase.

Example input:
encrypt('heLLo', n=5)
would return:  'tqqjm'  (as a string)

Your function should work for all positive values of n
(Assume no negative n)

another example input:
encrypt('zoo', n=3)
would return: 'rrc'


"""


def encrypt(string,n):
    lower_string=string.lower()
    print(lower_string)
    newstr=''
    for i in lower_string:
        update = ord(i) + n
        if update>122:
            newupdate = update
            update = 96 + newupdate-122
        newstr = newstr + chr(update)

    newstr.lower()
    newstr=newstr[::-1]
    return newstr

    





"""
#3
Write a function that accepts a dictionary as input.


You job is to sum all the lengths of the keys, and subtract from that the sum of lengths of values
If a datatype has no len, you should skip it.

example input: {'hi' : 10, 'that': [1,2,3]}

output: 3

Your code should work for the following datatypes
* ints
* floats
* str
* lists
* tuples
* sets
* dicts

"""


def manip_dicts(kwargs):
    sum_key=0
    sum_value=0
    for i in kwargs:
        key=len((i))
        value=(kwargs.get(i))
        sum_key = sum_key +key
        if type(value) != (int or float or bool):
            len_value=len(kwargs.get(i))
            sum_value = sum_value + len_value
    difference=sum_key-sum_value
    return difference
        #if a == b:
    
    
print(manip_dicts({'hi' : 10, 'that': [1,2,3]}))

"""
#4
Write a function create_matrix that returns a 2D matrix (nested set of loops).
It should accept two parameters rows, columns.
The matrix values should be in range 1-final number

example input:
create_matrix(4,5)
returns
[[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10,11,12],
 [13,14,15,16],
 [17,18,19,20]]

NOTE: the spaces between the numbers do not matter, 
I added them to make the example clear - your matrix is just a list of lists with ints inside.
"""


def create_matrix():
    
    pass
    

"""
#5

Write a class for to represent tires


instance attributes:
    
    warranty: int 
        ## number of miles before tires expire, default = 1000
    mileage: int  
        ## should default to 0
    expired: bool 
        ## default: false
        ## set to True if and only if the mileage is higher than the warranty
    
methods:
    drive:
        input: float
        returns: "SAFE" or "EXPIRED"
        
        This function should do 3 things
           * increase mileage by the amount drive ( the input)
           * check if the warranty has been reached (mileage is greater or equal), if it has, flip the expired boolean
           * if the tires are expired return "EXPIRED"
           * if the tires are safe, then return "SAFE"
"""


class Tires:
    
    def __init__(self,mileage=0,warranty=1000,expired=False):
        self.warranty=int(warranty)
        self.mileage=int(mileage)
        self.expired=bool(expired)

    def drive(self,input):
        self.input= float(input)
        if self.mileage>=self.warranty:
            self.expired=True
        if self.expired == True:
            return "EXPIRED"
        else:
            self.mileage=self.mileage+self.input        
            return f" New mileage {(self.mileage)} and SAFE" 

