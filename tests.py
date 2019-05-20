import cutils
import utils

import time
import math
import numpy as np
import cv2 as cv

icon = cv.imread('robot.png', cv.IMREAD_UNCHANGED)
icon = cv.resize(icon, (50, 50), interpolation=cv.INTER_NEAREST)

#pure python
print("pure python")

t_start = time.time()
level = utils.getMap(200, 10, 10)
print("getMap: " + str(time.time() - t_start))

position = np.array([int(level.shape[0] / 2), int(level.shape[1] / 2), -math.pi/2], dtype=np.uint8)
t_start = time.time()
utils.drawOverlay(level, icon, position)
print("drawOverlay: " + str(time.time() - t_start))

print()

#cython
print("cython")

t_start = time.time()
clevel = cutils.getMap(200, 10, 10)
print("getMap: " + str(time.time() - t_start))

cposition = np.array([int(clevel.shape[0] / 2), int(clevel.shape[1] / 2), -math.pi/2], dtype=np.uint8)
t_start = time.time()
cutils.drawOverlay(clevel, icon, cposition)
print("drawOverlay: " + str(time.time() - t_start))


#cv.imshow('frame', hello.look(arr))
#cv.waitKey(0)
#cv.destroyyAllWindows()