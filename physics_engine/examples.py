from physics_engine.physics_forces import ConstantPhysicsField, GravitationalPhysicsField, ElectricChargeInteraction, \
    GravitationalInteraction
from physics_engine.physics_object import PhysicsObject
from physics_engine.physics_system import PhysicsSystem
from physics_engine.system_renderer import Ascii1DPhysicsSystemRenderer

physics_system: PhysicsSystem = None # PUT SOMETHING HERE!
physics_renderer = Ascii1DPhysicsSystemRenderer(physics_system)

if __name__ == "__main__":
    physics_renderer.render_continually()
