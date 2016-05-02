import random
import math
import time
a = []
for baz in range(0,100):
	a.append(math.trunc(random.random() * 10000))
start = time.clock()
for foo in reversed(range(0, len(a))):
	for bar in range(0, foo):
		if(a[bar] > a[bar+1]):
			(a[bar], a[bar+1]) = (a[bar+1], a[bar])
print(a)
print("st:" + str(start) + " end: " + str(time.clock()))