#!/usr/bin/python
#  Fitness Function
#  This is how the program decides if a genome is fit
import Image, ImageDraw, ImageChops, ImageStat
global background_color, color_mode, imagewidth, imageheight, base_image, phenotype

def draw_genome(genome):
   genome_image = Image.new(color_mode,(imagewidth,imageheight),background_color)
   if phenotype == "Poly" or phenotype == "Poly3" or phenotype == "Trig":
      # Draw polygons from a list of points
      for polygon in genome:
         color, opacity, points = polygon
         color_mask = Image.new(color_mode,(imagewidth,imageheight), color)
         polygon_mask = Image.new('L',(imagewidth,imageheight), 0)
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
         color_mask = Image.new(color_mode,(imagewidth,imageheight), color)
         circle_mask = Image.new('L',(imagewidth,imageheight), 0)
         ImageDraw.Draw(circle_mask).ellipse(bounding_box, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,circle_mask)
      return genome_image
   elif phenotype == "Ellip":
      # Draw ellipses from ((x,y),(x,y))
      for ellipse in genome:
         color, opacity, points = ellipse
         color_mask = Image.new(color_mode,(imagewidth,imageheight), color)
         ellipse_mask = Image.new('L',(imagewidth,imageheight), 0)
         ImageDraw.Draw(ellipse_mask).ellipse(points, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,ellipse_mask)
      return genome_image
   elif phenotype == "Rect":
      # Draw rectangles from ((x,y),(x,y))
      for rectangle in genome:
         color, opacity, points = rectangle
         color_mask = Image.new(color_mode,(imagewidth,imageheight), color)
         rectangle_mask = Image.new('L',(imagewidth,imageheight), 0)
         ImageDraw.Draw(rectangle_mask).rectangle(points, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,rectangle_mask)
      return genome_image
   elif phenotype == "Line":
      # Draw lines from a list of points
      for line in genome:
         color, opacity, points = line
         color_mask = Image.new(color_mode,(imagewidth,imageheight), color)
         line_mask = Image.new('L',(imagewidth,imageheight), 0)
         if len(points) >= 2:
            ImageDraw.Draw(line_mask).line(points, fill=opacity)
         else: #len(points) == 1:
            ImageDraw.Draw(line_mask).point(points, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,line_mask)
      return genome_image
   elif phenotype == "WLine":
      # Draw lines from a list of points with a width
      for line in genome:
         color, opacity, points = line
         width = points.pop(0)
         color_mask = Image.new(color_mode,(imagewidth,imageheight), color)
         line_mask = Image.new('L',(imagewidth,imageheight), 0)
         if len(points) >= 2:
            ImageDraw.Draw(line_mask).line(points, fill=opacity, width=width)
         else: #len(points) == 1:
            ImageDraw.Draw(line_mask).point(points, fill=opacity)
         genome_image = Image.composite(color_mask,genome_image,line_mask)
      return genome_image

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
