import folium


def create_map_html(map_start, markers):
    """
    Function to create a base map with markers using Folium to
    build the Map1.html file
    """

    start_location = map_start
    map_markers = markers

    # Build the map background / tiles
    map = folium.Map(
        location=start_location,
        zoom_start=6,
        tiles="Stamen Terrain"
    )

    # Add Folium Feature Group for map layers
    fg = folium.FeatureGroup(name="My Map")

    # Add map markers as a Feature Group layer
    for marker in map_markers:
        fg.add_child(folium.Marker(
            location=marker,
            popup=f'Lat: {marker[0]}, Long: {marker[1]}',
            icon=folium.Icon(color='green')
        ))

    map.add_child(fg)

    # Create the map html file
    map.save("index_test.html")


init_map_coordinates = [38.59, -99.08]
marker_points = [
    [38.9, -99.3],
    [39.2, -98.1],
    [38.6, -99.9],
    [39.5, -98.1],
    [38.4, -98.7]]

create_map_html(init_map_coordinates, marker_points)
