import folium
map = folium.Map(location=[41.766159756592785, -87.75215891267531], zoom_start=10, tiles="Stamen Terrain") 

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[41.8, -87.8],[41.9, -87.9]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I'm a Marker", icon=folium.Icon(color='green')))


map.add_child(fg)

map.save("Map1.html")