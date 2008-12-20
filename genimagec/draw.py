import math
def pixel(old, new):
	if len(new) == 4:
		opacity = new[3]/255
		return int(old*(1-opacity) + new*opacity + 0.5)
	if len(new) == 3:
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
		
		intercept = y - slope*x
		while x != end[0]:
			old = base[x,y]
			base[x,y] = pixel(old, color)
			x += dx
			y = int(slope*x + intercept)
	else:
		if rise < 0: dy = 1
		else: dy = -1
		
		intercept = x - slope*y
		while y != end[1]:
			old = base[x,y]
			base[x,y] = pixel(old, color)
			y += dy
			x = int(y/slope + intercept)
