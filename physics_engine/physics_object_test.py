import pytest

from physics_engine.physics_object import PhysicsObject


def test_position_should_not_change_if_velocity_is_zero_regardless_of_position_and_delta_t():
    test_vel_x_0 = 0
    test_delta_ts = [0, 1, 2, 10, 20, 100]
    test_pos_xs = [0, 1, 2, 10, 20, 100]
    for test_delta_t in test_delta_ts:
        for test_pos_x_0 in test_pos_xs:
            test_obj = PhysicsObject(test_pos_x_0, test_vel_x_0)
            test_obj.update_pos(test_delta_t)
            test_pos_x_1 = test_obj.pos_x
            test_vel_x_1 = test_obj.vel_x
            assert (test_pos_x_1 == test_pos_x_0)
            assert (test_vel_x_1 == test_vel_x_0)


def test_position_should_update_by_velocity_times_delta_t():
    test_pos_x_0 = 5
    test_vel_x_0 = 10
    test_delta_t = 7
    expected_pos_x_1 = 75  # 5 + (10 * 7) = 75 (x0 + v0 * dt = x1)
    test_obj = PhysicsObject(test_pos_x_0, test_vel_x_0)
    test_obj.update_pos(test_delta_t)
    test_pos_x_1 = test_obj.pos_x
    assert (test_pos_x_1 == expected_pos_x_1)
