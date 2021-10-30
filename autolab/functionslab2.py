"""
YOU ONLY HAVE 5 ATTEMPTS FOR THIS ASSIGNMENT!
"""


"""
# 1 - pig_latin
7 marks

Write a function that converts a list of words into pig latin

Pig Latin is a language game, where you move the first letter of the word to the end and add "ay."
So "Python" becomes "ythonpay." 
You need to store the pig-latin in a dictionary, with the key as the original word and the value as the pig latin version

Example input:  ['hello', 'i', 'am', 'a' ,'dragon', 'named', 'rasevenous']
output: {'hello':'ellohay', 'i':'iay", 'am':'maay', 'a':'aay', 'dragon':'ragonday', 'named':'amednay', 'rasevenous':'asevenousray'}

"""


input = ['hello', 'i', 'am', 'a' ,'dragon', 'named', 'rasevenous']


def pig_latin(list_):
    emp=[]
    for i in list_:
        a=i[1::]+i[0]+'ay'
        emp.append(a)
    #print(emp)    
    #print(input)
    edict={}
    for i in list_:
        for j in emp:
            a=i[1::]+i[0]+'ay'
            if j == a:
                edict[i]=j
    return edict

print(pig_latin(input))


"""

# 2 - pass_check

10 marks

Write a function `pass_check` to check the validity of a password. 
Return True if valid, False otherwise
  
Validation : 
Only letters (uppers and lowers), digit, and #, $, @ are allowed

At least 1 letter between [a-z] and 1 letter between [A-Z]. 
At least 1 digit from [0-9]. 
At least 1 character from [$#@]. 
Any special characters not in the list of [$#@] are not allowed.
Minimum length 6 characters. 
Maximum length 16 characters. 

Examples:
Input: "amaZZ1_", output: False  (not valid)
Input: "aazzZZ12$$", output : True 
Input: "azZ1$", output: False  (too short)

hint:
you can use the string functions: .isupper(), islower(), isdigit()
to tell if a string character is an upper case letter, lower case letter or digit.


"""


pwwd="123@#Amd"

def pass_check(password):
    
    #and (((("@") or ("#") or ("$"))in p) or ((("@") and ("#") and ("$"))in p)) or ("#" in p)
    
    flag=0
    p=list(password)
    #print(p)
    spl=["@","#","$"]
    notreq='!%^&*()_-+=/*~`<>?,./:";|'
    notspl=list(notreq)
    if ((6<=len(p)<=16) ) :
        flag+=1
        for i in p:
            if (i.islower()):
                flag+=1
            elif (i.isupper()):
                flag+=1
            elif (i.isdigit()):
                flag+=1
            elif i in spl :
                flag+=1
            elif i  in notspl :
                return False        
        #print(flag)
    if (flag>=5):
        return True                    
    else:
        return False
         
    
print(pass_check(pwwd))         
    



"""
# 3 - arrange_me
Marks : 8

Finish the arrange_me function.

You are making a super secret code
Your code will be a string of 0's and 1's. 
You set the 0's and 1's by reading in a nested list of numbers
In the first sub-list, you take all the even indexed numbers.
In the second sub-list you take all the odd indexed numbers.

Then you will read those selected numbers (from the sub-lists) 
and write either 0 if the number was even or 1 if it was odd!

Here is an example input

input_example = [[12, 7], [131, 0]]
### index          0  1      0  1

I take all the even indexed numbers of the first sub-list which 
is : 12 (since it's 0 index)
Then I take all the odd indexed numbers which is : 0 (since it's index is 1)
Then I write a string:
output: "00"
It's 00 because both 12 and 0 are even, so I write 0's.

Input: List of Lists
Outout: String

EXAMPLES:

input_A : [[10,42,12,45],[63,12,7523,65]]
output_A : "0001"

input_B : [[142,22,3], [1,23,3]]
output_B:  "011"

input_C : [[1],[1]]
output_C: "1"

"""


input_A = [[142,22,3], [1,23,3]]


