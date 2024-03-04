import numpy as np
import cv2

# Loads the data as a VideoCapture format, which is really just
# an image sequence.
image_sequence = 'Delhi.mp4'
cap = cv2.VideoCapture(image_sequence)

# Load our cascade classifier from cars3.xml
car_cascade = cv2.CascadeClassifier('/home/aman/opncv_tutorials/cars3.xml')

# Reduce the number of frames to load.
number_of_frames_to_load = 500

for frame_id in range(number_of_frames_to_load):
    ret, image = cap.read()

    # Check if the video capture was successful
    if not ret:
        break

    # Crop so that only the roads remain, eliminates the distraction.
    image = image[120:, :-20]

    # Use Cascade Classifier to detect cars, may have to tune the
    # parameters for fewer false positives.
    cars = car_cascade.detectMultiScale(image, scaleFactor=1.008, minNeighbors=5)

    for (x, y, w, h) in cars:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

    print('Processing %d : cars detected : [%s]' % (frame_id, len(cars)))
    cv2.imshow('frame', image)
    cv2.waitKey(10)

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
