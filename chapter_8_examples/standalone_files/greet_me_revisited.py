# create a function that prints out a greeting
# to any name passed to the function
def greet_me(a_name):
 print("Variable `a_name` in `greet_me`: "+a_name)
 print("Hello "+a_name)

# create a variable named `author`
author = "Susan E. McGregor"

# create another variable named `editor`
editor = "Jeff Bleiel"

a_name = "Python"
print("Variable `a_name` in main script: "+a_name)

# use my custom function, `greet_me` to output "Hello" messages to each person
greet_me(author)
greet_me(editor)

print("Variable `a_name` in main script again: "+a_name)
