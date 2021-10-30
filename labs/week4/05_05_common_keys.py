# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

results = {}
for item in dict_1:
    print(item)
    if item in dict_2:
        results[item] = dict_1[item] + dict_2[item]
    else:
        results[item] = dict_1[item]

for item in dict_2:
    if item not in results:
        results[item] = dict_2[item]
  
print(results)          