import time


# Display
WIDTH = 200


class PhysicsObject:
    """
    This class should model a physical object in one dimensional space. Don't worry about dimensions or
    shape or anything. We'll treat it as a single point. It should have a pos_x, and a vel_x, and it
    should have a method that calculates its new position after a given change in time (delta_t). All
    these values should be `float`
    """
    def __init__(self, pos_x, vel_x):
        self.pos_x = pos_x
        self.vel_x = vel_x

    def update_pos(self):
            self.pos_x += self.vel_x

class ui:
    def __init__(self, width):
        self.width = width
        self.canvas = [" "] * self.width
        self.icon = "o"
        
    
    def draw(self, x):
        if x < self.width and x >= 0:
            self.canvas[x] = self.icon

        x = ""
        for element in self.canvas:
            x += str(element)

        print(x)
        self.canvas = [" "] * self.width




# TERMINAL UI        
point = PhysicsObject(int(WIDTH/2), 0)
canvas = ui(WIDTH)
running = True

print("Type 'info' for list of commands!")    
# Game Loop
while running:
    next_frame = input()
    
    if next_frame.isnumeric():
        point.vel_x = int(next_frame)
        print("Current velocity: " + str(point.vel_x))
        print()

    elif len(next_frame) > 0:
        if next_frame[-1].isnumeric() and next_frame[0] != "c":
            point.vel_x = int(next_frame)
            print("Current velocity: " + str(point.vel_x))
            print()

    if str(next_frame) == "q" or str(next_frame) == "Q":
        print("EXITING...")
        running = False
        
    if len(next_frame) > 0:
        
        if str(next_frame)[0] == "c":
            canvas.icon = str(next_frame)[3:]
            print("New Icon: " + canvas.icon)

        if str(next_frame)[0] == "i":
            print()
            print("***************************************************")
            print("*               =COMMAND LIST=                  *")
            print("*                                                             *")
            print("*           [] = PRINT NEXT FRAME               *")
            print("*  [INT] = CHANGE VELOCITY TO 'INT'       *")
            print("*             [help] = HELP MENU                  *")
            print("*     [ci (NEW ICON)] = CHANGES ICON      *")
            print("*       [q] or [Q] = QUIT SIMULATION         *")
            print("*                                                             *")
            print("***************************************************")
            print()
            
            
    point.update_pos()
    canvas.draw(point.pos_x)

    
    
    
