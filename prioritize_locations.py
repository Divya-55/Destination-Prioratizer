class PrioritizeLocations:

    def prioritize_given_locations(self, locations, map_plotter, go_back_to_starting_point_or_not):
        prioritized_loc_names = []
        locations_names = list(locations.keys())
        first_location_name = locations_names[0]
        copied_locations = locations_names.copy()
        curr_loc_name = locations_names[0]
        next_loc_name = "unknown"
        while copied_locations:
            min_distance = float("inf")  # this means floating value of infinite
            copied_locations.remove(
                curr_loc_name)  # del copied_locations[start_location] # works only for dictionaries due to key value not for lists
            for loc_name in copied_locations:
                path_details = map_plotter.get_shortest_path_details(tuple(locations[curr_loc_name]), tuple(locations[loc_name]))
                distance = path_details["distance"]
                if min_distance > distance:
                    min_distance = distance
                    next_loc_name = loc_name

            prioritized_loc_names.append(curr_loc_name)
            if len(locations_names) > 2:
                if copied_locations:
                    map_plotter.draw_path(curr_loc_name, next_loc_name, prioritized_loc_names, map_plotter.generate_random_color())
                elif go_back_to_starting_point_or_not == "yes":
                    map_plotter.draw_path(curr_loc_name, first_location_name, prioritized_loc_names, map_plotter.generate_random_color())
            else:
                map_plotter.draw_path(curr_loc_name, next_loc_name, prioritized_loc_names, map_plotter.generate_random_color())
                if go_back_to_starting_point_or_not == "yes":
                    map_plotter.draw_path(curr_loc_name, first_location_name, prioritized_loc_names, map_plotter.generate_random_color())

            curr_loc_name = next_loc_name
        return prioritized_loc_names
