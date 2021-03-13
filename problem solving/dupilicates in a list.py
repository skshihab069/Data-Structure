# sets are containers that contain non duplicate elements
# sets are unordered but mutable
# create empty list
# create empty set
# check length of set
# add item to set and check length
# if check 1 matches check 2 add to duplicate list
# print dupp list

def duplicates(my_list):
    dup = []
    my_set = set()
    for item in my_list:
        check_len = len(my_set)
        my_set.add(item)
        check_len2 = len(my_set)
        if check_len == check_len2:
            dup.append(item)
    return dup


my_listt = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9]

print(duplicates(my_listt))
