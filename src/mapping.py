'''
Jayati Samar
Last edited: 08/13/2024
CS6620: Cloud Computing - Final Project
Objective: This file creates a simple folium map
'''
import folium


# Import data
loci = [{'location':[43.6575, -70.2603],
		 'location_name':"Portland ME",
		 'current_pressure': 29.6,
		 'pressure_variation': -.02},
      {'location':[43.6764, -70.3674],
       'location_name':"Westbrook ME",
       'current_pressure': 29.8,
       'pressure_variation': -.04},
      {'location':[43.7890, -70.4086],
       'location_name':"Windham ME",
       'current_pressure': 30.2,
       'pressure_variation': 0},
      {'location':[43.8217, -69.8133],
       'location_name':"Phippsburg ME",
       'current_pressure': 30.0,
       'pressure_variation': 0.06},
      {'location':[44.0995, -70.2157],
       'location_name':"Lewiston ME",
       'current_pressure': "N/A",
       'pressure_variation': "N/A"}
        ]


# Add extra data points for the map markers
for loc in loci:
	# Add logic to determine what the current barometric pressure is
	if loc['current_pressure'] == "N/A":
		loc['pressure_class'] = "no data"	
	elif loc['current_pressure'] >= 30.2:
		loc['pressure_class'] = 'high'
	elif loc['current_pressure'] < 29.8:
		loc['pressure_class'] = "low"
	else:
		loc['pressure_class'] = 'normal'
		
    # Add logic for 'color' key based on 'pressure_variation'
	if loc['pressure_variation'] == "N/A":
		loc['color'] = "gray"
	elif abs(loc['pressure_variation']) >= 0.06:
		loc['color'] = "red"
	elif 0.03 <= abs(loc['pressure_variation']) < 0.06:
		loc['color'] = "orange"
	else:
		loc['color'] = "green"


#min_long, max_long = 42.75, 47.5
#min_lat,max_lat = -71.25, -66.75

# Create a map centered around a specific location (Portland, ME for now)
m = folium.Map(max_bounds=True,
			   location=[43.6575, -70.2603],
			   control_scale=True, 
			   zoom_start=12,
#			   min_lat = min_lat,
#			   min_long = min_long,
#			   max_lat = max_lat,
#			   max_long = max_long
               )


# Add markers based on the data in loci
for loc in loci:
    folium.Marker(
        location=loc['location'], 
        tooltip=loc['location_name'],
        popup=folium.Popup(
            f"{loc['location_name']} | Current Pressure: {loc['current_pressure']} inHg | Pressure Variation: {loc['pressure_variation']}",
            parse_html=True
        ),
        icon=folium.Icon(color=loc['color'])
    ).add_to(m)

# Save the map to an HTML file
m.save('templates/map.html')