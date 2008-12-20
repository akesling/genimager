import Image
import draw
pic = Image.open("mona-lisa.jpg")
print "white line from (0,0) to (100,100)"
draw.line(pic.load(), (255,255,255), (0,0), (100,100))
print "black line from (100,100) to (200,200)"
draw.line(pic.load(), (0,0,0), (100,100), (200,200))
print "blue line from (100,100) to (0,200)"
draw.line(pic.load(), (0,0,255), (100,100), (0,200))
print "red line from (100,100) to (200,0)"
draw.line(pic.load(), (255,0,0), (100,100), (200,0))
pic.show()
