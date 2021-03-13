# List comprehension is technique where you can create lists by adding for loops,
# and if conditions according to list criteria
# list = [expression(i) for var in collections if conditions]
# list comprehension makes code more minimal and with fewer lines of code


# without list comprehension
squares = []
for i in range(1,101):
    squares.append(i**2)
print(squares)

# with list comprehension
squares = [i**2 for i in range(1,101)]

print(squares)