import cv2
import numpy as np

# Function to detect the laser pointer in the video feed
def detect_laser(frame):
    # Convert the frame to HSV color space for better color detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the HSV color range for detecting the red laser pointer
    lower_red = np.array([160, 100, 100])
    upper_red = np.array([179, 255, 255])

    # Create a mask for red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Apply GaussianBlur to reduce noise
    mask = cv2.GaussianBlur(mask, (15, 15), 0)

    # Morphological operations to remove noise and close gaps
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If a contour is found, assume it's the laser pointer
    if len(contours) > 0:
        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea)

        # Get the bounding box around the laser spot
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Calculate the center of the bounding box
        center_x = x + w // 2
        center_y = y + h // 2

        # Draw the bounding box and center point
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

        # Estimate and display the distance (This is a placeholder value; camera calibration can improve it)
        distance_estimation = 200  # Placeholder for distance
        cv2.putText(frame, f"Distance: {distance_estimation} cm", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    return frame

# Main loop to process video from webcam
def main():
    # Capture video from the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Detect the laser pointer in the frame
        output_frame = detect_laser(frame)

        # Display the output
        cv2.imshow("Laser Pointer Detection", output_frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
