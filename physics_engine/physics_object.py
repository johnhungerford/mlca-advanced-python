import time
from typing import Optional


def acceleration_from_force_and_mass(force: float, mass: float) -> float:
    """
    Use this method to calculate the acceleration of an object from the current force
    on that object and the object's mass
    """
    return force / mass 


class PhysicsObject:
    """
    This class should model a physical object in one dimensional space. Don't worry about dimensions or
    shape or anything. We'll treat it as a single point. It should have a pos_x, and a vel_x, and it
    should have a method that calculates its new position after a given change in time (delta_t). All
    these values should be `float`
    """

    def __init__(self, pos_x: float, vel_x: float, mass: float, properties: Optional[dict] = None):
        """
        Each object has a position, a velocity, and a mass. Note that there is also a "properties" field
        is a dict object allowing any other optional properties we might want to give an object. This is
        where we can keep "charge," for instance.
        """
        self.pos_x: float = pos_x
        self.vel_x: float = vel_x
        self.mass: float = mass
        self.properties: dict = {} if properties is None else properties

    def update_state(self, delta_t: float, total_force: float):
        """
        Over any given change in time there are *two* things that will change: the position and the velocity.
        Position will change based on the *current* velocity. Velocity will change based on acceleration, which
        can be calculated from the force and mass using the helper function `acceleration_from_force_and_mass`.
        """
        old_vel = self.vel_x
        self.vel_x = self.vel_x + (acceleration_from_force_and_mass(total_force, self.mass) * delta_t)
        self.pos_x += 0.5 * (old_vel + self.vel_x) * delta_t  # use average velocity, not initial velocity

