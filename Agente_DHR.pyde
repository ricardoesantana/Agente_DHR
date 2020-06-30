# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com

# Equipe DHR

from Vehicle import Vehicle
from Food import Food



def setup():
    global v, f, contador
    size(640, 360)
    v = Vehicle(width / 2, height / 2)
    f = Food(random(width), random(height))
    
    contador = 0

    
def draw():
    background(51)
    
    global contador
        
    v.update()
    v.display()
    contador += f.update(v)

    f.display()
    v.seek(f.position)
    
    textSize(20)
    text('Pontos: ' + str(contador), 10, 30)
