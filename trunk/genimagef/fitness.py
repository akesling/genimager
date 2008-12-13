#!/usr/bin/python
#  Fitness Function
#  This is how the program decides if a genome is fit
import Image, ImageDraw, ImageChops, ImageStat
from __main__ import ImageWidth, ImageHeight, basecolor

def draw(DNA):
  im = Image.new('L',(ImageWidth,ImageHeight),basecolor)
  for polygon in DNA:
    color, opacity, points = polygon
    if (len(points) >= 3):
      im2 = Image.new('L',(ImageWidth,ImageHeight), color)
      mask = Image.new('L',(ImageWidth,ImageHeight), 0)
      maskDraw = ImageDraw.Draw(mask)
      maskDraw.polygon(points, fill=opacity) 
      im = Image.composite(im2,im,mask)
  return im

def diff(newImg, baseImg):
  diffIm = ImageChops.difference(newImg, baseImg)
  diffStat = ImageStat.Stat(diffIm)
  diffnum = sum(diffStat.sum2) #stat.sum returns a list of each color sum**2
  return diffnum
