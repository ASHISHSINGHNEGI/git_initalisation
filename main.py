# Import OpenCV2 for image processing
from tkinter import * 
import cv2
import os
from tkinter import *

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


face_id=input('enter your id')

def img_capturing():
	# Start capturing video 
	vid_cam = cv2.VideoCapture(0)

	# Detect object in video stream using Haarcascade Frontal Face
	face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

	# Initialize sample face image
	count = 0

	assure_path_exists("dataset/")

	# Start looping
	while(True):

	    # Capture video frame
	    _, image_frame = vid_cam.read()

	    # Convert frame to grayscale
	    gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)

	    # Detect frames of different sizes, list of faces rectangles
	    faces = face_detector.detectMultiScale(gray, 1.3, 5)

	    # Loops for each faces
	    for (x,y,w,h) in faces:

	        # Crop the image frame into rectangle
	        cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
	        
	        # Increment sample face image
	        count += 1

	        # Save the captured image into the datasets folder
	        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

	        # Display the video frame, with bounded rectangle on the person's face
	        cv2.imshow('frame', image_frame)

	    # To stop taking video, press 'q' for at least 100ms
	    if cv2.waitKey(100) & 0xFF == ord('q'):
	        break

	    # If image taken reach 100, stop taking video
	    elif count>=30:
	        print("Successfully Captured")
	        break

	# Stop video
	vid_cam.release()

	# Close all started windows
	cv2.destroyAllWindows()



def std_registration():
    tkWindow = Tk()
    tkWindow.geometry('500x500')
    tkWindow.title('student Registration')


    Label(tkWindow,text='Rollno').grid(row=0, sticky=W)
    v=StringVar()
    idlabelinput=Entry(tkWindow , textvariable=v).grid(row=0)
    face_id=v.get()
    print(face_id)

    Label(tkWindow, text="name" ).grid(row=1, sticky=W)
    name=StringVar()
    namelabelInput=Entry(tkWindow, textvariable=name ).grid(row=1)
    face_name=name.get()

    next_button=Button(tkWindow,text='image Capturing', command=img_capturing ).grid(row=2)
    #cancel_button=Button(tkWindow, text='cancel', command=call_uipage ).pack()

    tkWindow.mainloop()



std_registration()