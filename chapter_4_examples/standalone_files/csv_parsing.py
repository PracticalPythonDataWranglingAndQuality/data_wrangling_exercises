# A simple example of reading data from a .csv file with Python
# using the "csv" library.
# The source data was sampled from the Citi Bike system data:
# https://drive.google.com/file/d/17b461NhSjf_akFWvjgNXQfqgh9iFxCu_/
# Which can be found here:
# https://s3.amazonaws.com/tripdata/index.html

# import the `csv` library
import csv

# open the `202009CitibikeTripdataExample.csv` file in read ("r") mode
# this file should be in the same folder as our Python script or notebook
source_file = open("202009CitibikeTripdataExample.csv","r")

# pass our `source_file` as an ingredient to the the `csv` library's
# DictReader "recipe".
# Store the result in a variable called `citibike_reader`
citibike_reader = csv.DictReader(source_file)

# the DictReader method has added some useful information to our data,
# like a `fieldnames` property that lets us access all the values
# in the first or "header" row
print(citibike_reader.fieldnames)

# let's just print out the first 5 rows
for i in range(0,5):
    print (next(citibike_reader))
