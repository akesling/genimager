# genimagef.py - function-based genetic imager
# Creates a genome (DNA) based on a bunch of chromosomes (polygons)
# that mutates to look like a base image
import Image, ImageDraw, ImageChops, ImageStat
import copy, random

def mutate(DNA):
  #############################
  ###   MUTATION FUNCTION   ###
  #############################
  mDNA = copy.deepcopy(DNA)			# make a copy to mutate
  seedi = random.randint(0,3)			# choose what aspect to mutate
  seedj = random.randint(0,10)			
  index = random.randint(0,max(len(mDNA)-1,0))	# index of polygon in DNA
  if len(mDNA)==0: seedi,seedj = 0,0	# If DNA has no polygons force it to add a polygon
  if seedi == 0:
    ### POLYGON ACTION ###      
    if len(mDNA)>=100: seedj = random.randint(1,3) # DNA has max 100 polygons
    if seedj == 0:
      # INSERT POLYGON
      mDNA.insert(index,[random.randint(0,255),random.randint(0,255),[]])
      seedi = 3
      seedj = 0		# go to insert color to give it a new color
    elif seedj == 1:
      # REMOVE POLYGON
      del mDNA[index]
      return mDNA
    elif seedj == 2:
      # REORDER POLYGONS
      index2 = random.randint(0,max(len(mDNA)-1,0))
      indexa = min(index,index2)
      indexb = max(index,index2)
      mDNA.insert(indexa, mDNA[indexb])
      mDNA.insert(indexb + 1, mDNA[indexa + 1])
      del mDNA[indexa + 1]
      del mDNA[indexb + 1]
      return mDNA
    else : #seedj >= 3:
      # CHANGE POLYGON
      seedi = random.randint(1,3)
      seedj = random.randint(0,3)
  if seedi == 1:
    ### POINT ACTION ###
    ptindex = random.randint(0,max(len(mDNA[index][2])-1,0)) # index of point in polygon
    if len(mDNA[index][2])<3: seedj = 0	# If not >= 3 points, then insert one
    if seedj == 0:
      # INSERT POINT
      Xval = random.randint(-int(Xmax/10.),Xmax+int(Xmax/10.))
      Yval = random.randint(-int(Ymax/10.),Ymax+int(Ymax/10.))
      mDNA[index][2].insert(ptindex,(Xval,Yval))
      return mDNA
    elif seedj == 1:
      # REMOVE POINT
      if len(mDNA[index][2]) > 3:
        del mDNA[index][2][ptindex]
      return mDNA
    elif seedj == 2:
      # REORDER POINTS
      ptindex2 = random.randint(0,max(len(mDNA[index][2])-1,0))
      ptindexa = min(ptindex,ptindex2)
      ptindexb = max(ptindex,ptindex2)
      mDNA[index][2].insert(ptindexa, mDNA[index][2][ptindexb])
      mDNA[index][2].insert(ptindexb + 1, mDNA[index][2][ptindexa + 1])
      del mDNA[index][2][ptindexa + 1]
      del mDNA[index][2][ptindexb + 1]
      return mDNA
    else: #seedj >= 3:
      # CHANGE POINT
      Xval = random.randint(-int(Xmax/10.),+int(Xmax/10.))
      Yval = random.randint(-int(Ymax/10.),+int(Ymax/10.))
      point = mDNA[index][2][ptindex]
      Xval = point[0] + Xval
      Yval = point[1] + Yval
      mDNA[index][2][ptindex] = (Xval,Yval)
      return mDNA  
  elif seedi == 2:
    ### OPACITY ACTION ###
    if seedj == 0:
      # INSERT OPACITY
      opacity = random.randint(0,255)
      mDNA[index][1] = opacity
      return mDNA
    elif seedj == 1:
      # INVERSE OPACITY
      opacity = 255 - mDNA[index][1]
      mDNA[index][1] = opacity
      return mDNA
    elif seedj == 2:
      # REORDER OPACITY
      index2 = random.randint(0,max(len(mDNA)-1,0))
      opacity = mDNA[index][1]
      opacity2 = mDNA[index2][1]
      mDNA[index][1] = opacity2
      mDNA[index2][1] = opacity
      return mDNA
    else: #seedj == 3:
      # CHANGE OPACITY
      opacity = random.randint(-25,25)
      opacity = min(max(mDNA[index][1] + opacity,0),255)
      mDNA[index][1] = opacity
      return mDNA
  else: #seedi == 3:
    ### COLOR ACTION ###
    if seedj == 0:
      # INSERT COLOR
      Cval = random.randint(0,255)
      mDNA[index][0] = Cval
      return mDNA
      #elif seedj == 1:##########
      # SHUFFLE COLORS
      #list = [0,1,2]
      #random.shuffle(list)
      #i,j,k = list
      #color = mDNA[index][0]
      #mDNA[index][0] = (color[i],color[j],color[k])
      #return mDNA
    elif seedj == 2:
      # REORDER COLORS
      index2 = random.randint(0,max(len(mDNA)-1,0))
      color = mDNA[index][0]
      color2 = mDNA[index2][0]
      mDNA[index][0] = color2
      mDNA[index2][0] = color
      return mDNA
    else: #seedj == 3:
      # CHANGE COLOR
      Cval = random.randint(-30,30)
      color = mDNA[index][0]
      Cval = min(max(color + Cval,0),255)
      mDNA[index][0] = Cval
      return mDNA

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
