import cv2 as cv


class Robot():

    def __init__(self, icon='robot.png', size=50):
        self.__max_speed = 5

        self.icon = cv.imread(icon, cv.IMREAD_UNCHANGED)
        self.icon = cv.resize(self.icon, (size, size), interpolation=cv.INTER_NEAREST)

        self.size = size
        self.base = size / 2
        self.wheel_radius = size / 10
        self.rtob = self.wheel_radius/self.base

        self.__wheel_left_speed = 0
        self.__wheel_right_speed = 0

    def set_left_speed(self, speed):
        self.__wheel_left_speed = min(speed, self.__max_speed)

    def set_right_speed(self, speed):
        self.__wheel_right_speed = min(speed, self.__max_speed)

    def get_left_speed(self):
        return (self.__wheel_left_speed)  # + random.randint(int(self.error*self._w_left)))

    def get_right_speed(self):
        return (self.__wheel_right_speed)  # + random.randint(int(self.error*self._w_right)))

    """
    def get_range(self, angle, level, pos):
        k = math.tan(pos + math.pi*(angle/180))
        rows, cols, _ = level.shape  # Size of background Image
        y, x = int(pos[0]), int(pos[1])  # Position of foreground/overlay image

        #for i in range(200):
    """
