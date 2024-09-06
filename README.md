# Destination Prioritizer

*The Destination Prioritizer is a tool that helps users plan their travel route by prioritizing locations based on the shortest driving distance. It integrates with Google Maps to provide geolocation data, calculate driving distances, and plot routes on a map.*

## Description

It helps you plan trips to multiple places more efficiently. Whether you need to shop for clothes, buy groceries, visit friends, or pick up pet food, this tool figures out the best order to visit these places so you travel the shortest distance.

Simply enter your destinations, and the it will create a route that saves time and reduces travel. It can also return you to your starting point if you want.


## Features

- Retrieve and plot geolocation data.
- Prioritize locations based on shortest path.
- Optionally return to the starting point after visiting all locations.
- Generate an interactive map with the prioritized route.

## Technologies Used

- Python
- Google Maps API
- Folium for map plotting

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/destination-prioritizer.git
    cd destination-prioritizer
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use 'venv\Scripts\activate'
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python main.py
    ```

5. **Navigate to the generated map file:**

    Open `map.html` in a web browser to view the interactive map.

## Requirements

- Python 3.x
- Google Maps API key

## File Descriptions

- **main.py**: Main script to run the application.
- **locations.py**: Handles location services and geocoding.
- **map_plotter.py**: Manages map creation and path plotting.
- **prioritize_locations.py**: Contains logic for prioritizing locations based on distance.

## Screenshots

- **Map with Prioritized Route**:
  ![Map](screenshots/map-example.png)

## Usage

- Run the `main.py` script to start the application.
- Follow the prompts to input locations:
  - Enter the address or plus code and provide a name for each location.
  - Indicate whether you want to return to the starting point after visiting all locations.
- The application will generate an HTML file named `map.html`.
- Open `map.html` in a web browser to view the interactive map with the prioritized route.

## Note

- This app requires a Google Maps API key for geolocation and directions.
- Ensure your internet connection is active to fetch geolocation data and plot the route.
- Be aware of Google Maps API usage limits and quotas.

## Acknowledgements

- **Geolocation and Directions**: Google Maps API.
- **Interactive Maps**: Folium.
- **HTTP Requests**: Requests library.
- **Map Tiles**: CartoDB (OpenStreetMap).


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
