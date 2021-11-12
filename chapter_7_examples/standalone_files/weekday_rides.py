# Objectives: Filter all September, 2020 Citi Bike rides, and output a new
# file containing only weekday rides
# Program Outline:
# 1. Read in the data file: 202009-citibike-tripdata.csv
# 2. Create a new output file, and write the header row to it.
# 3. For each row in the file, make a date from the `starttime`:
# a. if it's a weekday, write the row to our output file
# 4. Close the output file

# import the "csv" library
import csv

# import the "datetime" library
from datetime import datetime

# open our data file in "read" mode
source_file = open("202009-citibike-tripdata.csv","r")

# open our output file in "write" mode
output_file = open("202009-citibike-weekday-tripdata.csv","w")

# convert source data to a DictReader; store the result in `citibike_reader`
citibike_reader = csv.DictReader(source_file)

# create a corresponding DictWriter and specify its fieldnames
output_writer = csv.DictWriter(output_file, fieldnames=citibike_reader.fieldnames)

# actually write the header row to the output file
output_writer.writeheader()

# use a `for...in` loop to go through our `citibike_reader` list of rows
for a_row in citibike_reader:

    # convert the value in the 'starttime' column to a date object
    the_date = datetime.strptime(a_row['starttime'], '%Y-%m-%d %H:%M:%S.%f')

    # if `the_date` is a weekday
    if the_date.weekday() <= 4:

        # write that row of data to our output file
        output_writer.writerow(a_row)

# close the output file
output_file.close()
