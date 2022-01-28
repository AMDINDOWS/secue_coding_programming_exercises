import timeit

start = timeit.default_timer()

def fib(n):
        if n == 0:
            return(0)
        if n == 1:
            return(1)
        return(fib(n-1) + fib(n-2))

stop = timeit.default_timer()

print('Time: ', stop - start)  


def encrypt(string,n):
    lstr=string.lower()
    print(lstr)
    newstr=''
    for i in lstr:
        update = ord(i) + n
        if update>122:
            newupdate = update
            update = 96 + newupdate-122
        newstr = newstr + chr(update)

    newstr.lower()
    newstr=newstr[::-1]
    return newstr
print(encrypt("xcrzAKQZrgz", 5))  

def create_matrix(r,c):
    m=[[i,i+1,i+2]for i in range(0,c)]
    for i in m:
        return (' '.join(str(i)))
    

print(create_matrix(4,5))


a = [2**i for i in range(0,10)]

print (a)

def output(list):

    
    t1=tuple(list)
    t1=t1[::-1]
    return t1

print(output([1,2,3]))    