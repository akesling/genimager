# Python program for mona-lisa-ing
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
  seedj = random.randint(0,3)			
  index = random.randint(0,max(len(mDNA)-1,0))	# index of polygon in DNA
  if len(mDNA)==0: seedi,seedj = 0,0	# If DNA has no polygons force it to add a polygon
  if seedi == 0:
    ### POLYGON ACTION ###      
    if len(mDNA)>=50: seedj = random.randint(1,3) # DNA has max 50 polygons
    if seedj == 0:
      # INSERT POLYGON
      mDNA.insert(index,[(0,0,0),random.randint(0,255),[]])
      seedi = 2
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
    else : #seedj == 3:
      # CHANGE POLYGON
      seedi = random.randint(1,3)
      seedj = random.randint(0,3)
  if seedi == 1:
    ### POINT ACTION ###
    ptindex = random.randint(0,max(len(mDNA[index][2])-1,0)) # index of point in polygon
    if len(mDNA[index][2])==0: seedj = 0	# If no points, then insert one
    if seedj == 0:
      # INSERT POINT
      mDNA[index][2].insert(ptindex,(0,0))
      seedj = 3 
    elif seedj == 1:
      # REMOVE POINT
      del mDNA[index][2][ptindex]
      return mDNA
    else: #seedj == 2:
      # REORDER POINTS
      ptindex2 = random.randint(0,max(len(mDNA[index][2])-1,0))
      ptindexa = min(ptindex,ptindex2)
      ptindexb = max(ptindex,ptindex2)
      mDNA[index][2].insert(ptindexa, mDNA[index][2][ptindexb])
      mDNA[index][2].insert(ptindexb + 1, mDNA[index][2][ptindexa + 1])
      del mDNA[index][2][ptindexa + 1]
      del mDNA[index][2][ptindexb + 1]
      return mDNA
    if seedj == 3:
      # CHANGE POINT
      Xval = random.randint(-int(Xmax/10.),Xmax+int(Xmax/10.))
      Yval = random.randint(-int(Ymax/10.),Ymax+int(Ymax/10.))
      mDNA[index][2][ptindex] = (Xval,Yval)
      return mDNA
  elif seedi == 2:
    ### COLOR ACTION ###
    if seedj == 0:
      # INSERT COLOR
      Rval = random.randint(0,255)
      Gval = random.randint(0,255)
      Bval = random.randint(0,255)
      mDNA[index][0] = (Rval,Gval,Bval)
      return mDNA
    elif seedj == 1:
      # SHUFFLE COLORS
      list = [0,1,2]
      random.shuffle(list)
      i,j,k = list
      color = mDNA[index][0]
      mDNA[index][0] = (color[i],color[j],color[k])
      return mDNA
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
      Rval = random.randint(-30,30)
      Gval = random.randint(-30,30)
      Bval = random.randint(-30,30)
      color = mDNA[index][0]
      Rval = (color[0] + Rval) % 255
      Gval = (color[1] + Gval) % 255
      Bval = (color[2] + Bval) % 255
      mDNA[index][0] = (Rval, Gval, Bval)
      return mDNA
  else: #seedi == 3:
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
      opacity = random.randint(-30,30)
      opacity = mDNA[index][1] + opacity % 255
      mDNA[index][1] = opacity
      return mDNA

