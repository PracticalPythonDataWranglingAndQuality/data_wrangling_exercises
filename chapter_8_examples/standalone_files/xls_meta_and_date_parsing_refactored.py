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

def main():
    # use `open_workbook()` to load our data in the `source_workbook` variable
    source_workbook = xlrd.open_workbook("fredgraph.xls")

    global the_datemode
    the_datemode = source_workbook.datemode

    # open and name a simple metadata text file
    source_workbook_metadata = open("fredgraph_metadata.txt","w")

    # an `.xls` workbook can have multiple sheets
    for sheet_name in source_workbook.sheet_names():

        # create a variable that points to the current worksheet
        current_sheet = source_workbook.sheet_by_name(sheet_name)

        # create "xls_"+sheet_name+".csv" as current sheet's output file
        output_file = open("xls_"+sheet_name+"_dates.csv","w")

        # use the `writer()` recipe to write `.csv`-formatted rows
        output_writer = csv.writer(output_file)

        # Boolean variable to detect if we've hit our table-type data yet
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

                # pass the requisite data to out `create_table_row()` function
                new_row = create_table_row(current_sheet, row_num)

                # write this new row to the data output file
                output_writer.writerow(new_row)

            # otherwise, this row must be metadata
            else:

                # pass the requisite data to our `create_meta_text()` function
                metadata_line = create_meta_text(current_sheet, row_num)

                # write this new row to the metadata output file
                source_workbook_metadata.write(metadata_line)

        # just for good measure, let's close our output files
        output_file.close()
        source_workbook_metadata.close()

def create_table_row(the_sheet, the_row_num):

    # extract the table-type data values into separate variables
    the_date_num = the_sheet.row_values(the_row_num)[0]
    U6_value = the_sheet.row_values(the_row_num)[1]

    # create a new row object with each of the values
    new_row = [the_date_num, U6_value]

    # if the `the_date_num` is a number, then the current row is *not*
    # the header row. We need to transform the date.
    if isinstance(the_date_num, Number):

        # use the xlrd library's `xldate_as_datetime()` to generate
        # a Python datetime object
        the_date_num = xlrd.xldate.xldate_as_datetime(the_date_num, the_datemode)

        # create a new list containing `the_date_num` (formatted to MM/DD/YYYY
        # using the `strftime()` recipe) and the value in the second column
        new_row = [the_date_num.strftime('%m/%d/%Y'),U6_value]

    # return the fully formatted row
    return(new_row)


def create_meta_text(the_sheet, the_row_num):
    
    meta_line = ""

    # since we'd like our metadata file to be nicely formatted, we
    # need to loop through the individual cells of each metadata row
    for item in the_sheet.row(the_row_num):
        # write the value of the cell, followed by a tab character
        meta_line = meta_line + item.value + '\t'

    # at the end of each line of metadata, add a newline
    meta_line = meta_line+'\n'

    # return the fully formatted line
    return(meta_line)


if __name__ == "__main__":
    main()
