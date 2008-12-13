# genimagef.py - function-based genetic imager
# Creates a genome (DNA) based on a bunch of chromosomes (polygons)
# that mutates to look like a base image
import Image, ImageDraw, ImageChops, ImageStat
import copy, random
import mutate

def draw(DNA):
  im = Image.new('L',(Xmax,Ymax),basecolor)
  for polygon in DNA:
    color, opacity, points = polygon
    if (len(points) >= 3):
      im2 = Image.new('L',(Xmax,Ymax), color)
      mask = Image.new('L',(Xmax,Ymax), 0)
      maskDraw = ImageDraw.Draw(mask)
      maskDraw.polygon(points, fill=0x77) #
      im = Image.composite(im2,im,mask)
  return im

def diff(newImg, baseImg):
  diffIm = ImageChops.difference(newImg, baseImg)
  diffStat = ImageStat.Stat(diffIm)
  diffnum = sum(diffStat.sum) #stat.sum returns a list of each color sum
  return diffnum

#MAIN
random.seed()
basefile = './images/darkwonder.jpg'
filename = 'darkwonderBW'
basecolor = 255
DNA = []				# the 'kept' dna strand
mDNA = []				# the 'mutated' dna strand
base = Image.open(basefile)
base = base.convert('L')
DNAIm = Image.new('L',base.size) # Image from DNA
mDNAIm = Image.new('L',base.size) # Image from mutated DNA
diffIm = ImageChops.difference(DNAIm, base) # difference Image
diffStat = ImageStat.Stat(diffIm) # Statistics instance for difference image
Xmax, Ymax = base.size
difference = sum(diffStat.sum)
mdifference = difference
counter = 0
while (difference >= 1E5):
  counter = counter + 1
  setpoint = min(int(round(random.normalvariate(12,4))),1)
  mDNA = mutate(DNA) #mutate the DNA
  mDNAIm = draw(mDNA) # draw the mutated DNA image
  mdifference = diff(mDNAIm, base) # difference of mutated DNA to base image
  if (mdifference == difference):
    DNA = mDNA
    DNAIm = mDNAIm
    difference = mdifference
  elif (mdifference < difference):
    DNA = mDNA
    DNAIm = mDNAIm
    difference = mdifference
    print 'level up! counter:',counter,'diff:',difference,'gons:',len(DNA)
    DNAIm.save('./images/'+filename+'/'+filename+'_'+str(counter)+'.jpg','JPEG')
