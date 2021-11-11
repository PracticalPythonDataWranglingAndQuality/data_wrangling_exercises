# splitting a string "literal" and then printing the result
split_world = "Hello World!".split()
print(split_world)

# assigning a string to a variable
# then printing the result of calling the `split()` method on it
world_msg = "Hello World!"
print(world_msg.split())

# the following will produce an error because
# the `split()` method must be called on a string in order to work!
split("Hello World!")
