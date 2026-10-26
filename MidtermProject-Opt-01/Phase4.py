

def setup():
    size(1000,1000)
    no_stroke()
    
def draw():
    x = 0
    y = 0
    while y < 1000:
        while x < 1000:
            drawObject(x,y,1)
            x = x+100
        y = y+100
        x = 0
    
    #for y in range(1000):
        #for x in range(1000):
            #drawObject(x*100,y*100,1)
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(255,51,51)
    ellipse(45,65,17.5,17.5)
    ellipse(60,61.5,17.5,17.5)
    fill(255,102,178)
    ellipse(50,50,35,35)
    ellipse(65,45,15,15)
    ellipse(36.2,57.5,15,15)
    pop()
    
             
        
            
    

    
    
    
    
