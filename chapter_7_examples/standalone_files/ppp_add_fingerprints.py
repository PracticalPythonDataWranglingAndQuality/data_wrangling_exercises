# Quick script for adding a "fingerprint" column to our loan data, which will
# help us confirm/correct for any typos or inconsistencies in, e.g., bank names

# import the csv library
import csv

# importing the `fingerprints` library
import fingerprints

# read the recent data sample into a variable
ppp_data = open('public_150k_plus_recent.csv','r')

# the DictReader function makes our source data more usable
ppp_data_reader = csv.DictReader(ppp_data)

# create an output file to write our modified dataset to
augmented_ppp_data = open('public_150k_plus_fingerprints.csv','w')

# create a "writer" so that we can output whole rows at once
augmented_data_writer = csv.writer(augmented_ppp_data)

# because we're adding a column, we need to create a new header row as well
header_row = []

# for every column header
for item in ppp_data_reader.fieldnames:

    # append the existing column header
    header_row.append(item)

    # if we're at 'OriginatingLender'
    if item == 'OriginatingLender':

        # it's time to add a new column
        header_row.append('OriginatingLenderFingerprint')

# now we can write our expanded header row to the output file
augmented_data_writer.writerow(header_row)

# iterate through every row in our data
for row in ppp_data_reader:

    # create an empty list to hold our new data row
    new_row = []

    # for each column of data in the *original* dataset
    for column_name in ppp_data_reader.fieldnames:

        # first, append this row's value for that column
        new_row.append(row[column_name])

        # when we get to the 'OriginatingLender' column, it's time
        # to add our new "fingerprint" value
        if column_name == 'OriginatingLender':

            # our fingerprint will consist of the generated fingerprint PLUS
            # the OriginatingLenderLocationID
            the_fingerprint = fingerprints.generate(row[column_name]) + \
            " " + row['OriginatingLenderLocationID']

            # append the compound fingerprint value to our row
            new_row.append(the_fingerprint)

    # once the whole row is complete, write it to our output file
    augmented_data_writer.writerow(new_row)

# close both files
augmented_ppp_data.close()
ppp_data.close()
