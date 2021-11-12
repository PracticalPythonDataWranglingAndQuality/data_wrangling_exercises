# Converting data in an .xls file with Python to csv + metadata file, with
# functional date values using the "xrld" library.

# First, pip install the xlrd library:
# https://pypi.org/project/xlrd/2.0.1/
# then, import the `xlrd` library
import xlrd

# import the csv library
import csv

# needed to test if a given value is *some* type of number
from numbers import Number

# for parsing/formatting our newly interpreted Excel dates
from datetime import datetime

# pass our filename as an ingredient to the `xlrd` library's
# `open_workbook()` "recipe"
# store the result in a variable called `source_workbook`
source_workbook = xlrd.open_workbook("fredgraph.xls")

# open and name a simple metadata text file
source_workbook_metadata = open("fredgraph_metadata.txt","w")

# an `.xls` workbook can have multiple sheets
for sheet_name in source_workbook.sheet_names():

    # create a variable that points to the current worksheet by
    # passing the current value of `sheet_name` to the `sheet_by_name` recipe
    current_sheet = source_workbook.sheet_by_name(sheet_name)

    # create "xls_"+sheet_name+".csv" as an output file for the current sheet
    output_file = open("xls_"+sheet_name+"_dates.csv","w")

    # use the `csv` library's "writer" recipe to easily write rows of data
    # to `output_file`, instead of reading data *from* it
    output_writer = csv.writer(output_file)

    # create a Boolean variable to detect if we've hit our table-type data yet
    is_table_data = False

    # now, we need to loop through every row in our sheet
    for row_num, row in enumerate(current_sheet.get_rows()):

        # pulling out the value in the first column of the current row
        first_entry = current_sheet.row_values(row_num)[0]

        # if we've hit the header row of our data table
        if first_entry == 'observation_date':

            # it's time to switch our "flag" value to "True"
            is_table_data = True

        # if `is_table_data` is True
        if is_table_data:

            # extract the table-type data values into separate variables
            the_date_num = current_sheet.row_values(row_num)[0]
            U6_value = current_sheet.row_values(row_num)[1]

            # create a new row object with each of the values
            new_row = [the_date_num, U6_value]

            # if the `the_date_num` is a number, then the current row is *not*
            # the header row. We need to transform the date.
            if isinstance(the_date_num, Number):

                # use the xlrd library's `xldate_as_datetime()` to generate
                # a Python datetime object
                the_date_num = xlrd.xldate.xldate_as_datetime(
                the_date_num, source_workbook.datemode)

                # overwrite the first value in the new row with
                # the reformatted date
                new_row[0] = the_date_num.strftime('%m/%d/%Y')

            # write this new row to the data output file
            output_writer.writerow(new_row)

        # otherwise, this row must be metadata
        else:

            # since we'd like our metadata file to be nicely formatted, we
            # need to loop through the individual cells of each metadata row
            for item in current_sheet.row(row_num):

                # write the value of the cell
                source_workbook_metadata.write(item.value)

                # separate it from the next cell with a tab
                source_workbook_metadata.write('\t')

            # at the end of each line of metadata, add a newline
            source_workbook_metadata.write('\n')

    # just for good measure, let's close our output files
    output_file.close()
    source_workbook_metadata.close()
