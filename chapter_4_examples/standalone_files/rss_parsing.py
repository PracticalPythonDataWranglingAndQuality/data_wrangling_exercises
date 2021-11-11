# An example of reading data from an .xml file with Python, using the "lxml"
# library.
# First, you'll need to pip install the lxml library:
# https://pypi.org/project/lxml/
# The data used here is an instance of
# http://feeds.bbci.co.uk/news/science_and_environment/rss.xml

# specify the "chapter" of the `lxml` library you want to import,
# in this case, `etree`, which stands for "ElementTree"
from lxml import etree

# import the `csv` library, to create our output file
import csv

# choose a filename, for simplicity
filename = "BBC News - Science Environment XML Feed"

# open our data file in read format, using "rb" as the "mode"
xml_source_file = open(filename+".xml","rb")

# pass our xml_source_file as an ingredient to the the `lxml` library's
# `etree.parse()` method and store the result in a variable called `xml_doc`
xml_doc = etree.parse(xml_source_file)

# start by getting the current xml document's "root" element
document_root = xml_doc.getroot()

# if the document_root is a well-formed XML element
if etree.iselement(document_root):

    # create our output file, naming it "rss_"+filename+".csv"
    output_file = open("rss_"+filename+".csv","w")

    # use the `csv` library's "writer" recipe to easily write rows of data
    # to `output_file`, instead of reading data *from* it
    output_writer = csv.writer(output_file)

    # document_root[0] is the "channel" element
    main_channel = document_root[0]

    # the `find()` method returns *only* the first instance of the element name
    article_example = main_channel.find('item')

    # create an empty list in which to store our future column headers
    tag_list = []
    for child in article_example.iterdescendants():

        # add each tag to our would-be header list
        tag_list.append(child.tag)

        # if the current tag has any attributes
        if child.attrib:

            # loop through the attribute keys in the tag
            for attribute_name in child.attrib.keys():

                # append the attribute name to our `tag_list` column headers
                tag_list.append(attribute_name)

    # write the contents of `tag_list` to our output file as column headers
    output_writer.writerow(tag_list)

    # now we want to grab *every* <item> elment in our file
    # so we use the `findall()` method instead of `find()`
    for item in main_channel.findall('item'):

        # empty list for holding our new row's content
        new_row = []

        # now we'll use our list of tags to get the contents of each element
        for tag in tag_list:

            # if there is anything in the element with a given tag name
            if item.findtext(tag):

                # append it to our new row
                new_row.append(item.findtext(tag))

            # otherwise, make sure it's the "isPermaLink" attribute
            elif tag == "isPermaLink":

                # grab its value from the <guid> element
                # and append it to our row
                new_row.append(item.find('guid').get("isPermaLink"))

        # write the new row to our output file!
        output_writer.writerow(new_row)

    # officially close the `.csv` file we just wrote all that data to
    output_file.close()
