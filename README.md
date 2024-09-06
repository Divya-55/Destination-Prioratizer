# Destination Prioritizer

*The Destination Prioritizer is a tool that helps users plan their travel route by prioritizing locations based on the shortest driving distance. It integrates with python to provide geolocation data, and Google Maps to calculate driving distances, and plot routes on a map.*

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
3. **Configure Environment Variables**:

    Create a `.env` file in the project root and include the following variables:
    
    ```plaintext
    GOOGLEMAPS_API_KEY=YOUR_GOOGLE_MAPS_API_KEY
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application:**

    ```bash
    python main.py
    ```

6. **Navigate to the generated map file:**

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
  ![map](https://github.com/user-attachments/assets/1a2afb53-c45b-4000-8156-19369118279a)

## Usage

- Run the `main.py` script to start the application.
- Follow the prompts to input locations:
  - Enter the address or plus code and provide a name for each location.
  - Indicate whether you want to return to the starting point after visiting all locations.
- The application will generate an HTML file named `map.html`.
- Open `map.html` in a web browser to view the interactive map with the prioritized route.

## Note

- This app requires a Google Maps API key for geocoding and directions.
- Python will fetch the geolocation of the user.
- Ensure your internet connection is active to fetch geolocation data and plot the route.
- Be aware of Google Maps API usage limits and quotas.

## Acknowledgements

- **Geocoding and Directions**: Google Maps API.
- **Geolocation**: Python.
- **Interactive Maps**: Folium.
- **HTTP Requests**: Requests library.
- **Map Tiles**: CartoDB (OpenStreetMap).

