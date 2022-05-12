import pytest

from physics_engine.physics_object import PhysicsObject
from physics_engine.physics_system import PhysicsSystem
from physics_engine.system_renderer import Ascii1DPhysicsSystemRenderer


def test_ascii_system_renderer_should_generate_empty_window_of_correct_size_if_no_objects():
    system = PhysicsSystem([], [])
    renderer = Ascii1DPhysicsSystemRenderer(system, 1, 10, 0, 9)
    expected_frame = "          "
    actual_frame = renderer.generate_current_frame()
    assert (actual_frame == expected_frame)


def test_ascii_system_renderer_should_generate_string_with_object_in_middle_if_object_is_in_middle():
    object = PhysicsObject(5, 0, 10)
    system = PhysicsSystem([object], [])
    renderer = Ascii1DPhysicsSystemRenderer(system, 1, 10, 0, 9)
    expected_frame = "     #    "
    actual_frame = renderer.generate_current_frame()
    assert (actual_frame == expected_frame)


def test_ascii_system_renderer_should_generate_blank_string_if_objects_are_outside_of_window():
    object_1 = PhysicsObject(-1, 0, 10)
    object_2 = PhysicsObject(10, 0, 10)
    system = PhysicsSystem([object_1, object_2], [])
    renderer = Ascii1DPhysicsSystemRenderer(system, 1, 10, 0, 9)
    expected_frame = "          "
    actual_frame = renderer.generate_current_frame()
    assert (actual_frame == expected_frame)


def test_ascii_system_renderer_should_scale_window_appropriately():
    object_1 = PhysicsObject(-1, 0, 10)
    object_2 = PhysicsObject(5000, 0, 10)
    system = PhysicsSystem([object_1, object_2], [])
    renderer = Ascii1DPhysicsSystemRenderer(system, 1, 25, -1, 5000)
    expected_frame = "#                       #"
    actual_frame = renderer.generate_current_frame()
    assert (actual_frame == expected_frame)
