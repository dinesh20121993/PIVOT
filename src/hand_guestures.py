import cv2
import numpy as np

def detect_thumbs_up(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    thumbs_up_detected = False

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

            x, y, w, h = cv2.boundingRect(approx) # Get bounding box coordinates

            aspect_ratio = float(w) / h

            if aspect_ratio > 1.5:
                cv2.drawContours(frame, [approx], -1, (0, 255, 0), 3) #draw green contours
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw blue rectangle
                cv2.putText(frame, "Thumbs Up", (x,y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2) #blue text
                thumbs_up_detected = True
                break

    return frame, thumbs_up_detected

