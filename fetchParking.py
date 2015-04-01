import overpass
api = overpass.API()


elements = ['node', 'way']
bbox = "(45.904105344941705,-66.80271148681639,45.98694349643096,-66.5311431884765)"
item = '["amenity"="parking"]'

api_query = []
for element in elements:
    query = element + bbox + item
