# Quick script for adding a "fingerprint" column to our loan data, which will
# help us confirm/correct for any typos or inconsistencies in, e.g. borrower
# name and address information

# import the csv library
import csv

# importing the `fingerprints` library
import fingerprints

# read the recent data sample into a variable
ppp_data = open('public_150k_plus_221.csv','r')

# the DictReader function has added useful information to our data,
# like a label that shows us all the values in the first or "header" row
ppp_data_reader = csv.DictReader(ppp_data)

# create an output file to write our modified data set to
augmented_ppp_data = open('public_150k_plus_borrower_fingerprint_a.csv','w')

# create a "writer" so that we can output whole rows at once
augmented_data_writer = csv.writer(augmented_ppp_data)

# because we're adding a column, we need to create a new header row as well
header_row = []

# for every column header
for item in ppp_data_reader.fieldnames:

    # append the existing column header
    header_row.append(item)

    # if we're at 'OriginatingLender'
    if item == 'BorrowerName':

        # it's time to add a new one!
        header_row.append('BorrowerNameFingerprint')

# write the completed header row to the output file
augmented_data_writer.writerow(header_row)

# iterate through row in the data
for row in ppp_data_reader:

    # adding a column means we need to build the new row of data
    # item by item, just as we did with the header row
    new_row = []

    # for each column of data in the *original* data set
    for column_name in ppp_data_reader.fieldnames:

        # first, append this row's value for that column
        new_row.append(row[column_name])

        # when we get to the 'OriginatingLender' column, it's time
        # to add our new "fingerprint" value
        if column_name == 'BorrowerName':

            # our fingerprint will consist of the generated fingerprint PLUS
            # the BorrowerZip
            try:
                the_fingerprint = fingerprints.generate(row[column_name]) +" "+ fingerprints.generate(row['BorrowerCity'])+" "+row['BorrowerState']
            except(TypeError):
                the_fingerprint = fingerprints.generate("MISSING") +" "+ fingerprints.generate(row['BorrowerCity'])+" "+row['BorrowerState']

            new_row.append(the_fingerprint)

    # once the whole row is complete, write it to our output file
    augmented_data_writer.writerow(new_row)

# close both files
augmented_ppp_data.close()
ppp_data.close()
