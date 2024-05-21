import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import colors
from Models_Constants.FDM_Parameters import *
from Models_Archive.FDM_Models import FireDynamics

image_path = "DataSet\Sim_data.jpg"
area_image = cv2.imread(image_path)


def get_green_filtered_image(area_image):
    hsv = cv2.cvtColor(area_image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, (36, 25, 25), (70, 255, 255))
    imask = mask > 0
    green = np.zeros_like(area_image, np.uint8)
    green[imask] = area_image[imask]
    return green


def get_edged_image(area_image):
    gray = cv2.cvtColor(area_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5)
    edges = cv2.Canny(blurred, 0, 255)
    return edges


green = get_green_filtered_image(area_image)
edged = get_edged_image(green)

dim = area_image.shape
size_L = dim[0]
size_B = dim[1]

IGNITION_Y = 1552
IGNITION_X = 350
IGNITION_POINTZ = []
for param in range(100):
    IGNITION_POINTZ.append((IGNITION_X + param, IGNITION_Y - param))
    # IGNITION_POINTZ.append((IGNITION_X - param, IGNITION_Y + param))
    # IGNITION_POINTZ.append((IGNITION_X + param, IGNITION_Y + param))
    # IGNITION_POINTZ.append((IGNITION_X - param, IGNITION_Y - param))

processed_matrix = np.zeros((size_L, size_B))

for point in IGNITION_POINTZ:
    processed_matrix[point[0], point[1]] = FIRE
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (point[0], point[1])
    fontScale = 1
    color = (255, 0, 0)
    thickness = 1
    image = cv2.putText(
        processed_matrix,
        "FIRE",
        org,
        font,
        fontScale,
        color,
        thickness,
        cv2.LINE_AA,
    )

for l in range(size_L - 1):
    for b in range(size_B - 1):
        if edged[l][b] == 255:
            processed_matrix[l][b] = FUEL
            for dx, dy in NEIGHBOUR:
                if processed_matrix[l + dx][b + dy] == FIRE:
                    try:
                        processed_matrix[l][b] = FIRE
                        processed_matrix[l + 10][b] = FIRE
                        # need to add fear of boundary for fire spread
                        # print("FIRE")

                        font = cv2.FONT_HERSHEY_SIMPLEX
                        org = (l, b)
                        fontScale = 5
                        color = (255, 0, 0)
                        thickness = 2
                        image = cv2.putText(
                            processed_matrix,
                            "FIRE",
                            org,
                            font,
                            fontScale,
                            color,
                            thickness,
                            cv2.LINE_AA,
                        )
                    except:
                        pass


plt.imshow(processed_matrix)
plt.show()
