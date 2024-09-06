from datetime import datetime
import random
import folium
import googlemaps


class MapPlotter:

    def __init__(self, googlemaps_api_key, locations):
        self.gmaps = googlemaps.Client(key=googlemaps_api_key)
        self.locations = locations
        self.first_loc_name = list(self.locations.keys())[0]
        self.map = self.create_map()

    def create_map(self):
        first_location = list(self.locations.values())[0]
        return folium.Map(location=first_location, tiles="cartodbpositron", zoom_start=10)

    def generate_random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF) + 1000)

    def get_shortest_path_details(self, start_coords, end_coords, mode='driving'):
        # Get directions between start and end coordinates
        try:
            directions_result = self.gmaps.directions(
                origin=start_coords,
                destination=end_coords,
                mode=mode,
                departure_time=datetime.now()
            )
            # Check if there are any routes
            if not directions_result:
                print("No routes found")
                return None
            # Get the shortest route by distance
            shortest_route = min(directions_result, key=lambda x: x['legs'][0]['distance']['value'])
            # Extract the polyline from the route
            polyline = shortest_route['overview_polyline']['points']
            # Decode the polyline into a list of coordinates
            path_coordinates = googlemaps.convert.decode_polyline(polyline)  # Extract distance and duration
            # get distance and duration
            distance = shortest_route['legs'][0]['distance']['value']
            distance_in_text = shortest_route['legs'][0]['distance']['text']
            duration = shortest_route['legs'][0]['duration']['text']
            return {
                'distance': distance,
                'distance_in_text': distance_in_text,
                'duration': duration,
                'path_coordinates': path_coordinates
            }
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


    def draw_path(self, start_loc_name, end_loc_name, prioritized_loc_names, color_of_the_path):

        if start_loc_name == self.first_loc_name:
            folium.Marker(
                location=list(self.locations[start_loc_name]),
                popup=start_loc_name,
                tooltip=start_loc_name,
                icon=folium.Icon(color='blue', icon="car", prefix="fa")
            ).add_to(self.map)
        else:
            folium.Marker(
                location=list(self.locations[start_loc_name]),
                popup=start_loc_name,
                tooltip=start_loc_name,
                icon=folium.Icon(color='red', icon="circle", prefix="fa")
            ).add_to(self.map)
            folium.Marker(
                location=list(self.locations[start_loc_name]),
                popup=start_loc_name,
                tooltip=start_loc_name,
                icon=folium.DivIcon(
                    html=f'<div style="font-size: 12pt; color: black; background-color: transparent; width: 30px; height: 30px; text-align: center; line-height: 30px; ">{prioritized_loc_names.index(start_loc_name)}</div>',
                    icon_size=(30, 30), icon_anchor=(14, 40))
            ).add_to(self.map)

        path_details = self.get_shortest_path_details(tuple(self.locations[start_loc_name]), tuple(self.locations[end_loc_name]),
                                                 mode='driving')  # dictionary or tuple of coords only # profile--->by car or walk or etc
        path_coordinates = path_details["path_coordinates"]
        if not path_coordinates:
            print("Could not retrieve path coordinates.")

        folium.PolyLine(locations=[[coordinates["lat"], coordinates["lng"]] for coordinates in path_coordinates],
                        color=color_of_the_path,
                        tooltip=f"Distance: {path_details['distance_in_text']}(s) & Time: {path_details['duration']}",
                        max_width=100,
                        weight=5).add_to(self.map)


    def add_html_content(self, prioritized_loc_names):
        html_content = """
        <div style="position: fixed; 
             top: 70px; left: 150px;
             padding: 30px; 
             line-height: 30px;
             background-color:pink; border:2px solid grey;z-index: 900;">
            <div style='font-size: 18px';>
                <div><u><i>Destination Sequence</i></u></div>
                {}
            </div>
        </div>
        """.format("".join(f"<div>{i}. {prioritized_loc_names[i].title().replace('_', ' ')}</div>" for i in
                           range(1, len(prioritized_loc_names))))

        self.map.get_root().html.add_child(folium.Element(html_content))

    def save_map(self, file_name="map.html"):
        self.map.save(file_name)

