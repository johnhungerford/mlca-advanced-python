import abc
from physics_engine.physics_object import PhysicsObject


class PhysicsField(abc.ABC):
    """
    Represents a field that generates a constant force based upon a *single* object's properties.
    """

    def force_x(self, physics_object: PhysicsObject) -> float:
        """
        Return the force in one dimension based on the properties of the object
        """


class ConstantPhysicsField(PhysicsField):
    """A PhysicsField representing a constant force at all points regardless of an object's properties"""

    def __init__(self, force_x_value: float):
        self.force_x_value: float = force_x_value

    def force_x(self, physics_object: PhysicsObject) -> float:
        return self.force_x_value


class GravitationalPhysicsField(PhysicsField):
    """
    A PhysicsField representing a constant acceleration at all points regardless of an object's properts.
    This is made possible by dividing by the object's mass.
    """

    def __init__(self, force_x_per_mass: float):
        self.force_x_per_mass: float = force_x_per_mass

    def force_x(self, physics_object: PhysicsObject) -> float:
        return self.force_x_per_mass / physics_object.mass
