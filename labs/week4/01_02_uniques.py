# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [1, 2, 6, 55, 'hi', 4, 13,]

List= [1,2,3,4,4,4,'hello','hi','bye']

set = set(List)

print(set)

unique_list = list(set)

print(f"\nTHE Qnique list is : {unique_list}")