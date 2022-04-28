from physics_engine.physics_system import PhysicsSystem

class SystemRenderer:
    """
    This class is what will *display* a `PhysicsSystem` and all of its `PhysicsObject`s as they change over time.
    """

    def __init__(self, system: PhysicsSystem, seconds_per_time_unit: float):
        self.system = system
        self.seconds_per_time_unit = seconds_per_time_unit

    def render_current(self) -> None:
        pass

    def render_by_time(self, delta_t: float, total_t: float) -> None:
        pass

    def render_by_frames(self, delta_t: float, total_frames: int) -> None:
        pass
