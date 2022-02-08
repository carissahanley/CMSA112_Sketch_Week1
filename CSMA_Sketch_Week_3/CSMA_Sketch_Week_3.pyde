import time


history = []
lifespan = 3000


def setup():
    
    size(500, 500)
    frameRate(20)
    colorMode(RGB, width, height, 255, 100)
    noStroke()
    
    
def draw():
    background(500)
    x = mouseX
    y = mouseY
    agent = [x, y, now()]
    history.append(agent)
    
    if len(history) > 500:
        history.pop(0)
        
    for agent in history:
        x, y = agent[0], agent[1]
        r, g, b = x, y, 0
        
        age = now() - agent[2]
        fade_factor = age / float(lifespan)
        a = 100 - fade_factor * 100 
        
        fill(r, g, b, a)
        circle(x, y, 20)
        
    print(agent)
  
def now(): 
    return int(time.time() * 1000)
    


    
    
