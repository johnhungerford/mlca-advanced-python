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

    def __init__(self, force_x_per_mass: float, positive: bool = True):
        self.force_x_per_mass: float = force_x_per_mass
        self.positive: bool = positive

    def force_x(self, physics_object: PhysicsObject) -> float:
        return (1 if self.positive else -1) * self.force_x_per_mass * physics_object.mass


class PhysicsInteraction(abc.ABC):
    """
    Represents an interaction between two physics objects
    """

    @abc.abstractmethod
    def can_interact(self, obj_1: PhysicsObject, obj_2: PhysicsObject) -> bool:
        """
        Return true if there is or can be a force between the two objects. Used to filter out interactions
        where no force exists
        """

    @abc.abstractmethod
    def force_x(self, acted_upon: PhysicsObject, actor: PhysicsObject) -> float:
        """
        "acted_upon" is the object that undergoes the force in question. "actor" is the object whose
        presence causes the force on "acted_upon". Returns the force produced on "acted_upon" by the interaction.
        Note that Newton's 3rd law, which states that force every force there exists an equal and opposite force,
        we can take the opposite of this force (i.e., multiply it by -1) to get the force on "actor," which will
        allow us to avoid calculating the value twice.
        """


class ElectricChargeInteraction(PhysicsInteraction):
    """
    Represents an interaction between charged particles
    """

    def __init__(self, force_charge_constant: float):
        self.force_charge_constant: float = force_charge_constant

    def can_interact(self, obj_1: PhysicsObject, obj_2: PhysicsObject) -> bool:
        """They can only interact if both have charge"""
        return 'charge' in obj_1.properties and 'charge' in obj_2.properties

    def force_x(self, acted_upon: PhysicsObject, actor: PhysicsObject) -> float:
        """Force between two charge particles is -charge_1 * charge_2 / (distance ^ 2) multipled by some constant"""
        distance = acted_upon.pos_x - actor.pos_x
        if distance > 0:
            return self.force_charge_constant * (acted_upon.properties['charge'] * actor.properties['charge']) / (distance * distance)
        elif distance < 0:
            return - self.force_charge_constant * (acted_upon.properties['charge'] * actor.properties['charge']) / (distance * distance)
        return 0


class GravitationalInteraction(PhysicsInteraction):
    """
    Represents the gravitational force between any two objects (with mass)
    """

    def __init__(self, force_mass_constant: float):
        self.force_mass_constant: float = force_mass_constant

    def can_interact(self, obj_1: PhysicsObject, obj_2: PhysicsObject) -> bool:
        """Since all objects have mass, all objects will interact"""
        return True

    def force_x(self, acted_upon: PhysicsObject, actor: PhysicsObject) -> float:
        """Force between two objects is mass_1 * mass_2 / (distance ^ 2) multipled by some constant"""
        distance = acted_upon.pos_x - actor.pos_x
        return self.force_mass_constant * (acted_upon.mass * actor.mass) / (distance * distance)
