# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# CrashCourse
# 1-- variables.
# age = 20 #integer
# price = 19.95 #float
# first_name = "Nick" #string
# is_online = True #boolean
# print(age)

# 2 -- using the input function in python
# name = input("What is your name? ")
# print("Hello " + name)

# 3 --  type conversion in python
# birth_year = input("Enter your birth year: ")
# age = 2024 - int(birth_year)
# print(age)
# int(), float() bool() str() other type conversions
# function adding two numbers.
# first_number = float(input("Enter first number: "))
# second_number = float(input("Enter second number: "))
# sum = first_number + second_number
# print("Result is: " + str(sum))

# 4 -- Strings
# course = "Python for Beginners"
# print(course.find('y'))
# print(course.upper())
# print(course.find('for'))
# print(course.replace('for', '4'))
# print('Python' in course)

# 5 -- arithmetic operators
# print(10+3)
# print(10/3) # returns decimal (3.3333333)
# print(10//3) # returns a whole number (3)
# print(10%3) # returns 1 remainder after dividing 10 by 3
# print(10 ** 3) # returns 10 to the power of 3 (exponent)
# x = 10
# x = x + 3 # returns 13
# x += 3 # augmented assignment operator (returns 13

# 6 -- operator precedence. orders in which arithmetic are done
# x = 10 + 3 * 2 # result is 16
# print(x)
# x = (10 + 3) * 2 # result is 26

# 7 -- comparison operators
# x = 3  != 2
# # > >= < <= == !=
# print(x)

# 8 -- logical operators
# price = 25
# print(price > 10 and price < 30) # if the first and second expression are true it will return true
# print (price > 10 or price < 10 ) # if at least one of the two expressions are true then the result of the expression will be true
# print (not price > 30) # inverse the true
# and (both) are true
# or ( at least one is true)
# not ( inverses the value given)

 # 9 -- if statements.
# temperature = 25
# if temperature > 30:
#      print("It's a hot day")
#      print("Drink plenty of water")
# elif temperature > 20: # (20, 30)
#     print("It's a nice day!")
# elif temperature > 10: # (10, 20)
#     print("It's a bit cold")
# else:
#     print("It's cold")
#
# # Exercise for converting weight (lbs) to (kgs) and vice-versa
# weight = float(input("Weight: "))
# unit = input("(K)g or (L)bs:")
# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("weight in Kgs: " + str(converted))

# 10 -- while loops
# i = 1
# while i <= 1_000: # instead of 1000 we put 1_000 to make the code more readable
#     print(i)
#     i+=1
# while i <= 10:
#     print(i * '*') # multiply with a string
#     i+=1

# 11 -- Lists
names = ["John", "Bob", "Mosh", "Sam", "Nick"]
print(names)
print(names[0]) #prints the first item in the list
print(names[-1]) #prints the last item in the list
names[0] = "Johnny"
print(names)
print(names[0:3]) # prints 0, 1, 2 excluding a 3





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
