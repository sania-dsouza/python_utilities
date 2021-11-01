from imutils import paths  # imutils includes opencv functions
import face_recognition
import pickle
import cv2 as cv
import os
import time

# get paths of each file in folder named Images
# Images here that contains data(folders of various people)
imagePath = list(paths.list_images('Images'))
kEncodings = []
kNames = []

# loop over the image paths
for (i, ip) in enumerate(imagePath):
    # extract the person name from the image path
    name = ip.split(os.path.sep)[-2]
    # load the input image and convert it from BGR
    image = cv.imread(ip)
    rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model='hog')

    # compute the facial embedding for the face
    encodings = face_recognition.face_encodings(rgb, boxes)

    # loop over the encodings
    for encoding in encodings:
        kEncodings.append(encoding)
        kNames.append(name)

# save encodings along with their names in dictionary data
data = {"encodings": kEncodings, "names": kNames}

# use pickle to save data into a file for later use
f = open("../face_enc", "wb")   # to open file in write mode

f.write(pickle.dumps(data))

f.close()  # to close file


# ------------------------------------------------------------------------------------

# to find path of xml file containing haarCascade file
cfp = os.path.dirname(cv.__file__) + "/data/haarcascade_frontalface_alt2.xml"
print(cfp)

# load the haar cascade in the cascade classifier
fc = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
print(fc)

# load the known faces and embeddings saved in last file
data = pickle.loads(open('../face_enc', "rb").read())

# Find path to the image you want to detect face and pass it here
image = cv.imread('../aaron.jpg')
#cv.imshow('test', image)


rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# convert image to Greyscale for HaarCascade
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
faces = fc.detectMultiScale(gray,
    minSize=(60, 60))

# the facial embeddings for face in input
encodings = face_recognition.face_encodings(rgb)
names = []

# loop over the facial embeddings in case
# we have multiple embeddings for multiple façes
for encoding in encodings:
    # Compare encodings with encodings in data["encodings"]
    # Matches contain array with boolean values True and False
    matches = face_recognition.compare_faces(data["encodings"], encoding)

# set name =unknown if no encoding matches
name = "Unknown"
# check to see if we have found a match
if True in matches:
    # Find positions at which we get True and store them
    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
    count = {}

# loop over the matched indexes and maintain a count for
# each recognized face face
for i in matchedIdxs:
    # Check the names at respective indexes we stored in matchedIdxs
    name = data["names"][i]
    # increase count for the name we got
    count[name] = count.get(name, 0) + 1
    # set name which has highest count
    name = max(count, key=count.get)
    # will update the list of names
    names.append(name)

# do loop over the recognized faces
for ((x, y, w, h), name) in zip(faces, names):
    # rescale the face coordinates
    # draw the predicted face name on the image
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.putText(image, name, (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

cv.imshow("Frame", image)
k = cv.waitKey(0)
