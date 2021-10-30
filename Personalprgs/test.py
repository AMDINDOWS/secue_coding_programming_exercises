   




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

for i in input_B:
    print("Key:" + i + "and Element:" + input_B[i])

