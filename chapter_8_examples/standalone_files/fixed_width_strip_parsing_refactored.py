""" NOAA data formatter
Reads data from an NOAA fixed-width data file with Python and outputs
a well-formatted CSV file.
The source file for this example comes from the NOAA, and can be accessed here:
https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
The metadata for the file can be found here:
https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/readme.txt
Available functions
-------------------
* convert_to_columns: Converts a line of text to a list
Requirements
------------
* csv module
"""
# we'll start by importing the "csv" library
import csv

def main():

    # variable to match our output filename to the input filename
    filename = "ghcnd-stations"

    # we'll just open the file in read format ("r") as usual
    source_file = open(filename+".txt", "r")

    # the "readlines()" method converts a text file to a list of lines
    stations_list = source_file.readlines()

    # as usual, we'll create an output file to write to
    output_file = open(filename+".csv","w")

    # and we'll use the `csv` library to create a "writer" that gives us handy
    # "recipe" functions for creating our new file in csv format
    output_writer = csv.writer(output_file)

    # we have to "hard code" these headers using the contents of `readme.txt`
    headers = ["ID","LATITUDE","LONGITUDE","ELEVATION","STATE","NAME",
    "GSN_FLAG","HCNCRN_FLAG","WMO_ID"]

    # create a list of `tuple`s with each column's start and end index
    column_ranges = [(1,11),(13,20),(22,30),(32,37),(39,40),(42,71),(73,75),
    (77,79),(81,85)]

    # write our headers to the output file
    output_writer.writerow(headers)

    # loop through each line of our file
    for line in stations_list:

        # send our data to be formatted
        new_row = convert_to_columns(line, column_ranges)

        # use the `writerow` function to write new_row to our output file
        output_writer.writerow(new_row)

    # for good measure, close our output file
    output_file.close()


def convert_to_columns(data_line, column_info, zero_index=False):

    """Converts a line of text to a list based on the index pairs provided
    Parameters
    ----------
    data_line : str
    The line of text to be parsed
    column_info : list of tuples
    Each tuple provides the start and end index of a data column
    zero_index: boolean, optional
    If False (default), reduces starting index position by one
    Returns
    -------
    list
    a list of data values, stripped of surrounding whitespace
    """
    new_row = []

    # function assumes that provided indices are *NOT* zero-indexed,
    # so reduce starting index values by 1
    index_offset = 1

    # if column_info IS zero-indexed, don't offset starting index values
    if zero_index:
        index_offset = 0

    # go through list of column indices
    for index_pair in column_info:

        # pull start value, modifying by `index_offset`
        start_index = index_pair[0]-index_offset

        # pull end value
        end_index = index_pair[1]

        # strip whitespace from around the data
        new_row.append((data_line[start_index:end_index]).strip())

    # return stripped data
    return new_row


if __name__ == "__main__":
    main()
