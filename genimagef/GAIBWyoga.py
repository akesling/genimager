# This is an experiment to make it more 'delicate'
# it becomes 10x more likely to try 'small adjustments'
# MAX POLYGON = 100
# opacity and color now just goes to 255 if it evloves to 260

# automatic restarts (check for outfile, grab DNA and counter)

# Python program for Genetic Alg Image in BLACK AND WHITE
# change max polygons
# figure out how far points should go outside of edge
# draw over color layer instead of making new
# get alpha layer working
# disp percentage or ln(p) of percent completed
# set max points
# adjust so base color is average of image
# only output certian interval images (once every 10, or based on percent difference)
# start from seed

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
basefile = './images/yoga.jpg'
filename = 'yogaBW'
basecolor = 255
DNA = [[12, 89, [(312, 611), (16, 237)]], [199, 70, [(75, 412), (585, 451)]], [255, 179, [(322, 479), (29, 142), (86, 111)]], [105, 116, [(136, 612), (778, 757)]], [132, 248, [(242, 642), (133, -61)]], [93, 86, [(791, 191)]], [149, 197, []], [104, 61, [(442, 301), (113, 785)]], [212, 50, [(722, 544), (358, -59)]], [211, 152, [(577, 160), (700, 156)]], [231, 146, [(214, 595), (94, 282)]], [1, 218, [(275, 4), (733, 46), (701, -171)]], [37, 68, [(456, 131), (678, 357)]], [220, 37, [(186, 405), (585, 458)]], [12, 255, [(641, 431), (71, 84)]], [90, 222, [(783, 538), (224, 334)]], [200, 221, [(199, 498), (606, 532)]], [99, 100, [(117, 154), (703, 60), (796, 178)]], [14, 255, [(198, 361), (39, 274)]], [0, 175, [(591, 717), (357, 331), (447, 274)]], [29, 102, []], [255, 232, [(216, 666), (233, 659), (-13, 91), (296, 96)]], [0, 1, [(821, 8), (517, 179), (420, -18), (422, -74), (-25, -5), (143, 71)]], [65, 175, [(314, -1), (-40, 763)]], [163, 24, [(505, 19), (294, -52), (456, 447)]], [200, 55, [(167, 489), (838, 21), (210, 294)]], [221, 17, [(507, 709), (84, 386)]], [255, 3, [(532, 816), (24, 773), (701, 575)]], [199, 177, [(105, 196), (-27, 292), (-121, 229)]], [0, 0, [(336, 109), (177, 571), (149, 193)]], [0, 173, [(211, 700), (192, 532), (240, 69)]], [90, 57, [(833, 2), (458, -114), (622, 184)]], [7, 222, [(133, 552), (222, -82), (216, 571)]], [0, 188, [(421, 314), (139, 215), (233, 292), (277, 382)]], [255, 0, [(546, 322), (62, 216), (-19, 46), (297, 39)]], [61, 58, [(768, 634), (518, 139)]], [95, 92, [(-6, 154), (25, 172)]], [132, 17, [(173, 557), (675, 632)]], [231, 216, [(187, 507)]], [186, 41, [(76, 94), (523, 79), (760, 229)]], [113, 206, [(154, 612), (726, 383)]], [150, 36, [(280, 277), (274, 430), (121, 116)]], [153, 225, [(419, 156), (46, 517)]], [67, 36, [(779, 9), (54, 124), (0, 157), (-74, -168)]], [153, 123, [(598, 477), (274, 182)]], [69, 74, [(267, 448), (376, 225), (670, -33), (-43, -60)]], [88, 151, [(600, 743), (593, 529)]], [31, 33, []], [59, 73, [(76, 285), (121, 474)]], [204, 255, [(702, 64), (370, 339), (253, 129)]], [167, 217, [(162, 363), (436, 117)]], [49, 231, [(100, 56), (745, 203)]], [64, 20, [(699, 760)]], [141, 255, [(305, 92), (78, 253), (-33, 57)]], [140, 184, [(34, 273), (794, 163)]], [12, 126, [(213, 322), (586, 686)]], [216, 247, [(480, 129), (274, 179), (752, 232)]], [75, 64, [(571, 305), (583, 419)]], [220, 252, [(772, 222), (151, 219), (-17, 137)]], [255, 239, [(275, 75), (94, 798), (220, 248)]], [88, 255, [(462, -48), (163, 615)]], [204, 119, [(249, 462), (105, 41)]], [0, 226, [(352, 237), (200, 429), (241, 427)]], [26, 239, [(398, 165), (591, 598)]], [255, 102, [(616, 250), (51, 98), (-9, 255)]], [131, 188, [(-52, 59), (268, 96), (-51, 196)]], [192, 168, [(697, 184), (383, -36)]], [157, 189, []], [87, 229, [(214, 337), (285, 623)]], [58, 61, [(254, 534), (640, 533)]], [0, 141, [(380, 304), (481, 322), (573, 761), (485, 526)]], [0, 123, [(159, 173), (456, 554), (526, 376)]], [110, 133, [(274, -20), (57, 682)]], [0, 181, [(349, 371), (492, 492), (416, 564)]], [184, 203, [(356, 459), (16, 275)]], [111, 241, [(68, 584), (106, 262)]], [161, 242, []], [122, 69, [(560, 92), (404, 304)]], [176, 243, [(416, 557), (502, 331)]], [1, 5, [(299, 356), (115, 138), (502, 378)]], [204, 121, [(615, 153), (405, 378)]], [178, 236, [(636, 165), (-46, 211), (-23, 91)]], [168, 172, [(330, 531), (318, 431)]], [12, 61, [(151, 410), (352, 389), (186, 118)]], [105, 138, [(554, 486), (669, 47)]]]				# the 'kept' dna strand
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
counter = 12425
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
    print DNA
    DNAIm.save('./images/'+filename+'/'+filename+'_'+str(counter)+'.jpg','JPEG')
mDNAIm.show()
