"""
#1
Write a function that accepts an infinite amount of positional arguments
Your function should take all the arguments and place them into a list
return the list

example input:  infinite_args(1,2,3,4,5)
example output: [1,2,3,4,5]

"""


def infinite_args(*args):
    lst=[]
    for i in args:
        lst.append(i)
        
    return lst    

print(infinite_args(1,2,3,4,5))


"""
#2
Write a function that accepts an infinite amount of keyword arguments
Your funciton should take all the keyword arguments and place them into a list of tuples
Each tuple should be a (keyword:value).

Return: a list of tuples(key:value)

example input:  ('hi' = 1, 'bye'=2, 'there_there' = 3)
example output: [('hi', 1), ('bye', 2), ('there_there', 3)]

"""


def infinite_kwargs(**kwargs):
    lst=[]
    lst2=[]
    #lstfinal=[]
    for key,value in kwargs.items():
       lst.append(key)
       lst2.append(value)
       tup1=tuple(lst)
       tup2=tuple(lst2)
       a=zip(tup1,tup2)
       #print(tup)
       
    return list(a)
       
print(infinite_kwargs(hi = 1, bye=2, there_there = 3))
"""
#3
Finish the function quotes_n_things that takes as input a dictionary with the following keys / value pairs

sample_dict = { 'name' : 'Gilad Gressel',
                'job_occupation': 'professor',
                'country' : 'Israel',
                'quote'   : 'You should strive to understand something, not just know it.'
                }

Your function should parse the dictionary and return a string in the following format

--------
"[Quote]", was delivered by Mr. [last_name], who is a [job_occupation] from [country]
--------

Note: the []'s are shown only to indicate the key's to use. Your final string should not include []'s. 
Your final string _should_ include double quotation marks "" around the [quote] key.

the sample output would be for the sample dict would be.
-------------
"You should strive to understand something, not just know it.", was delivered by Mr. Gressel, who is a professor from Israel
-------------
"""


def quotes_n_things(**kwargs):
    lst=[]
    lst2=[]
    for key,value in kwargs.items():
        lst.append(key)
        lst2.append(value)
    return f'"{lst2[-1]}.", was delivered by Mr. {lst2[0]}, who is a {lst2[1]} from {lst2[2]}'    


        
        
        
print(quotes_n_things(name="Gilad",job_occupation='professor',country='israel',quote='this is it'))
"""
#4
complete find_and_sum_lits, a function that 
sum all integers in a list, including any integer nested in another object

example input: [1,2,3]
output: 6

example input: [2,2,2, ['hello, 2], 'hi', {a:2}, {4,6}, 10, (5, 5)]
output: 40
"""

#input = [2,2,2, ['hello, 2], 'hi', {a:2}, {4,6}, 10, (5, 5)]
def find_and_sum_ints(lst):
    #sum = 0
    final_list=[]

    
    while True:
        for i in lst:
            if isinstance(i,(set,tuple,list)):
                final_list += i
            elif isinstance(i, dict):
                for k,v in i.items():
                    final_list.extend([k,v])
            else:
                final_list.append(i)        
        #check for full flat
        for i in final_list:
            if isinstance(i,(list,tuple,set,dict)):
                lst=final_list
                final_list=[]
                break
        else: #not break (for with else)
            break            
        pass
print(find_and_sum_ints([2,2,2, ['hello', 2], 'hi', {"a":2}, {4,6}, 10, (5, 5)]))
"""
#5

Write a class for a single room apartment. Use a class variable to keep track of how many apartments are for sale.

class attributes:
     num_apartments_for_sale

instance attributes:
     length : float
     width: float
     height: float
     bathroom: boolean
     num_windows : int

methods:
    square_foot : returns the square footage of the apartment (L x W x H)
    price: returns the price which is calculated by: (square_foot*10) + (Bathroom * 100) + (num_windows * 50)

When you print an instance of the Apartment class it should display the following string format

----------
The apartment has [square feet] and costs [price]
----------

"""


class Apartment:
    
    num_apartments_for_sale=0

    def __init__(self,lenght,width,height,bathroom,num_windows):
        self.lenght = float(lenght)
        self.width = float(width)
        self.height= float(height)
        self.bathroom= int(bathroom)
        self.num_windows= int(num_windows)
        Apartment.num_apartments_for_sale+=1

    def square_foot(self):
        return (self.lenght)*(self.width)*(self.height)

    def price(self):
        return (self.square_foot() *10) + (self.bathroom * 100) + (self.num_windows *50)       
    def __str__(self):
        return f"The apartment has {self.square_foot()} and costs {self.price()}"

apt1=Apartment(11.5,6,10,6,8)

print(apt1)
 

"""
Examine the follow Weapon class
You will need to use it in problem #5
"""


class Weapon:
    def __init__(self, name, str_req, attack_value):
        self.name = name
        self.str_req = str_req
        self.attack_value = attack_value


"""
#6
Finish the warrior class below

attributes:
    strength : int
    health   : int
    weapon: Weapon
    equipment_max_size : int

Methods:
    equip_weapon(weapon): --> None
        equips a weapon (from the weapon class) if the warrior has the required strength
        this method should update the weapon attribute to be the new current weapon
        returns nothing

    attack(): --> float
        returns damage done, which is equal to warriors strength + weapon attack value
        

When an instance of the Warrior class is printed to console it should display one of the following messages:

when the warrior has a weapon:
    
    -----------
    The warrior has [health] health points, [strength] strength, and has a [weapon] equipped
    -----------

otherwise:
    
    ------------
    The warrior has [health] health points, [strength] strength, and has nothing equipped
    ------------

The []'s are there only to indicate what stat should be displayed NOT as part of the actual string.

"""


class Warrior:
    def __init__(self,strength,health,weapon,equipment_max_size):
        self.strength=int(strength)
        self.health=int(health)
        self.weapon=Weapon
        self.equipment_max_size= int(equipment_max_size)

    def equip_weapon(self,weapon):
        if self.strength>=Weapon.str_req:
            self.weapon=weapon

    def attack(self):       
        if self.weapon:
            return self.weapon.attack_value + self.strength
        else:
            return self.strength    
    def __str__(self):
        if self.weapon:
            return f"The warrior has {self.health} health points, {self.strength} strength, and has a {self.weapon} equipped"
        else:
            return f"The warrior has {self.health} health points, {self.strength} strength, and has nothing equipped"    