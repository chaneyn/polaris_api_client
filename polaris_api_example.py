import polaris_api_client
minlon = -90.202
minlat = 43.201
maxlon = -90.201
maxlat = 43.202
var = 'sand'
layer = '0_5'
data = polaris_api_client.get_data(minlat,maxlat,minlon,maxlon,var,layer)
print(data)