def draw(DNA):
  im = Image.new('RGB',(Xmax,Ymax))
  for polygon in DNA:
    color, opacity, points = polygon
    if (len(points) >= 3):
      im2 = Image.new('RGB',(Xmax,Ymax), color)
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
basefile = './images/meliphagidae.jpg'
filename = 'meliphagidae'
DNA = 	[[(76, 103, 75), 159, [(422, -43), (-29, 72), (157, 1), (154, 622), (118, 655), (497, 576)]], [(131, 140, 127), 738, [(147, 355), (494, 722), (232, -68), (439, 152), (231, 74), (202, 642), (-28, 308), (179, -31), (350, 405), (145, 533), (113, 277), (392, 654), (203, 612)]], [(252, 246, 242), 192, [(65, 324), (397, 612), (504, 65), (233, 292), (305, 156), (40, -32), (-2, 238)]], [(118, 117, 135), 147, [(473, 38), (215, 143), (507, 95), (398, 605), (105, 691), (220, 472), (80, 735), (13, -52), (319, 134), (42, 377), (283, -61)]], [(43, 51, 36), 123, [(278, 525), (484, 284), (4, 524), (90, 601), (25, 361), (292, 599)]], [(186, 31, 4), 195, [(164, 119), (116, 303), (65, -11)]], [(235, 216, 207), 61, [(289, 211), (91, 96), (-5, 32), (129, 246), (155, -65), (244, 642), (395, 666), (407, 209), (234, 236)]], [(200, 189, 190), 134, [(43, 383), (-33, 255), (448, 116), (390, 145), (191, 211), (97, 700), (307, 454)]], [(71, 71, 81), 62, [(236, 78), (502, 532), (219, 660), (10, 734), (200, -60), (9, 732)]], [(58, 143, 16), 63, [(421, 136), (375, 472), (269, 378)]], [(224, 189, 158), 203, [(476, 264), (473, 366), (173, 480), (364, 164), (429, 52), (73, 128), (318, -5)]], [(234, 218, 251), 20, [(394, 366), (210, 218), (169, 416), (146, 522), (94, 431), (-6, -45), (135, -21), (357, 266), (328, 610), (291, 195), (21, -40), (252, 154), (204, 601)]], [(108, 103, 130), -177, [(91, -33), (153, 526), (439, 469), (223, 169), (478, 204), (442, 528), (509, 552), (136, 726)]], [(229, 248, 230), 33, [(12, 189), (109, 109), (93, 293), (276, 169), (199, 37), (495, -34), (433, 148), (272, 421), (342, 532), (366, 55)]], [(184, 198, 173), 264, [(295, 258), (284, 3), (491, 115), (431, 58), (210, -29), (442, 75), (491, 160), (363, 620), (207, 235), (411, 31), (3, 368), (300, 212), (157, 449), (138, -62), (25, -1), (364, 340)]], [(84, 21, 4), 422, [(282, 520), (407, 147), (168, 229), (398, 479)]], [(199, 185, 118), 112, [(280, 296), (305, 489)]], [(65, 80, 98), 110, [(148, 460), (269, 686), (333, 679), (113, 206), (345, 230), (240, 197)]], [(245, 229, 205), 454, [(314, 219), (94, 383), (202, 529), (402, 131), (227, 350)]], [(118, 116, 255), 242, []], [(141, 159, 190), 187, [(146, 533), (-45, 138), (450, 678), (265, 705), (278, 748), (511, -23)]], [(242, 239, 244), -247, [(428, 156), (92, -59), (39, -44)]], [(203, 253, 236), 400, [(389, 274), (335, 130), (320, 45), (407, -14)]], [(199, 158, 230), 93, [(432, 87), (326, 519)]], [(169, 84, 178), 188, [(500, -52)]], [(251, 183, 137), 82, [(120, 512), (183, 482), (227, 567), (212, 171), (-13, 2), (386, 185), (26, 216)]], [(238, 212, 220), 1113, [(-28, 561), (351, 10), (168, 572), (509, 15), (457, -2), (285, -15), (15, 43), (228, 248), (51, 227), (413, 182), (-30, 483)]], [(246, 232, 214), 71, [(302, 226), (334, 473), (195, 535), (7, 381), (191, 310)]], [(50, 215, 8), 52, [(337, 503)]], [(168, 9, 2), 29, [(437, 199), (-43, 379), (181, -21), (-38, -17), (141, 5)]], [(211, 170, 204), 50, [(403, 5), (67, -2), (19, 311), (133, 91)]], [(217, 209, 208), 97, [(-6, -20), (128, 663), (181, 675), (251, 738), (383, 563), (102, 641), (183, 142), (357, 195)]], [(225, 153, 36), 175, [(299, 242)]], [(199, 216, 200), 641, [(444, 160), (446, 261), (33, 265), (-45, 414), (443, 450), (339, 319), (154, 514), (79, 522), (363, 586), (347, 581), (5, 666), (310, 308), (412, 43), (318, -55)]], [(235, 253, 233), 237, [(298, 467), (352, 420), (-35, 18), (57, 462)]], [(219, 39, 114), 56, []], [(87, 54, 156), 183, [(24, 575)]], [(233, 225, 222), -180, [(-7, -1), (-45, 395), (246, 595), (116, -25), (282, -6), (177, 286), (189, 133), (160, 271)]], [(125, 14, 229), 246, [(386, -43), (500, -42)]], [(53, 66, 73), 71, [(246, 577), (482, 301), (482, 761), (382, 709), (182, 509)]], [(99, 12, 2), 127, [(209, 423), (80, 285), (393, 226), (77, 163)]], [(198, 174, 20), 170, [(286, 328), (345, 340), (244, 403), (140, 437), (239, 599), (155, 307)]], [(202, 205, 216), -181, [(414, 241), (-33, 695), (143, 20), (3, 193), (14, 394), (266, 285), (-3, 208), (46, 90), (80, 288), (73, 410), (366, 492), (438, 329)]], [(91, 150, 194), 310, [(483, 39)]], [(44, 121, 79), 166, []], [(229, 212, 201), 49, [(288, 634), (448, 179), (456, 196), (453, 89), (413, 19), (306, 317), (77, 219), (-16, 108)]], [(228, 252, 229), 231, [(412, -61), (122, -53), (55, 89), (52, 103), (228, 125), (426, -39)]], [(195, 211, 199), 188, [(50, 390), (27, 337), (105, -27), (58, 260), (112, -69), (-25, -64), (-5, 368)]]] #the 'kept' dna strand
mDNA = copy.deepcopy(DNA)		# the 'mutated' dna strand
base = Image.open(basefile)
base = base.convert('RGB')
DNAIm = Image.new('RGB',base.size) # Image from DNA
mDNAIm = Image.new('RGB',base.size) # Image from mutated DNA
diffIm = ImageChops.difference(DNAIm, base) # difference Image
diffStat = ImageStat.Stat(diffIm) # Statistics instance for difference image
Xmax, Ymax = base.size
difference = sum(diffStat.sum)
mdifference = difference
counter = 60891
while (difference >= 1E7):
  counter = counter + 1
  setpoint = min(int(round(random.normalvariate(12,4))),1)
  #for i in xrange(setpoint):
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
