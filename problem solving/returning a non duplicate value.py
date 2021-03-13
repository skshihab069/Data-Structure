# dictionaries have O(1) complexity
# dictionary follows hash table

def non_duplicate(list):
    dictionary = {}
    for item in list:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    for key, value in dictionary.items():
        if value == 1:
            print(key)


listt = [1, 2, 2, 3, 3, 4, 4]

print(non_duplicate(listt))
