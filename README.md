# AttendanceProject

Simple and Easy to use Attendance Taking System using the face-recognition library.
Video Demo: https://drive.google.com/file/d/1AcmbCe-Z6q4x8TFPQM2Y7UduuAd6pR5L/view?usp=sharing

# Usage

The following guide assumes Python 3.x to be the default python runtime environment.

1. Clone the repository to your current working directory.

`git clone https://github.com/jiayi1129/AttendanceProject.git`

2. Install a working C++ compiler, we used the one from Microsoft Visual Studio 2019.

link: https://visualstudio.microsoft.com/downloads/

NOTE: you have to go into Microsoft Visual Studio after its been installed and search for
C++ compiler and download it

3. Install Cmake

link: https://cmake.org/download/

4. Install the required dependencies.

This will install the cv2 and numpy library.

`pip install opencv-python`

This will download Dlib.

`pip install dlib`

This will install the face-recognition library.

`pip install face-recognition`

5. Input images you want to train into the `ImagesAttendance` folder 


Note `Bill Gates.jpg`, `Elon Musk.jpg` and `Jack Ma.jpg` are placed inside the folder as example, running the program and showing an image of those 3 people will work as well. 
Input image should only contain one face and the file name should correspond to the label for the person inside the image.

6. Run the program

`python AttendanceProject.py`

Webcam will be activated and a bounding box as well as a label will be drawn on the faces inside `ImagesAttendance` folder.
Check the Attendance.csv file, your name (as configured on the filename) along with the time of check in will be recorded on the csv.
Note that your attendance will only be recorded once to avoid overflow in the csv file.
