import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    lat_column = header_row.index('latitude')
    lon_column = header_row.index('longitude')
    bright_column = header_row.index('brightness')


    # Get brightness, lat and lon from this file.
    brightness_data, lats, lons = [], [], []
    counter = 0

    for row in reader:
        brightness_data.append(float(row[bright_column]))
        lats.append(float(row[lat_column]))
        lons.append(float(row[lon_column]))
        counter += 1

    print(f"I read {counter} lines")

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bright/30 for bright in brightness_data],
        'color': brightness_data,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'}
    },
}]
my_layout = Layout(title='World Fires for 1 Day')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_fires.html')
