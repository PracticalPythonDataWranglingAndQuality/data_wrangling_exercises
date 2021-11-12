# function that returns a greeting to any name passed in
def make_greeting(a_name):
    return("Hello "+a_name)

# function that adds a question to any greeting
def add_question(a_greeting):
    return(a_greeting+", how are you?")

# create a variable named author
author = "Susan E. McGregor"

# create another variable named editor
editor = "Jeff Bleiel"

# print the greeting message
print(make_greeting(author))

# pass the greeting message to the question function and print the result!
print(add_question(make_greeting(editor)))
