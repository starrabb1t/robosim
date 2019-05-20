import cv2 as cv

class Robot():

    def __init__(self, icon, size):  # size is scalar (robot diameter)

        self.__max_speed = 2
        self.__error = 0.05

        self.icon = cv.imread(icon, cv.IMREAD_UNCHANGED)
        self.icon = cv.resize(self.icon, (size, size), interpolation=cv.INTER_NEAREST)

        self.size = size
        self.b = size / 2
        self.r = size / 3

        self.__w_left = 0  # left speed
        self.__w_right = 0  # right speed

    def set_left_speed(self, speed):
        self.__w_left = min(speed,self.__max_speed)

    def set_right_speed(self, speed):
        self.__w_right = min(speed,self.__max_speed)

    def get_left_speed(self):
        return (self.__w_left)  # + random.randint(int(self.error*self._w_left)))

    def get_right_speed(self):
        return (self.__w_right)  # + random.randint(int(self.error*self._w_right)))

    #TODO: cythonize
    """
        def get_range(self, angle, level, pos):
        k = math.tan(pos + math.pi*(angle/180))
        rows, cols, _ = level.shape  # Size of background Image
        y, x = int(pos[0]), int(pos[1])  # Position of foreground/overlay image

        for i in range(200):
    """

