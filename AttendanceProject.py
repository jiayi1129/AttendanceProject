import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import multiprocessing as mp

path = 'ImagesAttendance'
images = []
classNames = []
for cl in os.listdir(path):
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    # get names from filename (without the .*)
    classNames.append(os.path.splitext(cl)[0])


# helper function to generate encoding for image passed in
# use the face recognition library to generate 128-dimension face encodings
def get_encoding_for_image(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    encoding = face_recognition.face_encodings(img)[0]
    return encoding


# Parallel processing to generate encodings for all input images
def get_encoding_for_all_images(images):
    pool = mp.Pool()
    encoding_list = pool.map(get_encoding_for_image, images)
    return encoding_list


# helper function to mark attendance of student
# if student is already present, then don't need to mark again
def mark_attendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


# helper function to predict personnel in image based on video stream
def predict_from_video_stream(encoding_list_known):
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        # get all the bounding boxes of the faces in the current frame
        facesCurrFrame = face_recognition.face_locations(imgS)
        # get all the 128-dimension face encodings for all the faces in the current frame
        encodesCurrFrame = face_recognition.face_encodings(imgS, facesCurrFrame)

        # for each face detected in the frame
        for encodeFace, faceLoc in zip(encodesCurrFrame, facesCurrFrame):
            # check if the encodings of this face matches any known encodings
            matches = face_recognition.compare_faces(encoding_list_known, encodeFace)
            # get the 'distance' between this face encoding and our known faces encodings
            faceDis = face_recognition.face_distance(encoding_list_known, encodeFace)
            # find the index which has the least 'distance' (best match)
            matchIndex = np.argmin(faceDis)

            # if the matches with the index of least 'distance' is a match
            if matches[matchIndex]:
                # find the name of this student from the index
                name = classNames[matchIndex].upper()
                # scale the bounding box to fit the input video stream image
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                # draw the rectangle and label the rectangle with the appropriate student name
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                # we mark the attendance here
                mark_attendance(name)

        cv2.imshow('Webcam', img)
        cv2.waitKey(1)


if __name__ == '__main__':
    # Learning step to get 128-dimension encodings of all known personnel in
    print('Started Encoding')
    encoding_list_known = get_encoding_for_all_images(images)
    print('Encoding Complete')

    # Testing step to check if the 128-dimension encodings of the known personnel
    # matches the 128-dimension encodings of the faces detected in video stream
    print('Started Video Stream')
    predict_from_video_stream(encoding_list_known)