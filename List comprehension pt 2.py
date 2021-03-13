# creates a new list of items which are larger than 5  from a given list
string = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [charecter for charecter in string if charecter > 5]
print(new_list)

# creates a list of series which start with "br" from a given list
movies = ["breaking bad","big bang theory","game of thrones"]
best_series = [string for string in movies if string.startswith("br")]
print(best_series)