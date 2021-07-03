import folium
import pandas


def create_map_html(map_start, data_file):
    """
    Function to create a base map with markers using Folium to
    build the Map1.html file
    """
    start_location = map_start

    # Import data_file as a Pandas DataFrame
    df = pandas.read_csv(f'{data_file}')
    name = list(df["NAME"])
    loc = list(df["LOCATION"])
    elev = list(df["ELEV"])
    status = list(df["STATUS"])
    type = list(df["TYPE"])
    lat = list(df["LAT"])
    lon = list(df["LON"])

    # Build the map background / tiles
    map = folium.Map(
        location=start_location,
        zoom_start=6,
        tiles="Stamen Terrain"
    )

    # Add Folium Feature Group for map layers
    fg = folium.FeatureGroup(name="My Map")

    # Add map markers as a Feature Group layer
    for nm, lc, el, st, tp, lt, ln in zip(
            name, loc, elev, status, type, lat, lon):
        
        # Build iFrame with Marker data
        iframe = folium.IFrame(
                '<h4>' + str(nm) + '</h4>' +
                'Location: ' + str(lc) + '<br>' +
                'Elev.: ' + str(el) + ' m<br>' +
                'Status: ' + str(st) + '<br>' +
                'Type: ' + str(tp) + '<br>' +
                'Lat: ' + str(lt) + '<br>' +
                'Long: ' + str(ln)
            )
        
        # Build the Marker layer
        fg.add_child(folium.Marker(
            location=[lt, ln],
            popup=folium.Popup(
                iframe,
                min_width=250,
                max_width=300
            ),
            icon=folium.Icon(color='red', icon='info-sign')
        ))

    map.add_child(fg)

    # Create the map html file
    map.save("index.html")


init_map_coordinates = [41.80229638979926, -114.08502404620313]
data_file = "Volcanoes.txt"

create_map_html(init_map_coordinates, data_file)
