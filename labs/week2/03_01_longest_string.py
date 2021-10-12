# Which of the following strings is the longest?
# Use the len() function to find out.
# You can run `len(my_variable)` and it will return the len of the variable (in this case it's a string)


longest_german_word = "Donaudampfschifffahrtsgesellschaftskapitänskajütentürschnalle"
longest_hungarian_word = "Megszentségteleníthetetlenségeskedéseitekért"
longest_finnish_word = "Lentokonesuihkuturbiinimoottoriapumekaanikkoaliupseerioppilas"
strong_password = "%8Ddb^ca<*'{9pur/Y(8n}^QPm3G?JJY}\(<bCGHv^FfM}.;)khpkSYTfMA@>N"

a = len(longest_german_word)
b = len(longest_hungarian_word)
c = len(longest_finnish_word)
d = len(strong_password)
 
print (" value of a =" f"{a}\n","value of b =" f"{b}\n","value of c =" f"{c}\n","value of d =" f"{d}")
print("The longest word is strong_passwd : "f"{strong_password}")

# Now that you know what the longest word is, print it out in an f-string below

