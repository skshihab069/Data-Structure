# finds the intersection  between 2 lists
def intersection(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3


num_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 8]
num_list2 = [5, 6, 7, 8, 9, 10, 11]
print(intersection(num_list1, num_list2))


# Alternative method using sets
# the intersection method intersects two or multiple sets
def intersections(list1, list2):
    a_set = set(list1)
    b_set = set(list2)
    list3 = a_set.intersection(b_set)
    return list3


listt1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
listt2 = [4,5,6,7,8,9,0]
print(intersections(listt1,listt2))