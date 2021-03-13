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


my_list = []
print("This is example of binary search\n\n".upper())

list_number = int(input("how many items do you want in your list "))
for i in range(0, list_number):
    items = int(input(f'enter item {i+1} '))
    my_list.append(items)

number = int(input("please enter the searched item -: "))
if binary_search(my_list, number):
    print("The item is in list")
else:
    print("the item is not in list")

