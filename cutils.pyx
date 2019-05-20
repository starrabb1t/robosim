import cv2 as cv
import random

import numpy as np
cimport numpy as np

cimport cython

UINT8 = np.uint8
ctypedef np.uint8_t UINT8_t

UINT32 = np.uint32
ctypedef np.uint32_t UINT32_t

@cython.boundscheck(False)
@cython.wraparound(False)
def getMap(int n, int w, int h):
    cdef np.ndarray level = np.zeros([w, h, 4], dtype=UINT8)
    level[:, :, 3] = 255 * np.ones([w, h], dtype=UINT8)

    cdef np.ndarray pos = np.array([int(w / 2), int(h / 2)])
    cdef UINT32_t i, val

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

# function to overlay a transparent image on background.
@cython.boundscheck(False)
@cython.wraparound(False)
def drawOverlay(np.ndarray[UINT8_t, ndim=3] src, np.ndarray[UINT8_t, ndim=3] overlay,
                np.ndarray[UINT8_t, ndim=1] pos = np.array([0,0])):

    cdef np.ndarray result = src.copy()

    cdef UINT32_t h = overlay.shape[0]  # Size of foreground
    cdef UINT32_t w = overlay.shape[1]  # Size of foreground

    cdef UINT32_t rows = result.shape[0]  # Size of background Image
    cdef UINT32_t cols = result.shape[1]  # Size of background Image

    cdef UINT32_t y = int(pos[0])  # Position of foreground/overlay image
    cdef UINT32_t x = int(pos[1])  # Position of foreground/overlay image

    cdef float alpha

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = overlay[i][j][3] / 255.0 # read the alpha channel

            result[x + i][y + j] = alpha * overlay[i][j] + (1 - alpha) * result[x + i][y + j]
    return result

def rotate(img, angle):
    w = img.shape[1]
    h = img.shape[0]

    M = cv.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    return cv.warpAffine(img, M, (w, h))
