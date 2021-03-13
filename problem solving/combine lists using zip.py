# with the help of zip function you can combine two lists

movies = ["Hacksaw Ridge", "Forest gump", "The butterfly effect", "the conjuring"]
ratings = [7, 9, 10, 8]
new_list = []
for items in zip(movies, ratings):
    new_list.append(items)

print(new_list)
