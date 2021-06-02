import urllib3
import numpy as np
import json
http = urllib3.PoolManager()

def get_data(minlat,maxlat,minlon,maxlon,var,layer):
 #Extract box
 string = '%.6f$%.6f$%.6f$%6f$%s$%s' % (minlon, minlat, maxlon, maxlat, layer, var)
 r = http.request('GET', 'http://152.3.67.2:8000/polaris/%s' % string)
 data = json.loads(r.data)
 for var in data:
  data[var] = np.array(data[var])
 return data
