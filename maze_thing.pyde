def setup():
    size(640, 480)
    
import random

char_width=20

def draw_slash(fwd_slash, top, left):
  if fwd_slash > 0.5:
      line(left+char_width, top, left, top+char_width)
  else:
      line(left, top, left+char_width, top+char_width)
      
def draw():
    for j in range(height / char_width):
        for i in range(width / char_width):
            draw_slash(random.random(), j*char_width, char_width*i)
            
noLoop()
    
#def draw():
   #right=20
    #top=20
    #draw_slash(fwd_slash, top, right)
