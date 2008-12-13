import random
class Chromosome():
	RANGE = 0
	XMAX = 0
	YMAX = 0
	EDGE = 50
	PMAX = 10
	PMIN = 3
	
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
			self.fill_a = 10 #random.randint(0, 255)
			
			for i in xrange(random.randint(self.PMIN,self.PMAX)):
				self.add_point()
	
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
		self.RANGE = 100./range
	
	def from_string(self, serial):
		self.outline = []
		temp = serial.replace("(", "")
		temp = temp.replace(")", "")
		temp = temp.replace("[", "")
		temp = temp.replace("]", "")
		temp = temp.replace(" ", "")
		intermediate = temp.split(",")
		
		self.fill_rgb = tuple(intermediate[0:3])
		self.fill_a = intermediate[3]
		self.outline = zip((int(i) for i in intermediate[4::2]), 
							(int(i) for i in intermediate[5::2]))
	
	def mutate(self):
		random.choice(self.MUTATORS)()
	
#Mutations
	def insert_point(self):
		XMAX = int(self.RANGE * self.XMAX)
		XMIN = int(self.RANGE * self.XMIN)
		YMAX = int(self.RANGE * self.YMAX)
		YMIN = int(self.RANGE * self.YMIN)
		
		if len(self.outline) < self.PMAX:
			self.outline.insert(random.randint(0, len(self.outline)), 
				(random.randint(XMIN, XMAX),
					 random.randint(YMIN, YMAX)))
	
	def add_point(self):
		XMAX = int(self.RANGE * self.XMAX)
		XMIN = int(self.RANGE * self.XMIN)
		YMAX = int(self.RANGE * self.YMAX)
		YMIN = int(self.RANGE * self.YMIN)
		
		if len(self.outline) < self.PMAX:
			self.outline.append((random.randint(XMIN, XMAX),
				random.randint(YMIN, YMAX)))
	
	def delete_point(self):
		if self.PMIN < len(self.outline):
			self.outline.remove(random.choice(self.outline))
	
	def adjust_color(self):
		color_adjust = 20
		
		red_adjust, green_adjust, blue_adjust, alpha_adjust = 0,0,0,0
		
		decide = random.random()
		if decide < .3:
			red_adjust = random.randint(-color_adjust,color_adjust)
		elif decide < .6:
			green_adjust = random.randint(-color_adjust,color_adjust)
		elif decide < .9:
			blue_adjust = random.randint(-color_adjust,color_adjust)
		
		if decide <= .5:
			alpha_adjust = random.randint(-10, 10)
		
		self.fill_rgb = (max(0, min(255, self.fill_rgb[0] + red_adjust)),
						max(0, min(255, self.fill_rgb[1] + green_adjust)),
						max(0, min(255, self.fill_rgb[2] + blue_adjust)))
		
		self.fill_a = max(0, min(255, self.fill_a + alpha_adjust))
	
	def adjust_point(self):
		distance_adjust = 20
		x_adjust = random.randint(-distance_adjust,distance_adjust)
		y_adjust = random.randint(-distance_adjust,distance_adjust)
		
		point_index = random.randint(0, len(self.outline)-1)
		
		self.outline[point_index] = (
			max(self.XMIN, min(self.XMAX, 
					self.outline[point_index][0] + x_adjust)), 
			max(self.YMIN, min(self.YMAX, 
					self.outline[point_index][1] + y_adjust)))
	
	MUTATORS = (add_point, \
				insert_point, \
				delete_point, \
				adjust_point, \
				adjust_color)
