# create a function that prints out a greeting to any name
def greet_me(a_name, greeting="Hello"):
    print(greeting+" "+a_name)

# create a variable named author
author = "Susan E. McGregor"

# create another variable named editor
editor = "Jeff Bleiel"

# use `greet_me()` to output greeting messages to each person
# say "Hello" by default
greet_me(author)

# let the programmer specify "Hi" as the greeting
greet_me(editor, greeting="Hi")
