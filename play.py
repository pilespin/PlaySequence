import time
import json
import argparse

# # time, canal, value
# data = [
# [0.5,1,255],
# [0.5,2,255],
# [0.5,3,255],
# [3.5,3,255],
# [3.5,2,255],
# [3.5,1,128],
# [5.5,1,0],
# ]

# # Create json
# j = {}
# j['key'] = 'value'
# j['data'] = data
# json_data = json.dumps(j)
# # pprint (json_data)
# # print(json.dumps(j, indent=4, sort_keys=True))
# with open("json", "w") as f: 
# 	f.write(json_data)


parser = argparse.ArgumentParser()
parser.add_argument('-s','--start', help='Start Time', nargs='?', required=True, const=0.0, type=float)
args = parser.parse_args()

# print(args.start)

with open('json') as f:
	j = json.loads(f.read())
	print('data:', j['data'])

timeStart = time.clock_gettime(0) - args.start
print(timeStart, '+', args.start)

for d in j['data']:
	if d[0] < args.start:
		continue

	timeInterval = time.clock_gettime(0) - timeStart

	timeDest = d[0]
	while (timeInterval <= timeDest):
		# print('Interval', timeInterval)
		time.sleep(0.0001)
		timeInterval = time.clock_gettime(0) - timeStart

	print(time.clock_gettime(0), '	canal', d[1], ':', d[2])
