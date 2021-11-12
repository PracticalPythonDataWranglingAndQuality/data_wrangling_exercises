# Objective: Filter all September, 2020 Citi Bike rides, and output a new
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
def main():
    # open our data file in "read" mode
    source_file = open("202009-citibike-tripdata.csv","r")
    # open our output file in "write" mode
    output_file = open("202009-citibike-weekday-tripdata.csv","w")
    # pass our source_file to the DictReader "recipe"
    # and store the result in a variable called `citibike_reader`
    citibike_reader = csv.DictReader(source_file)
    # create a corresponding DictWriter; specify its fieldnames should
    # be drawn from `citibike_reader`
    output_writer = csv.DictWriter(output_file, fieldnames=citibike_reader.fieldnames)
    # actually write the header row to the output file
    output_writer.writeheader()
    # loop through our `citibike_reader` rows
    for a_row in citibike_reader:
        # if the current 'starttime' value is a weekday
        if is_weekday(a_row['starttime']):
            # write that row of data to our output file
            output_writer.writerow(a_row)
    # close the output file
    output_file.close()


def is_weekday(date_string, date_format='%Y-%m-%d %H:%M:%S.%f'):

    # convert the value in the 'date_string' to datetime format
    the_date = datetime.strptime(date_string, date_format)

    # if `the_date` is a weekday (i.e., its integer value is 0-5)
    if the_date.weekday() <= 4:
        return(True)
    else:
        return(False)

if __name__ == "__main__":
    main()
