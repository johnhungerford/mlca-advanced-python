from typing import List

from physics_engine.physics_object import PhysicsObject

exObj=physicsObject(0,5)

class PhysicsSystem:
    """
    This class should model a system, or collection of physical objects. It should therefore consist primarily of
    a set of `PhysicsObject`s (see the other file in this directory). You should keep a careful eye on how `PhysicsObject`'s
    fields and methods are implemented. `PhysicsSystem` should include a method that updates the system after a
    change in time `delta_t`.
    """
    def __init__(self, physics_objects: List[PhysicsObject]):
        self.physicsObjects = physics_objects
    
    def update_state(self, delta_t):
        for i in self.physicsObjects:
            i.pos_x = i.pox_x+i.vel_x