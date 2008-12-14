#!/usr/bin/python
#  Fitness Function
#  This is how the program decides if a genome is fit
import Image, ImageDraw, ImageChops, ImageStat
global background_color, color_mode, ImageWidth, ImageHeight, base_image, phenotype

def draw_genome(genome):
   genome_image = Image.new(color_mode,(ImageWidth,ImageHeight),background_color)
   if phenotype == "Poly" or phenotype == "Poly3" or phenotype == "Trig":
      # Draw polygons from a list of points
      for polygon in genome:
         color, opacity, points = polygon
         color_mask = Image.new(color_mode,(ImageWidth,ImageHeight), color)
         polygon_mask = Image.new(color_mode,(ImageWidth,ImageHeight), 0)
         if len(points) >= 3:
            ImageDraw.Draw(polygon_mask).polygon(points, fill=opacity)
         elif len(points) == 2:
            ImageDraw.Draw(polygon_mask).line(points, fill=opacity)
         else: #len(points) == 1:
            ImageDraw.Draw(polygon_mask).point(points, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,polygon_mask)
      return genome_image
   elif phenotype == "Circ":
      # Draw circles from (centerX,centerY,radius)
      for circle in genome:
         color, opacity, points = circle
         #calculate bounding box
         centerX, centerY, radius = points[0], points[1], points[2]
         bounding_box = ((centerX-radius,centerY-radius),(centerX+radius,centerY+radius))
         color_mask = Image.new(color_mode,(ImageWidth,ImageHeight), color)
         circle_mask = Image.new(color_mode,(ImageWidth,ImageHeight), 0)
         ImageDraw.Draw(polygon_mask).ellipse(bounding_box, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,polygon_mask)
      return genome_image
   elif phenotype == "Ellip":
      # Draw ellipses from ((x,y),(x,y))
      for ellipse in genome:
         color, opacity, points = ellipse
         color_mask = Image.new(color_mode,(ImageWidth,ImageHeight), color)
         circle_mask = Image.new(color_mode,(ImageWidth,ImageHeight), 0)
         ImageDraw.Draw(polygon_mask).ellipse(points, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,polygon_mask)
   elif phenotype == "Rect":
      # Draw rectangles from ((x,y),(x,y))
      for ellipse in genome:
         color, opacity, points = ellipse
         color_mask = Image.new(color_mode,(ImageWidth,ImageHeight), color)
         circle_mask = Image.new(color_mode,(ImageWidth,ImageHeight), 0)
         ImageDraw.Draw(polygon_mask).rectangle(points, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,polygon_mask)

def image_difference(genome_image):
   """
   Image Difference
   takes two images and returns the differece
   calculated per pixel by taking the sum of the sqaured difference of each color
   and summing all of these over the whole image
   """
   difference_image = ImageChops.difference(genome_image, base_image) 
   difference_statistics = ImageStat.Stat(difference_image) # statistics for difference_image
   difference_value = sum(difference_statistics.sum2) #stat.sum returns a list of each color sum**2
   return difference_value
