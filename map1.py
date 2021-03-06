import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1500:
        return 'green'
    elif 1500 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[38.58,-99.09],zoom_start=5, tiles = "Stamen Terrain")



#feature group
fg = folium.FeatureGroup(name="My Map")


for lt, ln, el in zip(lat, lon,elev):
    iframe = folium.IFrame(html=html % str(el),width=200,height=100)
    fg.add_child(folium.Marker(location=[lt,ln], popup=folium.Popup(iframe), icon = folium.Icon(color=color_producer(el))))
    

fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function = lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 1000000 else 'orange' if 100000000 <= x['properties']
['POP2005']<20000000 else 'red'}))

map.add_child(fg)


map.save("Map1.html")
