import Image, ImageDraw, ImageChops, ImageStat
import random, copy
from chromosome import Chromosome
class Genome():
	XMAX = 0
	YMAX = 0
	
	def __init__(self):
		self.last_draw = None
		
		self.chromosomes = []
		for i in xrange(1):
			self.add_chromosome()
	
	def __str__(self):
		serial = "<"
		serial += ";".join((str(i) for i in self.chromosomes))
		return serial +">"
	
	def from_string(self, serial):
		self.chromosomes = []
		temp = serial.replace("<", "")
		temp = temp.replace(">", "")
		chromosomes = temp.split(";")	
		
		for chrom in chromosomes:
			new_chrom = Chromosome(True)
			new_chrom.from_string(chrom)
			self.chromosomes.append(new_chrom)
	
	def gene_transfer(self, second):
		second.last_draw = None
		second.chromosomes = []
		for i in self.chromosomes:
			second.chromosomes.append(copy.deepcopy(i))
	
	def mutate(self, rate):
		#Adjust multiple chromosomes per iteration
		#rate is the maximum percentage of chromosomes to adjust
		for i in random.sample(self.chromosomes, random.randint(0, 
				int((len(self.chromosomes)-1)*(rate/100))+1)):
			i.mutate()
		
		#Adjust multiple chromosomes per iteration
		random.choice(self.chromosomes).mutate()
		
		#Polygon position and existence alteration
		decide = random.random()
		if decide < .2:
			move_index = random.randint(0,len(self.chromosomes)-1)
			to_be_moved = self.chromosomes[move_index]
			self.chromosomes.remove(to_be_moved)
			self.chromosomes.append(to_be_moved)
		elif decide < .22:
			self.delete_chromosome()
		elif decide < .24:
			self.add_chromosome()
   
	def delete_chromosome(self):
		if len(self.chromosomes) > 0:
			del self.chromosomes[random.randint(0,len(self.chromosomes)-1)]
   	
	def add_chromosome(self):
		self.chromosomes.append(Chromosome())
	
	def draw(self): 
		base_layer = Image.new('RGBA',(self.XMAX,self.YMAX))
		color_layer = Image.new('RGBA',(self.XMAX, self.YMAX))
		color_layer_draw = ImageDraw.Draw(color_layer)
		for chromosome in self.chromosomes:
			color, opacity, points = chromosome.fill_rgb, \
									 chromosome.fill_a, \
									 chromosome.outline
			color_layer_draw.rectangle((0,0, self.XMAX,self.YMAX), color)
			alpha_mask = Image.new('L',(self.XMAX,self.YMAX), 0)
			alpha_mask_draw = ImageDraw.Draw(alpha_mask)
			alpha_mask_draw.polygon(points,fill=opacity)
			base_layer = Image.composite(color_layer,base_layer,alpha_mask)
		self.last_draw = base_layer
		
		return base_layer
	
	def diff(self, base):
		diffIm = ImageChops.difference(self.draw(), base)
		diffStat = ImageStat.Stat(diffIm)
		difference = sum(diffStat.sum) #stat.sum returns a list of each color sum
		return difference
#		my_pixels = self.draw().load()
#		
#		fitness = 0
#		for y in xrange(self.YMAX):
#			for x in xrange(self.XMAX):
#				c1 = base[x, y]
#				c2 = my_pixels[x, y]
#				
#				del_red = c1[0] - c2[0]
#				del_green = c1[1] - c2[1]
#				del_blue = c1[2] - c2[2]
#				
#				pixel_fitness = del_red*del_red + \
#								del_green*del_green + \
#								del_blue*del_blue
#				fitness += pixel_fitness
#		return fitness
