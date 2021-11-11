# import the encoded key from our credentials file
from Twitter_credentials import auth_ready_key

# include the requests library in order to get data from the web
import requests

# specify the Twitter endpoint that we'll use to retrieve
# our access token or "bearer" token
auth_url = 'https://api.twitter.com/oauth2/token'

# add our `auth_ready_key` to a template `dict` object provided
# in the Twitter API documentation
auth_headers = {
 'Authorization': 'Basic '+auth_ready_key,
 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

# another `dict` describes what we're asking for
auth_data = {
 'grant_type': 'client_credentials'
}

# make our complete request to the authorization endpoint, and store
# the results in the `auth_resp` variable
auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# pull the access token out of the json-formatted data
# that the authorization endpoint sent back to us
access_token = auth_resp.json()['access_token']

# now that we have an access/bearer token, we're ready to request some data!
# we'll create a new dict that includes this token
search_headers = {
 'Authorization': 'Bearer ' + access_token
}

# this is the Twitter search API endpoint for version 1.1 of the API
search_url = 'https://api.twitter.com/1.1/search/tweets.json'

# create a new dict that includes our search query parameters
search_params = {
 'q': 'Python',
 'result_type': 'recent',
 'count': 4
}

# send our data request and store the results in `search_resp`
search_resp = requests.get(search_url, headers=search_headers, params=search_params)

# parse the response into a JSON object
Twitter_data = search_resp.json()

# open an output file where we can save the results
Twitter_output_file = open("Twitter_search_results.json", "w")

# write the returned Twitter data to our output file
Twitter_output_file.write(str(Twitter_data))

# close the output file
Twitter_output_file.close()

# loop through our results and print the text of the Twitter status
for a_Tweet in Twitter_data['statuses']:
 print(a_Tweet['text'] + '\n')
