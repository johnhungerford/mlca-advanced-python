import abc
import math
import sys
import time

from physics_engine.physics_system import PhysicsSystem

def replace_str_index(text,index=0,replacement='#'):
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

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

    def set_next_frame(self, delta_t_frame_sec: float, num_calcs_per_frame: int) -> None:
        delta_time =  (delta_t_frame_sec / num_calcs_per_frame) * self.time_unit_per_second
        for calc in range(0, num_calcs_per_frame):
            self.system.update_state(delta_time)

    def time_next_frame(self, delta_t_frame_sec: float = 0.25, num_calcs_per_frame: int = 1) -> None:
        start_ts = time.time()
        self.set_next_frame(delta_t_frame_sec, num_calcs_per_frame)
        end_ts = time.time()
        so_far = end_ts - start_ts
        remaining = delta_t_frame_sec - so_far
        if remaining < 0:
            print(f"Unable to keep up with framerate: lost {-remaining} seconds")
            return
        time.sleep(remaining)

    def render_continually(self, delta_t_frame_sec: float = 0.25, num_calcs_per_frame: int = 1) -> None:
        self.render_current_frame()
        while True:
            self.time_next_frame(delta_t_frame_sec, num_calcs_per_frame)
            self.render_current_frame()

    def render_frames(self, total_frames: int, delta_t_frame_sec: float = 0.25, num_calcs_per_frame: int = 1) -> None:
        self.render_current_frame()
        for i in range(0, total_frames):
            self.time_next_frame(delta_t_frame_sec, num_calcs_per_frame)
            self.render_current_frame()

    def render_time_interval(self, total_t_sec: float, delta_t_frame_sec: float = 0.25,
                             num_calcs_per_frame: int = 1) -> None:
        num_frames = math.floor(total_t_sec / delta_t_frame_sec)
        self.render_frames(num_frames, delta_t_frame_sec, num_calcs_per_frame)


class Ascii1DPhysicsSystemRenderer(PhysicsSystemRenderer):
    """
    Simple implementation of SystemRenderer (see above) that renders a frame by printing a line of text
    where "#" represents an object (everything else should be empty space).
    """

    def __init__(self,
                 system: PhysicsSystem,
                 line_length: int = 100,
                 vis_pos_x_min: float = 0,
                 vis_pos_x_max: float = 100,
                 seconds_per_time_unit: float = 1):
        # Use the base class constructor to pass the system and the time unit conversion
        super().__init__(system, seconds_per_time_unit)
        # We also need to establish:
        #   1) how big our view screen is (how long each rendered line is) and
        #   2) what pos_x values correspond to the lower and upper bounds of the view screen
        self.line_length = line_length
        self.range_x = [vis_pos_x_min, vis_pos_x_max]

    def generate_current_frame(self) -> str:
        
        frame  = self.line_length * " "
        new_frame = ""
        act_idx = 0
        act_range = self.range_x[1] - self.range_x[0]
        for phys_object in  self.system.physics_objects:
            if phys_object.pos_x <= self.range_x[1] and phys_object.pos_x >= self.range_x[0]:
                act_idx = int(round(phys_object.pos_x - self.range_x[0]) * (self.line_length - 1)/act_range)
                new_frame = replace_str_index(frame, act_idx)
                frame = new_frame

        return frame

    def render_current_frame(self) -> None:
        sys.stdout.write('\r'+self.generate_current_frame())
        sys.stdout.flush()
