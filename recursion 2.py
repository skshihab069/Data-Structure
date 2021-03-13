def recursion(times, n=1):
    print("I love EDM Times {}".format(n))
    if n < times:
        recursion(times, n + 1)


number = int(input("how many times do u want to print "))
print(recursion(number))
