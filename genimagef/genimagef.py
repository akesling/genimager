# genimagef.py - function-based genetic imager
# Creates a genome (DNA) based on a bunch of chromosomes (polygons)
# that mutates to look like a base image
import Image, ImageDraw, ImageChops, ImageStat
import copy, random
random.seed()
#MAIN
basefile = 'darkwonder.jpg'
filename = 'darkwonderBW'
basecolor = 0
DNA = []				# the 'kept' dna strand
mDNA = []				# the 'mutated' dna strand
base = Image.open('../images/'+filename+'/'+basefile)
base = base.convert('L')
DNAIm = Image.new('L',base.size) # Image from DNA
mDNAIm = Image.new('L',base.size) # Image from mutated DNA
diffIm = ImageChops.difference(DNAIm, base) # difference Image
diffStat = ImageStat.Stat(diffIm) # Statistics instance for difference image
ImageWidth, ImageHeight = base.size
import mutateBW as mutate, fitnessBW as fitness
difference = sum(diffStat.sum2)
mdifference = difference
counter = 0
gencounter = 0
while (difference >= 1E6):
  counter = counter + 1
  setpoint = min(int(round(random.normalvariate(12,4))),1)
  mDNA = mutate.mutate(DNA) #mutate the DNA
  mDNAIm = fitness.draw(mDNA) # draw the mutated DNA image
  mdifference = fitness.diff(mDNAIm, base) # difference of mutated DNA to base image
  if (mdifference == difference):
    DNA = mDNA
    DNAIm = mDNAIm
    difference = mdifference
  elif (mdifference < difference):
    gencounter = gencounter + 1
    DNA = mDNA
    DNAIm = mDNAIm
    difference = mdifference
    print 'level up! counter:',counter,'diff:',difference,'gons:',len(DNA)
    if gencounter % 10 == 0:
      DNAIm.save('../images/'+filename+'/'+filename+'_'+str(counter)+'.jpg','JPEG')
