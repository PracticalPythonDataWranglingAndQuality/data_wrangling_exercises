# fictional list of chapter page counts
page_counts = [28, 32, 44, 23, 56, 32, 12, 34, 30]

# define a new `count_pages()` function that takes one ingredient/argument:
# a list of numbers
def count_pages(page_count_list):

    # create variables to keep track of:
    # the total pages in the book
    total_pages = 0

    # the number of chapters with more than 30 pages,
    under_30 = 0

    # the number of chapters with fewer than 30 pages
    over_30 = 0

    # for every item in the page_count_list:
    for a_number in page_count_list:

        # add the current number of pages to our total_pages count
        total_pages = total_pages + a_number

        # check if the current number of pages is more than 30
        if a_number > 30:

            # if so, add 1 to our over_30 counter
            over_30 = over_30 + 1

            # otherwise...
        else:

            # add 1 to our under_30 counter
            under_30 = under_30 + 1

    # print our various results
    print(total_pages)
    print("Number of chapters over 30 pages:")
    print(over_30)
    print("Number of chapters under 30 pages:")
    print(under_30)

# call/execute this "recipe", being sure to pass in our
# actual list as an argument/ingredient
count_pages(page_counts)
