# recursion is a method of solving problem by breaking it into smaller parts
# any problem that can be solved by iterative algorithms can be solved by recursion
# recursion is simply repeating a function until it reaches its base case
# a base case is a condition that stops the recursion
# recursion does a similar job as for loop but in a functional way
# problems that can be solve by iteration can be solved recursively

# Recursion has 3 rules
#  1. Every recursive algo must have a base case
#  2. Recursive algo must change state and move towards the base case
#  3. Recursive algo must call its self recursively


def recursion(word):
    ############### 1. BASE CASE ##############
    if word < 1:
        print("""No more bottles of beer on the wall. No more 
                 bottles of beer.""")
        return

    temp = word
    word -= 1  ######## 2. changing state and moving towards base case

    print("""{} bottles of beer on the wall. {} bottles
             of beer. Take one down, pass it around, 
             {} bottles of beer on the wall.""".format(temp, temp, word))

    recursion(word)  ########## 3. calling it self


def recursion_example2(num):
    # base
    if num >= 5:
        print("NUmber printing done")
        return
    # changing state
    print(num)
    num += 1
    # calling it self
    recursion_example2(num)


print(recursion(99))
print(recursion_example2(0))
