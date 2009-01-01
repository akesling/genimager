import Settings
from Chromosome import Polygon
from Genome import Basic 
import Image, ImageDraw, ImageChops, ImageStat
import random, copy
random.seed()

run_id = str(random.randint(0,9999999999))
###########################################
filename = "seeds/Captain_Jack_Sparrow.jpg"
#serial = "genomes/runs/3074301915_1661.gen"
###########################################
base = Image.open(filename)
base = base.convert('RGBA')
base_pix = base.load()
#base = ImageChops.invert(base) #
Xmax, Ymax = base.size

Settings.Genome.Basic.XMAX = Xmax
Settings.Genome.Basic.YMAX = Ymax
Settings.Chromosome.Polygon.set_size(Xmax, Ymax)
Settings.Chromosome.Polygon.set_range(100)

canon = Basic()
mutant = Basic()
grower = Image.new('RGBA',base.size) # Image from DNA

###MAIN###
#Load .gen file and set difference appropriately
if locals().has_key("serial"):
	canon.from_string(open(serial, "r").read())
	difference = canon.diff(base)
else:
	difference = 5000000000000
percent_diff = 100
mutation_rate = 100
counter = 0
since_change = 0
since_write = 0
base.show()
print "Run Number:", run_id + "\n" + \
	"Iter. |", "Fitness |", "% Similarity |", "Since Last Evolve |", \
	"Polygons |", "Alg. Fitness"
try:
	while True:
		counter += 1
		since_change += 1
		if (counter % 50 == 0):
			print counter
		canon.gene_transfer(mutant)
		Settings.Chromosome.Polygon.set_range(min(100, percent_diff))
		mutant.mutate(mutation_rate)
		mdifference = mutant.diff(base)
		if mdifference <= difference:
			since_write += 1
			difference = mdifference
			percent_diff = ((difference / float(Xmax * Ymax)) / 225) * 100
			mutation_rate = min(100, percent_diff)
			mutant.gene_transfer(canon)
			grower = mutant.last_draw
			
			if since_write >= 10:
				since_write = 0
				grower.save("./images/"+ run_id +"_"+ str(counter) + \
							".jpg", "JPEG")
				print counter, mdifference, str(int(100-percent_diff)) +"%", \
					since_change, len(canon.chromosomes), \
					int(counter / (100-percent_diff)), "saved"
			else:
				print counter, mdifference, str(int(100-percent_diff)) +"%", \
					 since_change, len(canon.chromosomes), \
					 int(counter / (100-percent_diff))
			since_change = 0
except KeyboardInterrupt:
	grower.save("images/"+ run_id +"_"+ str(counter) +".jpg", "JPEG")
	gene_file = open("genomes/runs/"+ run_id +"_"+ str(counter) +".gen", "w")
	gene_file.write(str(canon))
	gene_file.close()
	
print "\n"+ str(canon)
grower.show()
