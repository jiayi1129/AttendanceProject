# AttendanceProject

Simple and Easy to use Attendance Taking System using the face-recognition library.

# Usage

The following guide assumes Python 3.x to be the default python runtime environment.

1. Clone the repository to your current working directory.

`git clone https://github.com/jiayi1129/AttendanceProject.git`

2. Install the required dependencies.

This will install the cv2 and numpy library.

`pip install opencv-python`

This will install the face-recognition library.

`pip install face-recognition`

3. Input images you want to train into the `ImagesAttendance` folder 


Note `Bill Gates.jpg`, `Elon Musk.jpg` and `Jack Ma.jpg` are placed inside the folder as example, running the program and showing an image of those 3 people will work as well. 
Input image should only contain one face and the file name should correspond to the label for the person inside the image.

4. Run the program

`python AttendanceProject.py`

Webcam will be activated and a bounding box as well as a label will be drawn on the faces inside `ImagesAttendance` folder.
Check the Attendance.csv file, your name (as configured on the filename) along with the time of check in will be recorded on the csv.
Note that your attendance will only be recorded once to avoid overflow in the csv file.
