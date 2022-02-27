from PIL import Image
im = Image.new("RGB", (960,1280))
 
infile = open('result.txt', 'r')
data = infile.read().strip('\n').split(', ')
 
rgblist = []
 
for x in data:
  v = x.strip(')').strip('(').split()
  rgb = (int(v[0]),int(v[1]),int(v[2]))
  rgblist.append(rgb)
 
im.putdata(rgblist)
im.save("output.png") 