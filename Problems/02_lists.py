# LISTS (25pts)
# Show work on all problems.  Manually finding the answer doesn't count

# PROBLEM 1 (Using List Comprehensions - 8pts)
# Use list comprehensions to do the following:
# a) Make a list of numbers from 1 to 100
my_list = [x for x in range(1,101)]
print(my_list)
# b) Make a list of even numbers from 20 to 40
my_numlist = [x for x in range(20,41) if x % 2 == 0]
print(my_numlist)
# c) Make a list of squares from 1 to 100 (1 ** 2 to 100 ** 2)
my_list2 = [x ** 2 for x in range(1, 101)]
print(my_list2)
# d) Make a list of all positive numbers in my_list below.
my_list = [-77, -78, 82, 81, -40, 2, 62, 65, 74, 48, -37, -52, 90, -84, -79, -45, 47, 60, 35, -18]
my_list3 = [x for x in my_list if x > 0]
print(my_list3)

# PROBLEM 2 (Import the number list - 3pts)
# The Problems directory contains a file called "number_list.py"
# import this file which contains num_list
# Print the last 5 numbers in num_list

from Problems.number_list import num_list
print(num_list[-5:])


# PROBLEM 3 (List functions and methods - 8pts)
# Find and print the highest number in num_list (1pt)
print(max(num_list))
# Find and print the lowest number in num_list (1pt)
print(min(num_list))
# Find and print the average of num_list (2pts)
print(sum(num_list) // len(num_list))
# Remove the lowest number from num_list (2pt)
print(num_list[1:])
# or you can do...
# num_list.sort()
# num_list.pop(0)
# print(num_list)

# Create and print a new list called top_ten which contains only the 10 highest numbers in num_list(2pts)

top_ten = (num_list[-10:])
print(top_ten)



# PROBLEM 4 (4pts)
# Find the number which appears most often in num_list?

count = 0
number = 0

for n in num_list:
    if num_list.count(n) > count:
        count = num_list.count(n)
        number = n
        print(n)


# another way:
# my_counts = [num_list.count(x) for x in num_list]
# print(my_counts)
# print(num_list[my_counts.index(max(my_counts))])

# CHALLENGE PROBLEMS (2pts)
# TOUGH PROBLEMS, BUT FEW POINTS

# Find the number of prime numbers in num_list?
# Hint: One way is to just start removing the ones that aren't

def is_prime(n):
    for i in range(2, n//2):
        if n % 1 == 0:
            return False
    return True

print(is_prime(102))



# Find the number of  palindromes
# Hint: This may be easier to do with strings

string_list = [str(x) for x in num_list]

def is_palindrome(my_string):
    for i in range(len(my_string)):
        if my_string[i] != my_string[-i -1]:
            return False
    return True

print(is_palindrome("AMANAPLANACANALPANAMA"))

# Find the number of palindromes
# Hint: This may be easier to do with strings




