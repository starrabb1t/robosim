from robot import Robot
from environment import Environment
from utils import *
import math

if __name__ == '__main__':

    myRobot = Robot('robot.png', 50)
    myRobot.set_left_speed(0)
    myRobot.set_right_speed(0)

    env = Environment(200,10,10)

    step_num = 200
    map_width = 10
    map_height = 10


    position = [int(env.level.shape[0] / 2), int(env.level.shape[1] / 2), -math.pi/2]
    cv.namedWindow('simulation', cv.WINDOW_NORMAL)
    cv.resizeWindow('simulation', 600, 600)

    while (True):
        position = env.updatePosition(myRobot, position)
        frame = env.render(myRobot, position)
        cv.imshow('simulation', frame)

        #time.sleep(0.1)

        key_flag = cv.waitKey(1) & 0xFF

        if key_flag == ord('a'):
            myRobot.set_left_speed(myRobot.get_left_speed() + 0.1)
        if key_flag == ord('z'):
            myRobot.set_left_speed(myRobot.get_left_speed() - 0.1)
        if key_flag == ord('s'):
            myRobot.set_right_speed(myRobot.get_right_speed() + 0.1)
        if key_flag == ord('x'):
            myRobot.set_right_speed(myRobot.get_right_speed() - 0.1)
        if key_flag == ord('b'):
            myRobot.set_right_speed(0)
            myRobot.set_left_speed(0)

        if key_flag == ord('p'):
            print(position)
        if key_flag == ord('q'):
            break

    cv.destroyAllWindows()