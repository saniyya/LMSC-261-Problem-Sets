

def setup():
    size(1000,1000)
    no_stroke()
    
def draw():
    drawObject(0,0,1)
    drawObject(-300,-300,1)
    
def drawObject(x,y,s):
    push()
    translate(x,y)
    scale(s)
    fill(255,51,51)
    ellipse(450,650,175,175)
    ellipse(600,615,175,175)
    fill(255,102,178)
    ellipse(500,500,350,350)
    ellipse(650,450,150,150)
    ellipse(362,575,150,150)
    pop()
    
             
        
            
    

    
    
    
    
