import numpy as np
import cv2

original_points = np.float32([[23,23],[29,40],[50,60]])
current_points = np.float32([[45,45,],[39,60],[20,20]])

Affine_Matrix = cv2.getAffineTransform(original_points, current_points)
print(Affine_Matrix)
