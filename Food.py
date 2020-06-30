# The "Food" class

class Food():

    def __init__(self, x, y):
        self.position = PVector(x, y)
        self.r = 6
        
    def update(self, vehicle):
        if (PVector.dist(self.position, vehicle.position) < (2 * self.r)):
            self.position = PVector(random(width), random(height))
            return 1    
        else:
            return 0

    def applyForce(self, force):
        # We could add mass here if we want A = F / M
        self.acceleration.add(force)

    def display(self):
        # Draw a triangle rotated in the direction of velocity
        #theta = self.velocity.heading()# + PI / 2
        fill(127)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            #rotate(theta)
            rect(0, 0, self.r, self.r)
            # beginShape()
            # vertex(0, -self.r * 2)
            # vertex(-self.r, self.r * 2)
            # vertex(self.r, self.r * 2)
            # endShape(CLOSE)
