import time
import pygame

"""
# Display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Physics Engine')
running = True
"""

class PhysicsObject:
    """
    This class should model a physical object in one dimensional space. Don't worry about dimensions or
    shape or anything. We'll treat it as a single point. It should have a pos_x, and a vel_x, and it
    should have a method that calculates its new position after a given change in time (delta_t). All
    these values should be `float`
    """
    def __init__(self, pos_x, vel_y):
        self.pos_x = pos_x
        self.vel_y = vel_y
        self.time = time.time()
        self.delta_t = 0.001

    def update_pos(self):
        #print(time.time() - self.time)
        if time.time() - self.time > self.delta_t:
            self.pos_x += self.vel_y 
            pygame.draw.circle(screen, (255, 255, 255), (self.pos_x, HEIGHT/2), 10)
            self.time = time.time()

    
"""
point = PhysicsObject(WIDTH/2, 1)
               
# Game Loop
while running:
    
    # Events
    for event in pygame.event.get():
    
        # running bool to false
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 50))
    point.update_pos()
    pygame.display.update()


    
pygame.quit()
"""
