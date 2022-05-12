import abc

from physics_engine.physics_system import PhysicsSystem


class PhysicsSystemRenderer(abc.ABC):
    """
    This class is what will *display* a `PhysicsSystem` and all of its `PhysicsObject`s as they change over time.
    It is an "abstract class", which means that it includes unimplemented "abstract methods" (see below). We can
    create classes that extend this class and implement its methods to provide different rendering solutions that
    can be used in our application in the *same exact way*.
    """

    def __init__(self, system: PhysicsSystem, seconds_per_time_unit: float):
        self.system = system
        # We need to have some notion of how many seconds on the screen corresponds to the unit
        # of time of our physics system
        self.seconds_per_time_unit = seconds_per_time_unit
        # Let's precalculate the reverse conversion for the sake of efficiency (division is
        # more time-consuming than multiplication)
        self.time_unit_per_second = 1 / seconds_per_time_unit

    @abc.abstractmethod
    def render_current_frame(self) -> None:
        """
        Render a single frame the current state of self.system
        """
        pass

    @abc.abstractmethod
    def set_next_frame(self, delta_t_calc_sec: float, delta_t_frame_sec: float) -> None:
        """
        Update system state for the next frame, calculating all changes of position over delta_t_calc_sec intervals,
        after a larger interval of delta_t_frame_sec. Note that delta_t_calc_sec must be <= delta_t_frame_sec
        """

    @abc.abstractmethod
    def render_time_interval(self, delta_t_calc_sec: float, delta_t_frame_sec: float, total_t_sec: float) -> None:
        """
        Render movement over total_t_sec seconds, with delta_t_calc_sec intervals to calculate changes of position
        and delta_t_frame_sec seconds between rendered frames
        """
        pass

    @abc.abstractmethod
    def render_frames(self, delta_t_calc_sec: float, delta_t_frame_sec: float, total_frames: int) -> None:
        """
        Render movement over total_frames frames, with delta_t_calc_sec intervals to calculate changes of position
        and delta_t_frame_sec seconds between rendered frames
        """
        pass

    @abc.abstractmethod
    def render_continually(self, delta_t_calc_sec: float, delta_t_frame_sec: float) -> None:
        """
        Render continually, calculating delta_t_calc_sec intervals of motion and rendering position every
        delta_t_frame_sec seconds
        """


class Ascii1DPhysicsSystemRenderer(PhysicsSystemRenderer):
    """
    Simple implementation of SystemRenderer (see above) that renders a frame by printing a line of text
    where "#" represents an object.
    """

    def __init__(self,
                 system: PhysicsSystem,
                 seconds_per_time_unit: float,
                 line_length: int,
                 vis_pos_x_min: float,
                 vis_pos_x_max: float):
        # Use the base class constructor to pass the system and the time unit conversion
        super().__init__(system, seconds_per_time_unit)
        # We also need to establish:
        #   1) how big our view screen is (how long each rendered line is) and
        #   2) what pos_x values correspond to the lower and upper bounds of the view screen
        self.line_length = line_length
        self.range_x = [vis_pos_x_min, vis_pos_x_max]

    def generate_current_frame(self) -> str:
        pass

    def render_current_frame(self) -> None:
        print(self.generate_current_frame())

    def set_next_frame(self, delta_t_calc_sec: float, delta_t_frame_sec: float) -> None:
        pass

    def render_time_interval(self, delta_t_calc_sec: float, delta_t_frame_sec: float, total_t_sec: float) -> None:
        pass

    def render_frames(self, delta_t_calc_sec: float, delta_t_frame_sec: float, total_frames: int) -> None:
        pass

    def render_continually(self, delta_t_calc_sec: float, delta_t_frame_sec: float) -> None:
        pass
