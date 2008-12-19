import Image, ImageDraw
import random
class Chromosome():
	XMAX = 0
	YMAX = 0
	RANGE = 1
	EDGE = 50
	PMAX = 10
	PMIN = 3
	MUTATORS = ("insert_point", \
				"delete_point", \
				"adjust_point", \
				"adjust_color", \
				"adjust_opacity")
	#Adjustment settings
	color_adjust = 20
	alpha_adjust = 20
	distance_adjust = 20
	
	def __init__(self, blank=False):
		self.outline = []
		
		#If just needing an empty Chromosome
		if blank:
			self.fill_rgb = 0
			self.fill_a = 0
		else:
			self.fill_rgb = (random.randint(0,255), random.randint(0,255), 
				random.randint(0,255))
			#Opacity can evolve, but start is fixed
			self.fill_a = random.randint(10, 20)
			
			center = (random.randint(self.XMIN, self.XMAX), 
						random.randint(self.YMIN, self.YMAX))
			for i in xrange(random.randint(self.PMIN,self.PMAX)):
				self.add_point(center)
	
	def __str__(self):
		return "("+ str(self.fill_rgb[0]) + \
				","+ str(self.fill_rgb[1]) + \
				","+ str(self.fill_rgb[2]) + \
				","+ str(self.fill_a) + \
				"),"+ str(self.outline)
	
	@classmethod
	def set_size(self, XMAX, YMAX):
		#Point max & min
		self.XMAX = XMAX + self.EDGE
		self.YMAX = YMAX + self.EDGE
		self.XMIN = -self.EDGE
		self.YMIN = -self.EDGE
	
	@classmethod
	def set_range(self, range):
		self.RANGE = range/200.
	
	def from_string(self, serial):
		self.outline = []
		temp = serial.replace("(", "")
		temp = temp.replace(")", "")
		temp = temp.replace("[", "")
		temp = temp.replace("]", "")
		temp = temp.replace(" ", "")
		intermediate = temp.split(",")
		
		self.fill_rgb = tuple((int(i) for i in intermediate[0:3]))
		self.fill_a = int(intermediate[3])
		self.outline = zip((int(i) for i in intermediate[4::2]), 
							(int(i) for i in intermediate[5::2]))
	
	def mutate(self):
		eval("self."+ random.choice(self.MUTATORS) +"()")
	
	def draw(self, base):
		color_layer = Image.new('RGBA', base.size, self.fill_rgb)
		alpha_mask = Image.new('L', base.size, 0)
		alpha_mask_draw = ImageDraw.Draw(alpha_mask)
		alpha_mask_draw.polygon(self.outline,fill=self.fill_a)
		base_layer = Image.composite(color_layer, base_layer, alpha_mask)
	
####Mutations####

##Shape alterations##
	def insert_point(self, center=False):
		if center:
			assert type(center) == tuple and len(center) == 2
			XMAX = center[0] + abs(int(self.RANGE * (self.XMAX - center[0])))
			XMIN = center[0] - abs(int(self.RANGE * (self.XMIN + center[0])))
			YMAX = center[1] + abs(int(self.RANGE * (self.YMAX - center[1])))
			YMIN = center[1] - abs(int(self.RANGE * (self.YMIN + center[1])))
		else:
			XMAX = self.XMAX
			XMIN = self.XMIN	
			YMAX = self.YMAX
			YMIN = self.YMIN	
		
		if len(self.outline) < self.PMAX:
			self.outline.insert(random.randint(0, len(self.outline)), 
				(random.randint(XMIN, XMAX),
					 random.randint(YMIN, YMAX)))
	
	def add_point(self, center=False):
		if center:
			assert type(center) == tuple and len(center) == 2
			XMAX = center[0] + abs(int(self.RANGE * (self.XMAX - center[0])))
			XMIN = center[0] - abs(int(self.RANGE * (self.XMIN + center[0])))
			YMAX = center[1] + abs(int(self.RANGE * (self.YMAX - center[1])))
			YMIN = center[1] - abs(int(self.RANGE * (self.YMIN + center[1])))
		else:
			XMAX = self.XMAX
			XMIN = self.XMIN	
			YMAX = self.YMAX
			YMIN = self.YMIN	
		
		if len(self.outline) < self.PMAX:
			self.outline.append((random.randint(XMIN, XMAX),
				random.randint(YMIN, YMAX)))
	
	def delete_point(self):
		if self.PMIN < len(self.outline):
			self.outline.remove(random.choice(self.outline))
	
	def adjust_point(self):
		x_adjust = random.randint(-self.distance_adjust,self.distance_adjust)
		y_adjust = random.randint(-self.distance_adjust,self.distance_adjust)
		
		point_index = random.randint(0, len(self.outline)-1)
		
		self.outline[point_index] = (
			max(self.XMIN, min(self.XMAX, 
					self.outline[point_index][0] + x_adjust)), 
			max(self.YMIN, min(self.YMAX, 
					self.outline[point_index][1] + y_adjust)))
	
##Color Alterations##
	def adjust_color(self):
		red_adjust = random.randint(-self.color_adjust,self.color_adjust)
		green_adjust = random.randint(-self.color_adjust,self.color_adjust)
		blue_adjust = random.randint(-self.color_adjust,self.color_adjust)
		
		self.fill_rgb = (max(0, min(255, self.fill_rgb[0] + red_adjust)),
						max(0, min(255, self.fill_rgb[1] + green_adjust)),
						max(0, min(255, self.fill_rgb[2] + blue_adjust)))
		
	
	def adjust_opacity(self):
		alpha_adjust = random.randint(-self.alpha_adjust,self.alpha_adjust)
		self.fill_a = max(0, min(255, self.fill_a + alpha_adjust))
