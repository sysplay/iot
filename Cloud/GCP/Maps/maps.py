# importing the requests library 
import requests 

# api-endpoint 
URL = "https://maps.googleapis.com/maps/api/geocode/json"

# api key
key = "gcp_api_key"

# location given here 
location = "SysPlay eLearning Academy for You"
#location = "eSrijan Innovations Private Limited"

# defining a params dict for the parameters to be sent to the API 
PARAMS = {'key': key, 'address': location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

print(r)

# extracting data in json format 
data = r.json() 

print(data)

# extracting latitude, longitude and formatted address  
# of the first matching location 
latitude = data['results'][0]['geometry']['location']['lat'] 
longitude = data['results'][0]['geometry']['location']['lng'] 
formatted_address = data['results'][0]['formatted_address'] 

# printing the output 
print("Latitude: %s\nLongitude: %s\nFormatted Address: %s"
	%(latitude, longitude, formatted_address)) 
