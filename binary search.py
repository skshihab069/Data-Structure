# Binary search is a searching technique for a sorted list
# it is much more efficient than linear search


# Binary search operates by searching through mid points of a list
# it checks if the mid point is the required search number
# if the mid is not the searched item it checks if the search number is greater than or smaller than mid point
# if the searched item is greater than mid point it removes the lower part of list and sets mid as first item of list
# if the searched item is smaller than mid point it removes the upper part of list and sets mid as las ittem of list

def binary_search(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if list[mid] == item:
            found = True
        elif item > list[mid]:
            first = mid + 1
        else:
            last = mid - 1

    return found


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item = 11

if binary_search(my_list, item):
    print("The item is in list")
else:
    print("The item is not in list")
