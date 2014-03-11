import re, sys
import numpy as np
infile = sys.argv[1]
filt = re.compile(r'^"?([^"]*)"?$')
converter = lambda x: filt.match(x.strip()).group(1)
data = np.recfromcsv(infile, delimiter=',')
shapes = np.array(map(int, [converter(x) for x in data["shape_id"]]))
lats = np.array(map(float, [converter(x) for x in data["shape_pt_lat"]]))
lons = np.array(map(float, [converter(x) for x in data["shape_pt_lon"]]))
idx = np.where(shapes == 41545540)[0]

if 0:
	print '{"%s":' % (41545540),
	for la,lon in zip(lats[idx], lons[idx]): print "[%f,%f]," % (la,lon),
	print "}"
else:
	print "["
	for i in idx:
		print "{"
		print '    name: "pt%d",' % (i)
		print '    lng: %f,' % (lons[i])
		print '    lat: %f,' % (lats[i])
		print ' }, ',
	print "]"