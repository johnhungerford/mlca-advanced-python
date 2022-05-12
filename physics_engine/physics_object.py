import time

class PhysicsObject:
    """
    This class should model a physical object in one dimensional space. Don't worry about dimensions or
    shape or anything. We'll treat it as a single point. It should have a pos_x, and a vel_x, and it
    should have a method that calculates its new position after a given change in time (delta_t). All
    these values should be `float`
    """
    def __init__(self, pos_x: float, vel_x: float):
        self.pos_x: float = pos_x
        self.vel_x: float = vel_x

    def update_pos(self, delta_t: float):
            self.pos_x += self.vel_x * delta_t


    
    
