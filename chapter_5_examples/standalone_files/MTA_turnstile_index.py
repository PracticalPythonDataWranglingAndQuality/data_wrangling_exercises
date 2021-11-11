# include the requests library in order to get data from the web
import requests

# specify the URL of the web page we're downloading
# this one contains a linked list of all the NYC MTA turnstile data files
# going back to 2010
mta_turnstiles_index_url = "http://web.mta.info/developers/turnstile.html"

# create some header information for our web page request
headers = {
 'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 13597.66.0) ' + \
 'AppleWebKit/537.36 (KHTML, like Gecko) ' + \
 'Chrome/88.0.4324.109 Safari/537.36',
 'From': 'YOUR NAME HERE - youremailaddress@emailprovider.som'
}

# send a `get()` request for the URL, along with our informational headers
mta_web_page = requests.get(mta_turnstiles_index_url, headers=headers)

# open up a writable local file where we can save the contents of the web page
mta_turnstiles_output_file = open("MTA_turnstiles_index.html","w")

# write the `text` web page to our output file
mta_turnstiles_output_file.write(mta_web_page.text)

# close our output file!
mta_turnstiles_output_file.close()
