from physics_engine.physics_forces import ConstantPhysicsField, GravitationalPhysicsField, ElectricChargeInteraction, \
    GravitationalInteraction
from physics_engine.physics_object import PhysicsObject
from physics_engine.physics_system import PhysicsSystem
from physics_engine.system_renderer import Ascii1DPhysicsSystemRenderer

obj1 = PhysicsObject(3, 0, 1, {'charge': 20, 'inert': True})
obj2 = PhysicsObject(97, 0, 1, {'charge': 20, 'inert': True})
obj3 = PhysicsObject(10, 50, 4, {'charge': 40})
obj4 = PhysicsObject(90, -50, 4, {'charge': 40})
charge_interaction = ElectricChargeInteraction(50)
system_1: PhysicsSystem = PhysicsSystem([obj1, obj2, obj3, obj4], [], [charge_interaction])
renderer_1 = Ascii1DPhysicsSystemRenderer(system_1)

obj5 = PhysicsObject(97, 0, 1, {'charge': 60, 'inert': True})
obj6 = PhysicsObject(10, 0, 5, {'charge': 15})
obj7 = PhysicsObject(20, 0, 5, {'charge': 15})
obj8 = PhysicsObject(30, 0, 5, {'charge': 15})
obj9 = PhysicsObject(40, 0, 5, {'charge': 15})

gravitational_field = GravitationalPhysicsField(20)
system_2: PhysicsSystem = PhysicsSystem([obj5, obj6, obj7, obj8, obj9], [gravitational_field], [charge_interaction])
renderer_2 = Ascii1DPhysicsSystemRenderer(system_2)

if __name__ == "__main__":
    print('\n\n')
    renderer_2.render_time_interval(30, 0.017, 500)
