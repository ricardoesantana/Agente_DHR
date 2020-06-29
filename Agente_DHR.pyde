# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Seeking "vehicle" follows the mouse position

# Implements Craig Reynold's autonomous steering behaviors
# One vehicle "seeks"
# See: http://www.red3d.com/cwr/

from Vehicle import Vehicle
#from Food import Food

def setup():
    global v, food, mouse
    size(640, 360)
    #velocity = PVector(0, 0)
    v = Vehicle(width / 2, height / 2)
    #food = Food(random(width), random(height), velocity)
    
    w = random(width)
    h = random(height)
    mouse = PVector(w, h)

def draw():
    background(51)
    
    #mouse = PVector(mouseX, mouseY)

    # Draw an ellipse at the mouse position
    fill(127)
    stroke(200)
    strokeWeight(2)
    ellipse(mouse.x, mouse.y, 7, 7)

    # Call the appropriate steering behaviors for our agents
    v.arrive(mouse)
    v.update()
    v.display()
    
    #food.update()
    #food.display()
