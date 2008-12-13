from genome import Genome
import Image, ImageDraw, ImageChops, ImageStat
import random, copy
random.seed()

run_id = str(random.randint(0,9999999999))
###########################################
filename = "mona-lisa.jpg"
###########################################
base = Image.open(filename)
base = base.convert('RGBA')
base_pix = base.load()
#base = ImageChops.invert(base) #

Xmax, Ymax = base.size
canon = Genome(Xmax, Ymax)
mutant = Genome(Xmax, Ymax)
grower = Image.new('RGBA',base.size) # Image from DNA

# MAIN
difference = 5000000000000
percent_diff = 100
mutation_rate = 100
counter = 0
since_change = 0
since_write = 0
base.show()
print "Run Number:", run_id + "\n" + \
	"Iter. |", "Fitness |", "% Similarity |", "Since Last Evolve |", "Polygons"
while (1):
	counter += 1
	since_change += 1
	if (counter % 50 == 0):
		print counter
	canon.gene_transfer(mutant)
	mutant.mutate(mutation_rate)
	mdifference = mutant.diff(base)
	if mdifference < difference:
		since_write += 1
		difference = mdifference
		percent_diff = ((difference / float(Xmax * Ymax)) / 225) * 100
		mutation_rate = min(100, percent_diff)
		mutant.gene_transfer(canon)
		grower = mutant.last_draw
		
		if since_write >= 10:
			since_write = 0
			grower.save("./images/"+ run_id +"_"+ str(counter) +".jpg", "JPEG")
			print counter, mdifference, str(int(100-percent_diff)) +"%", since_change, len(canon.chromosomes), "saved"
		else:
			print counter, mdifference, str(int(100-percent_diff)) +"%", since_change, len(canon.chromosomes)
		since_change = 0

grower.show()
