import locations
import map_plotter
import prioritize_locations
import os
from dotenv import find_dotenv, load_dotenv

# find .env automatically until it's found
dotenv_path = find_dotenv()
# load the entries as environmental variables
load_dotenv(dotenv_path)

GOOGLEMAPS_API_KEY = os.getenv('API_KEY')

if __name__ == "__main__":
    LOCATIONS = {}

    locations_obj = locations.LocationService(GOOGLEMAPS_API_KEY)
    prioritize_locations_obj = prioritize_locations.PrioritizeLocations()

    my_location = locations_obj.get_geolocation_data()
    LOCATIONS["My_location"] = [my_location["lat"], my_location["lng"]]

    locations_obj.user_reply = "yes"
    while locations_obj.user_reply != "no":
        if locations_obj.user_reply == "yes":
            location = locations_obj.user_input()
            LOCATIONS[locations_obj.user_choice_loc_name.replace(" ", "_")] = [location["lat"], location["lng"]]
        else:
            print("please enter 'yes' or 'no' only")
            locations_obj.user_reply = input("Do you want to give another location details (yes/no): ").lower()
    go_back_to_starting_point_or_not = input("Do you want to go back to the starting point after your last destination(yes/no)? ")
    print(LOCATIONS)

    map_plotter_obj = map_plotter.MapPlotter(GOOGLEMAPS_API_KEY, LOCATIONS)
    prioritized_loc_names = prioritize_locations_obj.prioritize_given_locations(LOCATIONS, map_plotter_obj, go_back_to_starting_point_or_not)

    map_plotter_obj.add_html_content(prioritized_loc_names)
    map_plotter_obj.save_map()



