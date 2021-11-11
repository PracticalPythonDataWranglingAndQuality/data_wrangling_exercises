# fictional list of chapter page counts
page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30]

# variable for tracking total page count; starting value is 0
total_pages = 0

# for every item in the list, perform some action

for a_number in page_counts:
    print("Top of loop!")
    print("The current item is:")
    print(a_number)
    total_pages = total_pages + a_number
    print("The running total is:")
    print(total_pages)
    print("Bottom of loop!")

print(total_pages)
