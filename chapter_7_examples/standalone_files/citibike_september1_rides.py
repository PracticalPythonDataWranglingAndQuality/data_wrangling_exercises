# Objectives: Filter all September, 2020 Citi Bike rides, and output a new
# file containing only the rides from 2020-09-01

# Program Outline:
# 1. Read in the data file: 202009-citibike-tripdata.csv
# 2. Create a new output file, and write the header row to it.
# 3. For each row in the file, split the `starttime` value on space:
# a. If the first item in the resulting list is '2020-09-01', write
# the row to our output file
# 4. Close the output file

# import the "csv" library
import csv

# open our data file in "read" mode
source_file = open("202009-citibike-tripdata.csv","r")

# open our output file in "write" mode
output_file = open("2020-09-01-citibike-tripdata.csv","w")

# pass our source_file to the DictReader "recipe"
# and store the result in a variable called `citibike_reader`
citibike_reader = csv.DictReader(source_file)

# create a corresponding DictWriter and specify that the
# header should be the same as the `citibike_reader` fieldnames
output_writer = csv.DictWriter(output_file, fieldnames=citibike_reader.fieldnames)

# write the header row to the output file
output_writer.writeheader()

# use a `for...in` loop to go through our `citibike_reader` list of rows
for a_row in citibike_reader:

    # get the value in the 'starttime' column
    start_timestamp = a_row["starttime"]

    # split the value in 'starttime' on the space character
    timelist = start_timestamp.split(" ")

    # the "date" part of the string will be the first item, position 0
    the_date = timelist[0]

    # if `the_date` matches our desired date
    if the_date == "2020-09-01":

        # write that row of data to our output file
        output_writer.writerow(a_row)

# close the output file
output_file.close()
