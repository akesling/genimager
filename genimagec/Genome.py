import Image, ImageDraw, ImageChops, ImageStat
import random, copy
from Settings.Genome import Basic as Settings
from Chromosome import Polygon

class Basic():
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
			new_chrom = Polygon(True)
			new_chrom.from_string(chrom)
			self.chromosomes.append(new_chrom)
	
	def gene_transfer(self, second):
		second.last_draw = None
		second.chromosomes = []
		for i in self.chromosomes:
			second.chromosomes.append(copy.deepcopy(i))
	
	def mutate(self, rate):
		#Polygon z-position and existence alteration
		mutation = random.randint(0,10)
		if mutation == 0:
			self.mutate_position()
		elif mutation <= 5:
			self.mutate_shape()
		elif mutation <= 10:
			self.mutate_color()
#		else:
#			#Adjust one chromosome per iteration
#			random.choice(self.chromosomes).mutate()
#			#Adjust multiple chromosomes per iteration
#			#rate is the maximum percentage of chromosomes to adjust
#			for i in random.sample(self.chromosomes, random.randint(0, 
#					int((len(self.chromosomes)-1)*(rate/100))+1)):
#				i.mutate()
	
##Mutations##
	def mutate_color(self):
		decide = random.randint(0,1)
		if decide == 0:
			random.choice(self.chromosomes).adjust_color()
		else:
			random.choice(self.chromosomes).adjust_opacity()
	
	def mutate_shape(self):
		decide = random.randint(0,2)
		if decide == 0:
			random.choice(self.chromosomes).insert_point()
		elif decide == 1:
			random.choice(self.chromosomes).delete_point()
		else:
			random.choice(self.chromosomes).adjust_point()
	
	def mutate_position(self):
		decide = random.randint(0,2)
		if decide == 0:
			self.swap_chromosome()
		elif decide == 1:
			self.delete_chromosome()
		else:
			self.add_chromosome()
	
##Chromosomal Positioning##
	def swap_chromosome(self, first=False, second=False):
		if len(self.chromosomes) > 1:
			if not (first and second):
				first = random.randint(0,len(self.chromosomes)-1)
				second = random.randint(0,len(self.chromosomes)-1)
			to_swap = self.chromosomes[first]
			self.chromosomes[first] = self.chromosomes[second]
			self.chromosomes[second] = to_swap
   
	def delete_chromosome(self):
		if len(self.chromosomes) > 1:
			del self.chromosomes[random.randint(0,len(self.chromosomes)-1)]
   	
	def add_chromosome(self):
		self.chromosomes.append(Polygon())
	
##Fitness##
	def draw(self): 
		base_layer = Image.new('RGBA',(Settings.XMAX,Settings.YMAX))
		for chromosome in self.chromosomes:
			base_layer = chromosome.draw(base_layer)
		self.last_draw = base_layer
		
		return base_layer
	
	def diff(self, base):
		diffIm = ImageChops.difference(self.draw(), base)
		diffStat = ImageStat.Stat(diffIm)
		difference = sum(diffStat.sum)
		return difference
