   




'''x = [10, [30, 'baz', 2.718], 'foo']

lst=[]
for i in x:
    if (type(i)==list) :
        lst.extend(i)
    else:
        lst.append(i)
   
#print(lst)


a = lst[2]

print(a[2])

def fun1(name, age): 
    print(name, age)'''

def multi_return(a, b, c):
      if a > 10:
             return b
      elif b> a:
              return c
      else:
             return a,b,c
z = multi_return(12,13,1)
print(z)

input_B = {4:"5",43:"342",72:"7"}



class Thor:

    destination ="Asgard"

    def teleport(self):
        print("\n Lightning Teleport")

    def get_location(self):
        print(f"\n Thr location is : {self.destination}")

#1st obj(class instance), define object 
Mjonir=Thor()

Septre=Thor()

# value changing at object 
Mjonir.destination="Earth"

#class method calls, self para givrn but not req
Mjonir.teleport()

Mjonir.get_location()

Septre.teleport()

Septre.get_location()


aa="5502622159812088949850305428800254892961651752960000000000"
print(len(aa))

