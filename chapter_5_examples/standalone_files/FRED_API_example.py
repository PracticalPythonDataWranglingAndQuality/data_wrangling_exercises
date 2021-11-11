# import the requests library, which let's us write Python that acts like
# a web browser through code
import requests

# we can import our API key by first giving Python the name of our credentials
# file, and then telling it the variable to import
from FRED_credentials import my_api_key

# specify the FRED endpoint we want to use
FRED_endpoint = "https://api.stlouisfed.org/fred/series/observations?"

# also specify the query parameters and their values
FRED_parameters = "series_id=U6RATE&file_type=json"

# construct the complete URL for our API request, adding our API key to the end
complete_data_URL = FRED_endpoint + FRED_parameters +"&api_key="+my_api_key

# open a new, writable file with our chosen filename
FRED_output_file = open("FRED_API_data.json","w")

# use the requests library's "get" recipe to access the contents of our
# target URL and store it in a our `FRED_data` variable
FRED_data = requests.get(complete_data_URL)

# the requests library's "get" function has put the contents of the webpage
# in a property "text", which we'll write directly to our FRED_output_file
# using the built-in "write" method
FRED_output_file.write(FRED_data.text)

# close our FRED_output_file
FRED_output_file.close()
