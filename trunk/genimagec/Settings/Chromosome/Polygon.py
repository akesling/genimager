"""
Settings for the Polygon chromosome.
"""


##Positioning Settings##
#Image's height and width
XMAX = 0
YMAX = 0
#Range box around center of new polygon in which points may be placed
RANGE = 1
#Extra distance beyond image border in which points may be placed
EDGE = 50
#Max/Min number of points per polygon
PMAX = 10
PMIN =3
#Maximum distance (in pixels) allowable to adjust a point
distance_adjust = 20


##Color/Opacity Settings##
#Maximum allowable amounts by which to adjust color/opacity
color_adjust = 20
alpha_adjust = 20


##Mutation Settings##
#Mutators to use (available listed below):
#	insert_point
#	delete_point
#	adjust_point
#	adjust_color
#	adjust_opacity
MUTATORS = ("insert_point", \
			"delete_point", \
			"adjust_point", \
			"adjust_color", \
			"adjust_opacity")

##Setters##
def set_size (XMAX, YMAX):
   #Point max & min
   globals()["XMAX"] = XMAX + EDGE
   globals()["YMAX"] = YMAX + EDGE
   globals()["XMIN"] = -EDGE
   globals()["YMIN"] = -EDGE

def set_range (range):
   globals()["RANGE"] = range/200.
