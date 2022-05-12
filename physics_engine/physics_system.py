from typing import List

from physics_engine.physics_forces import PhysicsField
from physics_engine.physics_object import PhysicsObject


class PhysicsSystem:
    """
    This class should model a system, or collection of physical objects. It should therefore consist primarily of
    a set of `PhysicsObject`s (see the other file in this directory). You should keep a careful eye on how `PhysicsObject`'s
    fields and methods are implemented. `PhysicsSystem` should include a method that updates the system after a
    change in time `delta_t`.

    Now that we are adding
    """
    def __init__(self, physics_objects: List[PhysicsObject], physics_fields: List[PhysicsField]):
        self.physics_objects: List[PhysicsObject] = physics_objects
        self.physics_fields: List[PhysicsField] = physics_fields
    
    def update_state(self, delta_t: float):
        for physics_object in self.physics_objects:
            physics_object.update_state(delta_t, 0)