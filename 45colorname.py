import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

P = [R, G, B]
min = 3000

with open(colorfile) as fp:
	for line in fp:
		line = line.split()
		color_values = line[2].split(',')
		Q = []
		for value in color_values: Q.append(int(value))
		if dtc(P, Q) < min:
			min = dtc(P,Q)
			color = line[0]
print(color)
			