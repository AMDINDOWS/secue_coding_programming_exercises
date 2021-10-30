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


pwwd=input("\nPLEASE ENTER PASSWORD REMEMBERING THE NORMS: ")

def pass_check(password):
    
    
    
    flag=0
    p=list(password)
    
    if (6<=len(p)<=16) and (("@" and "#" and "$")in p) and (("@" or "#" or "$")in p):
        flag+=3
        for i in p:
            if (i.islower()):
                flag+=1
            elif (i.isupper()):
                flag+=1
            elif (i.isdigit()):
                flag+=1
        print(flag)
    if (flag>=6):
        return True                    
    else:
        return False
         
    
print(pass_check(pwwd)












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


def even_return(num_dict):
    pass


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


def swap_string(swap_str):
    pass


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


def str_rearrange(in_str):
    pass
