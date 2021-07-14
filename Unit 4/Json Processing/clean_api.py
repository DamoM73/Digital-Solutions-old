import requests
import json

def jprint(obj):
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))
    else:
        print(obj.status_code, "error in retrieving API")

# ---- MAIN PROGRAM -----
# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")
sites_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/sites")
bookings_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/bookings")

jprint(bookings_data)