def arrange_me(list_):
    st=''
    for indice,i in enumerate(list_):
        if indice%2==0:
            for j in i:
        
                if int(j)%2==0 and (j in i[0::2]):
                    st+="0"
                if int(j)%2!=0 and (j in i[0::2]):
                    st+="1"    
        if indice%2!=0:
            for j in i:
        
                if int(j)%2==0 and (j in i[1::2]):
                    st+="0"
                if int(j)%2!=0 and (j in i[1::2]):
                    st+="1" 
    return st                    

print(arrange_me(input_A))


"""
# 4 - even_return
Marks: 10

Finish the even_return function.
Return the sum of the even key values
If there are no even keys return 0

Input: Dictionary
Output: Integer Result

EXAMPLES:

input_A : {1:"45",7:"12",34:"765"}
output_A : 765

input_B : {4:"5",43:"342",72:"7"}
output_B:  12

input_C : {1:"23"}
output_C: 0

"""


input_B = {1:"23"}

def even_return(num_dict):
    a=0
    flag=0
    count=0
    for i in num_dict:
        if i%2==0:
            k=int(num_dict[i])
            a = a + k
            flag+=1
        if i%2!=0:
            count+=1
    if flag>0 :
        return a
    if count>0 and flag==0:
        return 0    
print(even_return(input_B))


"""
# 5 - swap_string
Marks: 7

Finish the swap_string function.
Swap the adjacent characters in a string and add space after each pair.
If no swapping partner is there add a space and use the space in the swap.
For the final pair/swap, do not add a space afterwards (the string should always end with a character).

Input: String
Output: String

EXAMPLES:
input_A : "arvcwevw"
output_A : "ra cv ew wv"

input_B : "bsvcdwe"
output_B:  "sb cv wd  e"   ### Note the extra space!

input_C : "bswv325wev"
output_C: "sb vw 23 w5 ve"

"""


input_X ="bsvcdwe"
def swap_string(swap_str):
    if (len(swap_str))%2!=0:
        swap_str = swap_str + " "
    else:
        swap_str=swap_str
    lst=list(swap_str)
    #print(lst)
    le=[]
    lo=[]
    lf=[]
    for indices,i in enumerate(lst):
        
        if indices%2==0:
            le.append(i)
            
        if indices%2!=0:    
            lo.append(i)
            
    #print(lo)
    #print(le)        
    for value,j in enumerate(le):
        for key,g in enumerate(lo):
            if key==value:
                lf.append(g)
                lf.append(j)
                lf.append(' ')
    lf.pop(-1)
    st=''
    for item in lf:
        st+=item  
                  
    return st           

print(swap_string(input_X))


"""

# 6 - str_rearrange
Marks: 8

Finish the str_rearrange function.

Our friend from the neighbouring town has requested a new cipher code.
They gave us the following instructions

They will send us a string which contains a 'key' followed by n adders or substracters.
If a number j is an adder, you add the key j times. If it's a subtractor, you remove the key j times


We asked how to tell if the numbers are adders or subtractors and our friend told us:
"We will send n numbers in the pattern: 'adder, subtractor, adder, subtractor" alternating!

Here is an example

Input: "happy 2 3 4"
We have happy (the key), followed by 2 adder, 3 subtractor, and 4 adder.
So it's a total of 6 adder and 3 subtractor, so it's a net total 3 adder!
output "happyhappyhappy"

If your net total is <0, return a "0" code.

Examples:
Input: String
Outout: String

EXAMPLES:
input_A : "s 5 3"
output_A : "ss"

input_B : "t 3 8 1 4"
output_B:  "0"

input_C : "sde 5 7 4"
output_C: "sdesde"

input_D : "fe 4"
output_D: "fefefefe"

"""


input_Z = "fe 4"
def str_rearrange(in_str):
    lst=in_str.split(" ")
    a = lst.pop(0)
    
    addr=0
    subbr=0
    for indices,i in enumerate(lst):
        
        if indices%2==0:
            addr = addr + int(i)
        if indices%2!=0:
            subbr=subbr+ int(i)
    out=addr-subbr
    if out<0:
        return str(0)
    if out>=0:
        return a*out
    
print(str_rearrange(input_Z))
