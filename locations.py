import requests

class LocationService:

    def __init__(self, googlemaps_api_key):
        self.GOOGLEMAPS_API_KEY = googlemaps_api_key

    def get_geolocation_data(self):
        response = requests.get('https://ipinfo.io/')

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            location = data['loc'].split(',')
            my_location = {
                'lat': location[0],
                'lng': location[1]
            }
            return my_location
        else:
            print("Failed to retrieve geolocation data:", response.status_code, response.text)
            return None, None, None


    def get_location(self, plus_code_or_address):
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": plus_code_or_address,
            "key": self.GOOGLEMAPS_API_KEY
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            location_data = data["results"][0]["geometry"]["viewport"]["northeast"]
            return location_data
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

    def user_input(self):
        self.new_address = input("Please Enter the plus code/address of the location: ")
        self.user_choice_loc_name = input("Please enter any name for the location: ")
        self.user_reply = input("Do you want to give another location details (yes/no): ").lower()
        location = self.get_location(self.new_address)
        return location


