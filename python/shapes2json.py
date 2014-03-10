import re
import numpy as np
infile = "shapes.txt"
filt = re.compile(r'^"?([^"]*)"?$')
converter = lambda x: filt.match(x.strip()).group(1)
data = np.recfromcsv(infile, delimiter=',')
shapes = np.array(map(int, [converter(x) for x in data["shape_id"]]))
lats = np.array(map(float, [converter(x) for x in data["shape_pt_lat"]]))
lons = np.array(map(float, [converter(x) for x in data["shape_pt_lon"]]))
idx = np.where(shapes == 10003553)
print "{%s:" % (10003553),
for la,lon in zip(lats[idx], lons[idx]): print "[%f,%f]," % (la,lon),
print "}"

#import matplotlib.pyplot as plt
#idx = np.where(shapes == 10003553)
#plt.plot(lats[idx], lons[idx])
#plt.show()