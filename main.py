from robot import Robot
from environment import Environment
import math
import cv2 as cv

if __name__ == '__main__':
    robot = Robot()
    robot.set_left_speed(0)
    robot.set_right_speed(0)

    env = Environment()

    position = [int(env.level.shape[0] / 2), int(env.level.shape[1] / 2), -math.pi / 2]

    cv.namedWindow('simulation', cv.WINDOW_NORMAL)
    cv.resizeWindow('simulation', 600, 600)

    while (True):
        position = env.updatePosition(robot, position)
        frame = env.render(robot, position)
        cv.imshow('simulation', frame)

        key_flag = cv.waitKey(1) & 0xFF

        if key_flag == ord('a'):
            robot.set_left_speed(robot.get_left_speed() + 0.5)
        if key_flag == ord('z'):
            robot.set_left_speed(robot.get_left_speed() - 0.5)
        if key_flag == ord('s'):
            robot.set_right_speed(robot.get_right_speed() + 0.5)
        if key_flag == ord('x'):
            robot.set_right_speed(robot.get_right_speed() - 0.5)
        if key_flag == ord('b'):
            robot.set_right_speed(0)
            robot.set_left_speed(0)

        if key_flag == ord('p'):
            print(position)
        if key_flag == ord('q'):
            break

    cv.destroyAllWindows()
