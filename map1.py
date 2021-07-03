import folium


def create_map_html():
    """
    Function to create a base map with markers using Folium to
    build the Map1.html file
    """

    # Build the map background / tiles
    map = folium.Map(
        location=[38.58, -99.09],
        zoom_start=6,
        tiles="Stamen Terrain"
    )

    # Add map markers
    map.add_child(folium.Marker(
        location=[38.2, -99.1],
        popup="Hi I'm a marker",
        icon=folium.Icon(color='green')
    ))

    map.save("Map1.html")


create_map_html()
