Laser Pointer Detection Using OpenCV
This Python project uses OpenCV to detect a laser pointer in a video feed from a webcam. The application applies color filtering (using the HSV color space) to isolate the laser pointer based on its color and detects its position. The project is capable of identifying the laser pointer up to a distance of 2 meters, with a tolerance of 10 cm.

Features
Detects laser pointers based on color and intensity.
Capable of recognizing the laser within a 2-meter range.
Simple to run and adaptable to different types of laser pointers.
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x
OpenCV (cv2)
NumPy (numpy)
To install the required dependencies, run the following command:

pip install opencv-python numpy
How to Run
Clone the repository:

git clone https://github.com/jucie-yue/LaserPointerDetection.git
Navigate to the project directory:

cd LaserPointerDetection
Run the Python script:

python laser_detection.py
Press q to quit the application.

Future Improvements
Implement distance calculation using camera calibration.
