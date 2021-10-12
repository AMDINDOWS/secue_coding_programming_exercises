for x in range(5):
    print(x)


print("\n WHILE LOOP")
i=0
while i < 5:
    print(i)
    i += 1

print("\n LIST DATA\n")

lst=["asc3","halo","mad max"," "]
for x in lst:
    print(x)

print("\nappend 2 lists\n ")

j=0
a=[1,2,3,4]
b=[4,5,6,7]
c=[]
while j <len(a):
    c.append(a[j]+b[j])
    j+=1
print(c)    
print("\n\nAppend using zip ")

for x,y in zip(a,b):
    c.append(x+y)
print(c)

print("\n\n list deletion")

print(c.pop(4))

del c[5]

print(f"\ndel keyword:{c}")

print("\nused remove")

print(c.remove(9))


print("\n\nlist to string conversion")
list1=['a','b']
str1=",".join(list1)
print(str1)

list2=[1,2,3,4,]
str2=str(list2).strip('[]')
print(str2)

str3=''.join(str(e) for e in list2)
print (str3)

print("\nThe dictionary system")

dict={"A":"apple",1 : "janet",2.0 :"Piglet"}

print(dict)

print(f"\nThe element 1 : {dict[1]}")

print("\nNOw tuples: :-")

tup= 1,2,"hello",7.9
print(f"Tuple tup :{tup}")