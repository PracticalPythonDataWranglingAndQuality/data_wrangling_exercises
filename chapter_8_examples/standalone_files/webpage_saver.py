""" Web page Saver!
Downloads the contents of a web page and saves it locally

Usage
-----
python webpage_saver.py target_url filename

Parameters
----------
target_url : str
 The full URL of the web page to be downloaded
filename : str
 The desired filename of the local copy

Requirements
------------
* argparse module
* requests module
"""

# include the requests library in order to get data from the web
import requests

# include argparse library to pull arguments from the command line
import argparse

# create a new `ArgumentParser()`
parser = argparse.ArgumentParser()

# arguments will be assigned based on the order in which they were provided
parser.add_argument("target_url", help="Full URL of web page to be downloaded")
parser.add_argument("filename", help="The desired filename of the local copy")
args = parser.parse_args()

# pull the url of the web page we're downloading from the provided arguments
target_url = args.target_url

# pull the intended output filename from the provided arguments
output_filename = args.filename

# create appropriate header information for our web page request
headers = {
 'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13597.66.0) ' + \
 'AppleWebKit/537.36 (KHTML, like Gecko) ' + \
 'Chrome/88.0.4324.109 Safari/537.36',
 'From': 'YOUR NAME HERE - youremailaddress@emailprovider.som'
}

# because we're just loading a regular web page, we send a `get` request to the
# URL, along with our informational headers
webpage = requests.get(target_url, headers=headers)

# opening up a local file to save the contents of the web page to
output_file = open(output_filename,"w")

# the web page's code is in the `text` property of the website's response
# so write that to our file
output_file.write(webpage.text)

# close our output file!
output_file.close()
