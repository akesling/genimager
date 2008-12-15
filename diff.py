import Image, ImageChops
import sys
original = Image.open(sys.argv[1])
final = Image.open(sys.argv[2])
difference = ImageChops.difference(original, final)
difference.show()
