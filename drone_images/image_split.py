import cv2
import numpy as np

im = cv2.imread("satellite_image.jpg")
M = im.shape[0]//3 # Rows
N = im.shape[1]//5 # Columns
tiles = [(f"{int(x/M)}{int(y/N)}.jpg", im[x:x+M,y:y+N]) for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]

print(len(tiles))
print(im.shape)
"""
cv2.imshow("", im)
cv2.waitKey()
for i, t in tiles:
    print(t.shape)
    cv2.imshow("", t)
    cv2.waitKey()
"""
tshape = tiles[0][1].shape
canvas = np.zeros((tshape[0] * 3, tshape[1] * 5, tshape[2]), dtype = "uint8")
print(canvas.shape)
for x in range(0, canvas.shape[0], tshape[0]):
    print(f"x = {x}")
    for y in range(0, canvas.shape[1], tshape[1]):
        print(f"y = {y}")
        print(f"coords: {int(y/tshape[1]) + int((x*5)/tshape[0])}")
        print(f"{tiles[int(y/tshape[1]) + int((x*5)/tshape[0])][0]}")
        canvas[x:x+M,y:y+N] = tiles[int(y/tshape[1]) + int((x*5)/tshape[0])][1]
        cv2.imshow("", canvas)
        cv2.waitKey()
cv2.imshow("", im)
cv2.waitKey()
print(not False in (im == canvas))
"""
for name, image in tiles:
    cv2.imwrite(name, image)
"""
