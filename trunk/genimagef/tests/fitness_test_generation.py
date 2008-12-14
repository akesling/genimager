#!/usr/bin/python
# Fitness Test Generation Script
# This generates the images that are used to test the fitness function
import Image, ImageDraw

# Draw color images first
##################################
# Polygon Test; phenotype = "Poly"
#base
image = Image.new('RGB',(400,400),(0,0,0))
# first polygon - red
layer = Image.new('RGB',(400,400),(150,0,0))
mask = Image.new('L',(400,400),0)
draw = ImageDraw.Draw(mask)
draw.polygon([(100,100),(200,300),(100,300),(300,100),(300,200)],fill=200)
image = Image.composite(layer,image,mask)
# second polygon - green
layer = Image.new('RGB',(400,400),(0,0,70))
mask = Image.new('L',(400,400),0)
draw = ImageDraw.Draw(mask)
draw.polygon([(200,300),(300,100),(400,200),(300,300)],fill=150)
image = Image.composite(layer,image,mask)
# third polygon - blue
layer = Image.new('RGB',(400,400),(0,200,0))
mask = Image.new('L',(400,400),0)
draw = ImageDraw.Draw(mask)
draw.polygon([(0,0),(100,200),(200,100)],fill=70)
image = Image.composite(layer,image,mask)
# output image
image.save('color_poly.png','PNG')


