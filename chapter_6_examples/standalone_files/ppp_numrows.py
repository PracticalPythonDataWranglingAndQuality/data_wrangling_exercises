# Quick script to print out the number of rows in each of our PPP loan data files
# This is a pretty basic task, so no need to import extra libraries!

# open the August PPP data in "read" mode
august_data = open("public_150k_plus_080820.csv","r")

# use `readlines()` to convert the lines in the data file into a list
print("August file has "+str(len(august_data.readlines()))+" rows.")

# ditto for the recent PPP data
recent_data = open("public_150k_plus_recent.csv","r")

# once again, print the number of lines
print("Recent file has "+str(len(recent_data.readlines()))+" rows.")
