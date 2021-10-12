# use a for loop with enumerate to go over the long word and
# sum all the indices for every single vowel

# example:
#
# input: "hi I me
# i=1, I=3, e = 6,
# the sum is: 10
print("The vowels")
a_long_word = "the quick brown fox jumped over the lazy dog and then ran around and got very happy happy happy yes!"
# the sum should be 99 (you can check your code with this)
sum = 0
for x,vowels in enumerate(a_long_word):
    if (vowels == "a")or( vowels =="e") or (vowels =="i") or (vowels =="o") or (vowels =="u") :
        print(x,vowels)
        sum = sum + x
        print(f"\nCurrent sum of vowels is : {sum}")
    x +=1    