import cv2 as cv
import numpy as np
import random

def getMap(n,w,h):

    level = np.zeros((w,h,4), np.uint8)
    level[:,:,3] = 255*np.ones((w,h))

    pos = [int(w/2),int(h/2)]

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
            pos[0] = w-1

        if pos[1] >= h:
            pos[1] = h-1

        if pos[0] < 0:
            pos[0] = 0

        if pos[1] < 0:
            pos[1] = 0

        level[pos[0],pos[1],0:3] = 255

    return cv.resize(level, (1000,1000), interpolation=cv.INTER_NEAREST)


# function to overlay a transparent image on background.
def drawOverlay(src, overlay, pos=(0, 0)):

    result = src.copy()
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = result.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image

    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel

            result[x + i][y + j] = alpha * overlay[i][j] + (1 - alpha) * result[x + i][y + j]
    return result


def rotate(img, angle):
    w = img.shape[1]
    h = img.shape[0]

    M = cv.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    return cv.warpAffine(img, M, (w, h))