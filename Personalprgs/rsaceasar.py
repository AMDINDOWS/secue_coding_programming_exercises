import math
import random
#CEASER

def encrypt(message, key):
 
    cipher = ''
    for char in message:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + key - 97) % 26 + 97)
  
    return cipher

def decrypt(message, key):
 
    cipher = ''
    for char in message:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char)- key - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - key - 97) % 26 + 97)
    
    return cipher

#RSA
def rsaencrypt(me):
    p = 11
    q = 7
    n = p*q
    z = (p-1)*(q-1)
    lst=[i for i in range(2, z + 1) if all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))]

    e = random.choice(lst)
    
    print(e)
    
    pvk = math.pow(me,e)
    c = pvk % n
    
    return c
def rsadecrypt(ct):
    p = 11
    q = 7
    n = p*q
    z = (p-1)*(q-1)
    lst=[i for i in range(2, z + 1) if all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))] #prime less than z

    e = random.choice(lst)
    
    print(e)
    
    pvk = math.pow(ct,e)
    m = ct**pvk % n
    return m






print("\nWhat operation do you want to perform? \nCeaser Encryption (Enter (1)) \nCeaser Decryption(Enter (2)) \nRSA Encryption(Enter (3)) \nRSA Decryption(Enter (4))")
action=int(input("\nEnter Your choice : "))
if action==1:    
    text = input("\nEnter string to encrypt: ")
    s = int(input("\nEnter key number: "))
    print("Original string: ", text)
    print("After encryption: ", encrypt(text, s))
elif action==2:
    text = input("\nEnter string to Decrypt: ")
    s = int(input("\nEnter key number: "))
    print("Original string: ", text)
    print("After Decryption: ", decrypt(text, s))
elif action==3:
    data= int(input("\nEnter the message to be encrypted: "))
    print("\nOriginal Message is: ", data)
    print("\nAfter Encryption RSA: ", rsaencrypt(data))          
elif action==4:
    data= int(input("\nEnter the message to be Decrypted: "))
    print("\nOriginal Message is: ", data)
    print("\nAfter Decryption RSA: ", rsaencrypt(data))
