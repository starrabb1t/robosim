from utils import *
import math

class Environment():

    def __init__(self, step_num, map_width, map_height):

        self.tau = 0.05
        self.level = getMap(step_num, map_width, map_height)

    #TODO: cythonize
    def updatePosition(self, robot, pos):
        rtob = robot.r / robot.b
        w_left = robot.get_left_speed()
        w_right = robot.get_right_speed()

        phi = pos[2] + (self.tau / 2) * (rtob) * (w_left - w_right)
        x = pos[0] + (robot.r / 2) * math.cos(phi) * (w_right + w_left) * self.tau
        y = pos[1] + (robot.r / 2) * math.sin(phi) * (w_right + w_left) * self.tau

        if self.isHit(robot, [x,y,phi]):
            return pos

        return [x, y, phi]

    def render(self, robot, pos):
        icon = rotate(robot.icon, -90-int(180 * (pos[2] / math.pi)))
        return drawOverlay(self.level, icon, np.array([pos[0], pos[1]], dtype=np.uint8))

    # TODO: cythonize
    def isHit(self,robot, pos):
        h, w, _ = robot.icon.shape  # Size of foreground
        rows, cols, _ = self.level.shape  # Size of background Image
        y, x = int(pos[0]), int(pos[1])  # Position of foreground/overlay image

        # loop over all pixels and apply the blending equation
        for i in range(h):
            for j in range(w):
                if (self.level[x + i][y + j][0] == 0) and (self.level[x + i][y + j][3] == 255):
                    return True

        return False