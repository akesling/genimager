from Settings.Chromosome import Polygon as Settings
import Image, ImageDraw
import random

class Polygon():
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
			
			center = (random.randint(Settings.XMIN, Settings.XMAX), 
						random.randint(Settings.YMIN, Settings.YMAX))
			for i in xrange(random.randint(Settings.PMIN,Settings.PMAX)):
				self.add_point(center)
	
	def __str__(self):
		return "("+ str(self.fill_rgb[0]) + \
				","+ str(self.fill_rgb[1]) + \
				","+ str(self.fill_rgb[2]) + \
				","+ str(self.fill_a) + \
				"),"+ str(self.outline)
	
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
	
	def draw(self, base_layer):
		color_layer = Image.new('RGBA', base_layer.size, self.fill_rgb)
		alpha_mask = Image.new('L', base_layer.size, 0)
		alpha_mask_draw = ImageDraw.Draw(alpha_mask)
		alpha_mask_draw.polygon(self.outline,fill=self.fill_a)
		base_layer = Image.composite(color_layer, base_layer, alpha_mask)
		return base_layer
	
####Mutations####

##Shape alterations##
	def insert_point(self, center=False):
		if center:
			assert type(center) == tuple and len(center) == 2
			XMAX = center[0] + abs(int(Settings.RANGE * \
									(Settings.XMAX - center[0])))
			XMIN = center[0] - abs(int(Settings.RANGE * \
									(Settings.XMIN + center[0])))
			YMAX = center[1] + abs(int(Settings.RANGE * \
									(Settings.YMAX - center[1])))
			YMIN = center[1] - abs(int(Settings.RANGE * \
									(Settings.YMIN + center[1])))
		else:
			XMAX = Settings.XMAX
			XMIN = Settings.XMIN	
			YMAX = Settings.YMAX
			YMIN = Settings.YMIN	
		
		if len(self.outline) < Settings.PMAX:
			self.outline.insert(random.randint(0, len(self.outline)), 
				(random.randint(XMIN, XMAX),
					 random.randint(YMIN, YMAX)))
	
	def add_point(self, center=False):
		if center:
			assert type(center) == tuple and len(center) == 2
			XMAX = center[0] + abs(int(Settings.RANGE * \
									(Settings.XMAX - center[0])))
			XMIN = center[0] - abs(int(Settings.RANGE * \
									(Settings.XMIN + center[0])))
			YMAX = center[1] + abs(int(Settings.RANGE * \
									(Settings.YMAX - center[1])))
			YMIN = center[1] - abs(int(Settings.RANGE * \
									(Settings.YMIN + center[1])))
		else:
			XMAX = Settings.XMAX
			XMIN = Settings.XMIN	
			YMAX = Settings.YMAX
			YMIN = Settings.YMIN	
		
		if len(self.outline) < Settings.PMAX:
			self.outline.append((random.randint(XMIN, XMAX),
				random.randint(YMIN, YMAX)))
	
	def delete_point(self):
		if Settings.PMIN < len(self.outline):
			self.outline.remove(random.choice(self.outline))
	
	def adjust_point(self):
		x_adjust = random.randint(-Settings.distance_adjust,
									Settings.distance_adjust)
		y_adjust = random.randint(-Settings.distance_adjust,
									Settings.distance_adjust)
		
		point_index = random.randint(0, len(self.outline)-1)
		
		self.outline[point_index] = (
			max(Settings.XMIN, min(Settings.XMAX, 
					self.outline[point_index][0] + x_adjust)), 
			max(Settings.YMIN, min(Settings.YMAX, 
					self.outline[point_index][1] + y_adjust)))
	
##Color Alterations##
	def adjust_color(self):
		red_adjust = random.randint(-Settings.color_adjust,
									Settings.color_adjust)
		green_adjust = random.randint(-Settings.color_adjust,
									Settings.color_adjust)
		blue_adjust = random.randint(-Settings.color_adjust,
									Settings.color_adjust)
		
		self.fill_rgb = (max(0, min(255, self.fill_rgb[0] + red_adjust)),
						max(0, min(255, self.fill_rgb[1] + green_adjust)),
						max(0, min(255, self.fill_rgb[2] + blue_adjust)))
		
	
	def adjust_opacity(self):
		alpha_adjust = random.randint(-Settings.alpha_adjust,
										Settings.alpha_adjust)
		self.fill_a = max(0, min(255, self.fill_a + alpha_adjust))
