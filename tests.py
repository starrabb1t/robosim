from robot import Robot
from environment import Environment
import math
import time

if __name__ == '__main__':
    robot = Robot()
    robot.set_left_speed(1)
    robot.set_right_speed(1)

    env = Environment()

    position = [int(env.level.shape[0] / 2), int(env.level.shape[1] / 2), -math.pi / 2]

    t_start = time.time()
    for i in range(100):
        position = env.updatePosition(robot, position)
        frame = env.render(robot, position)
    print("pure python: " + str(int(1/(0.01*(time.time() - t_start)))) + " fps")
