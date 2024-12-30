import cv2
from hand_guestures import detect_thumbs_up
def main():
    print("Welcome to PIVOT!")
    # Placeholder for camera input handling
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    print("Camera opened successfully. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        frame, thumbs_up = detect_thumbs_up(frame) # Get the frame and the thumbs_up boolean

        if thumbs_up:
            print("Thumbs up detected!") # Print to the console
            # You could trigger other actions here, like saving an image,
            # sending a signal, etc.

        cv2.imshow("PIVOT - Camera Feed", frame)


        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
