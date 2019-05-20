import math
import cv2 as cv
import numpy as np
import random

cimport numpy as np
cimport cython

UINT8 = np.uint8
ctypedef np.uint8_t UINT8_T

cdef class Environment():
    cdef float __tau
    cdef public np.ndarray level

    def __cinit__(self, int step_num=200, int map_width=10, int map_height=10):
        self.__tau = 0.05
        self.level = self.genMap(step_num, map_width, map_height)

    def updatePosition(self, robot, pos):
        w_left = robot.get_left_speed()
        w_right = robot.get_right_speed()

        phi = pos[2] + (self.__tau / 2) * (robot.rtob) * (w_left - w_right)
        x = pos[0] + (robot.wheel_radius / 2) * math.cos(phi) * (w_right + w_left) * self.__tau
        y = pos[1] + (robot.wheel_radius / 2) * math.sin(phi) * (w_right + w_left) * self.__tau

        if (self.isHit(robot.icon, y, x) == 1):
            return pos

        return [x, y, phi]

    @cython.boundscheck(False)
    @cython.wraparound(False)
    cpdef UINT8_T isHit(self, np.ndarray[UINT8_T, ndim=3] icon, int x, int y):
        cdef int h = icon.shape[0]
        cdef int w = icon.shape[1]
        cdef int rows = self.level.shape[0]
        cdef int cols = self.level.shape[1]
        cdef int i, j

        for i in range(h):
            for j in range(w):
                if (self.level[x + i][y + j][0] == 0) and (self.level[x + i][y + j][3] == 255):
                    return 1

        return 0

    @cython.boundscheck(False)
    @cython.wraparound(False)
    cdef np.ndarray[UINT8_T, ndim=3] drawOverlay(self, np.ndarray[UINT8_T, ndim=3] src, np.ndarray[UINT8_T, ndim=3] overlay, int x, int y):
        cdef np.ndarray result = src.copy()
        cdef int h = overlay.shape[0]
        cdef int w = overlay.shape[1]
        cdef int rows = result.shape[0]
        cdef int cols = result.shape[1]
        cdef int i, j
        cdef float alpha

        for i in range(h):
            for j in range(w):
                if x + i >= rows or y + j >= cols:
                    continue
                alpha = float(overlay[i][j][3] / 255.0)

                result[x + i][y + j] = alpha * overlay[i][j] + (1 - alpha) * result[x + i][y + j]
        return result

    def render(self, robot, pos):
        icon = self.rotate(robot.icon, -90 - int(180 * (pos[2] / math.pi)))
        return self.drawOverlay(self.level, icon, int(pos[1]), int(pos[0]))

    def rotate(self, img, angle):
        w = img.shape[1]
        h = img.shape[0]

        M = cv.getRotationMatrix2D((w / 2, h / 2), angle, 1)
        return cv.warpAffine(img, M, (w, h))

    def genMap(self, n, w, h):

        level = np.zeros((w, h, 4), np.uint8)
        level[:, :, 3] = 255 * np.ones((w, h))

        pos = [int(w / 2), int(h / 2)]

        for i in range(1, n):
            val = random.randint(1, 4)

            if val == 1:
                pos[0] += 1
            elif val == 2:
                pos[0] -= 1
            elif val == 3:
                pos[1] += 1
            else:
                pos[1] -= 1

            if pos[0] >= w:
                pos[0] = w - 1

            if pos[1] >= h:
                pos[1] = h - 1

            if pos[0] < 0:
                pos[0] = 0

            if pos[1] < 0:
                pos[1] = 0

            level[pos[0], pos[1], 0:3] = 255

        return cv.resize(level, (1000, 1000), interpolation=cv.INTER_NEAREST)
