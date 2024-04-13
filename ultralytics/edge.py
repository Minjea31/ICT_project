import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_image_edges_coordinates(image_path):
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (640, 640), interpolation=cv2.INTER_AREA)
    grayscale = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(grayscale, 240, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea)
    edge_coordinates = [tuple(point[0]) for point in largest_contour]

    return edge_coordinates

def normalize_coordinates(edge_coordinates):
    x_coords = [coord[0] for coord in edge_coordinates]
    y_coords = [coord[1] for coord in edge_coordinates]

    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)

    normalized_coordinates = [(float(x - x_min) / (x_max - x_min), float(y - y_min) / (y_max - y_min)) for x, y in edge_coordinates]

    return normalized_coordinates

def draw_red_marks_and_green_keypoints_on_frame(frame, normalized_coordinates, keypoints): #arg:circle_keypoints
    resized_frame = cv2.resize(frame, (640, 640))
    points = [((int(x * 640), int(y * 640))) for x, y in normalized_coordinates]

    for i in range(1, len(points)):
        cv2.line(resized_frame, points[i - 1], points[i], (0, 0, 255), thickness=4)

    for point in keypoints:
        cv2.circle(resized_frame, point, 20, (0, 255, 0), 2)  
    
    return resized_frame
