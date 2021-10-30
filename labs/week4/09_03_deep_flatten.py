# Make your list flatten code do a DEEP flatten and account for other datatypes

hard_nested_list = [
    [1, 2, [1, [1, 2], 2], 3, 4],
    [5, 6],
    [7, 8, 9],
    "shiva",
    10,
    [1, 2, [8, 9,], "Devi"],
    10.0,
    (1, 2),
]

# should get back
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'brandon', 10, 10.0, 1, 2]

many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']
count =0
flat_list=[]
while True:
    for item in hard_nested_list:
        if isinstance(item,list) or isinstance(item,tuple):
            flat_list.extend(item)
        else:
            flat_list.append(item)
    print(flat_list)
    hard_nested_list= flat_list
    flat_list =[]
    
    for item in hard_nested_list:
        if (isinstance(item,list) or isinstance(item,tuple)) :
            break
    else:
        break    



