# create a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

input = "Python is smooth "
inst=[]
final=[]
if type(input)==str:
    inst=input.split(' ')

if inst[-1]=='':
    inst.pop(-1)
print(inst)
for i in (inst):
    a = tuple(i)
    final.append(a)

print(final)



  
                
            