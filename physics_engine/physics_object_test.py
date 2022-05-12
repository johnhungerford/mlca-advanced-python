import pytest

from physics_engine.physics_object import PhysicsObject, acceleration_from_force_and_mass


def test_position_should_not_change_if_velocity_and_force_are_zero_regardless_of_position_and_delta_t():
    test_mass = 10
    test_vel_x_0 = 0
    test_delta_ts = [0, 1, 2, 10, 20, 100]
    test_pos_xs = [0, 1, 2, 10, 20, 100]
    for test_delta_t in test_delta_ts:
        for test_pos_x_0 in test_pos_xs:
            test_obj = PhysicsObject(test_pos_x_0, test_vel_x_0, test_mass)
            test_obj.update_state(test_delta_t, 0)
            actual_pos_x_1 = test_obj.pos_x
            actual_vel_x_1 = test_obj.vel_x
            assert (actual_pos_x_1 == test_pos_x_0)
            assert (actual_vel_x_1 == test_vel_x_0)


def test_position_should_update_by_velocity_times_delta_t_if_no_force():
    test_mass = 10
    test_pos_x_0 = 5
    test_vel_x_0 = 10
    test_delta_t = 7
    expected_pos_x_1 = 75  # 5 + (10 * 7) = 75 (x0 + v0 * dt = x1)
    test_obj = PhysicsObject(test_pos_x_0, test_vel_x_0, test_mass)
    test_obj.update_state(test_delta_t, 0)
    actual_pos_x_1 = test_obj.pos_x
    assert (actual_pos_x_1 == expected_pos_x_1)

def test_position_should_update_by_velocity_times_delta_t_if_there_is_force():
    test_mass = 10
    test_pos_x_0 = 5
    test_vel_x_0 = 10
    test_force_x_0 = 1000
    test_delta_t = 7
    expected_pos_x_1 = 75  # 5 + (10 * 7) = 75 (x0 + v0 * dt = x1)
    test_obj = PhysicsObject(test_pos_x_0, test_vel_x_0, test_mass)
    test_obj.update_state(test_delta_t, test_force_x_0)
    actual_pos_x_1 = test_obj.pos_x
    assert (actual_pos_x_1 == expected_pos_x_1)


def acceleration_from_force_and_mass_should_correctly_calculate_acceleration():
    test_mass = 2
    test_force = 50
    expected_acceleration = 25
    assert(acceleration_from_force_and_mass(test_force, test_mass) == expected_acceleration)


def test_velocity_should_update_by_force_divided_by_mass_times_delta_t_if_there_is_force():
    test_mass = 10
    test_pos_x_0 = 0
    test_vel_x_0 = 5
    test_force_x_0 = 100
    test_delta_t = 5
    expected_pos_x_1 = 25  # delt_t * vel_x_0 + pos_x_0
    expected_vel_x_1 = 50  # delta_t * (force / mass) + vel_x_0
    test_obj = PhysicsObject(test_pos_x_0, test_vel_x_0, test_mass)
    test_obj.update_state(test_delta_t, test_force_x_0)
    actual_pos_x_1 = test_obj.pos_x
    actual_vel_x_1 = test_obj.vel_x
    assert (actual_pos_x_1 == expected_pos_x_1)
    assert (actual_vel_x_1 == expected_vel_x_1)
