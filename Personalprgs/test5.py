l=[0,1,23,5,6,7]
x=6

for i in l:
    a=x-i
    if a>0:
        for b in l:
            if a+b==x:
                print(a,b)
        

