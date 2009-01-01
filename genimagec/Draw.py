import math
def pixel(old, new):
	if len(new) == 4:
		opacity = new[3]/255.
		return (int(old[0]*(1-opacity) + new[0]*opacity + 0.5), 
				int(old[1]*(1-opacity) + new[1]*opacity + 0.5), 
				int(old[2]*(1-opacity) + new[2]*opacity + 0.5))

	elif len(new) == 3:
		return new

def line(base, color, start, end):
	#Equation of a line: y=((y1-y2)/(x1-x2))*(x-x1)+y1
	#y = mx + b
	rise = float(start[1] - end[1])
	run = float(start[0] - end[0])
	if run: slope = rise/run
	else: slope = None
	
	x = start[0]
	y = start[1]
	if slope == None:
		for y in xrange(start[1], end[1]):
			old = base[x,y]
			base[x,y] = pixel(old, color)
	elif abs(slope) < 1:
		if run < 0: dx = 1
		else: dx = -1
		
		#Draw start point
		old = base[x,y]
		base[x,y] = pixel(old, color)
		
		intercept = y - slope*x
		while x != end[0]:
			x += dx
			y = int(slope*x + intercept + 0.5)
			old = base[x,y]
			base[x,y] = pixel(old, color)
	else:
		if rise < 0: dy = 1
		else: dy = -1
		
		#Draw start point
		old = base[x,y]
		base[x,y] = pixel(old, color)
		
		intercept = x - y/slope
		while y != end[1]:
			y += dy
			x = int(y/slope + intercept + 0.5)
			old = base[x,y]
			base[x,y] = pixel(old, color)
