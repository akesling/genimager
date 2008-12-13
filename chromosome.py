import random
class Chromosome():
	def __init__(self, XMAX, YMAX):
		#Point max & min
		self.PMAX = 10
		self.PMIN = 3
		
		border = 50
		self.XMAX = XMAX + border
		self.YMAX = YMAX + border
		self.XMIN = -border
		self.YMIN = -border
		
		self.outline = []
		self.fill_rgb = (random.randint(0,255), random.randint(0,255), 
			random.randint(0,255))
		#Opacity can evolve, but start is fixed
		self.fill_a = 10 #random.randint(0, 255)
		
		for i in xrange(random.randint(self.PMIN,self.PMAX)):
			self.outline.append((random.randint(self.XMIN, self.XMAX), 
				random.randint(self.YMIN, self.YMAX)))
	
	def insert(self):
		if len(self.outline) < self.PMAX:
			self.outline.insert(random.randint(0, len(self.outline)), 
				(random.randint(self.XMIN, self.XMAX),
					 random.randint(self.YMIN, self.YMAX)))
	
	def delete(self):
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
	
	def __str__(self):
		return "("+ str(self.fill_rgb[0]) + \
				","+ str(self.fill_rgb[1]) + \
				","+ str(self.fill_rgb[2]) + \
				","+ str(self.fill_a) + \
				")<"+ str(self.outline) +">"
