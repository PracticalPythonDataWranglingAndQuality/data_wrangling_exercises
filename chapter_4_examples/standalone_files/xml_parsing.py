# An example of reading data from a .xml file with Python, using the "lxml"
# library.
# First, you'll need to pip install the lxml library:
# https://pypi.org/project/lxml/
# A helpful tutorial can be found here: https://lxml.de/tutorial.html
# The data used here is an instance of
# https://api.stlouisfed.org/fred/series/observations?series_id=U6RATE& \
# api_key=YOUR_API_KEY_HERE

# specify the "chapter" of the `lxml` library you want to import,
# in this case, `etree`, which stands for "ElementTree"
from lxml import etree

# import the `csv` library, to create our output file
import csv

# choose a filename
filename = "U6_FRED_data"

# open our data file in read format, using "rb" as the "mode"
xml_source_file = open(filename+".xml","rb")

# pass our xml_source_file as an ingredient to the the `lxml` library's
# `etree.parse()` method and store the result in a variable called `xml_doc`
xml_doc = etree.parse(xml_source_file)

# start by getting the current xml document's "root" element
document_root = xml_doc.getroot()

# let's print it out to see what it looks like
print(etree.tostring(document_root))

# confirm that `document_root` is a well-formed XML element
if etree.iselement(document_root):

    # create our output file, naming it "xml_"+filename+".csv
    output_file = open("xml_"+filename+".csv","w")

    # use the `csv` library's "writer" recipe to easily write rows of data
    # to `output_file`, instead of reading data *from* it
    output_writer = csv.writer(output_file)

    # grab the first element of our xml document (using `document_root[0]`)
    # and write its attribute keys as column headers to our output file
    output_writer.writerow(document_root[0].attrib.keys())

    # now, we need to loop through every element in our XML file
    for child in document_root:

        # now we'll use the `.values()` method to get each element's values
        # as a list, and then use that directly with the `writerow` recipe
        output_writer.writerow(child.attrib.values())

    # officially close the `.csv` file we just wrote all that data to
    output_file.close()
