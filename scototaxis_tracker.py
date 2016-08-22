import cv2
import numpy as np

'''
My attempt to create a scototaxis tracker. Contains some potentially useful functions but I was unable to actually get it to work, as the signal and noise are of similar magnitudes.
'''

def invert(image):
    image = (255-image)
    return image

def increase_brightness(frame):
    frame = frame + 100
    # frame = np.clip(frame, 0, 255)
    frame[frame > 255] = 255
    return frame

# 1.4 is a good place to start for amount
def increase_contrast(frame, amount):
    x = np.multiply(frame,np.full(img.shape, amount))
    x = x.astype(np.uint8)
    x = np.clip(x, 0, 255)
    return x

def getBackgroundImage(vid, numFrames):
    """compute an 'average' photo of the first numFrames frames from the video."""
    print "\n\n\n\n-----------------------\n\ninitializing background detection\n"

    # set a counter
    i = 0
    _, frame = vid.read()
    # initialize an empty array the same size of the pic to update
    update = np.float32(frame)

    # loop through the first numFrames frames to get the background image
    while i < numFrames:
        # grab a frame
        _, frame = vid.read()

        # main function
        cv2.accumulateWeighted(frame, update, 0.01)
        final = cv2.convertScaleAbs(update)
        # increment the counter
        i += 1

        # print something every 100 frames so the user knows the gears are
        # grinding
        if i % 100 == 0:
            print "detecting background -- on frame " + str(i) + " of " + str(numFrames)
    return final

def transform(frame):
    # img[img > 50] = 0
    img = np.multiply(frame, np.full(frame.shape, 10))
    img[img > 255] = 255
    img = img.astype(np.uint8)
    # img = cv2.blur(img, (3,3))
    # grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # ret,thresh = cv2.threshold(grey,100,255,cv2.THRESH_BINARY)
    return img

path = "xnlab4Smale.avi"

# get an image, write it
cap = cv2.VideoCapture(path)
# ret = cap.set(1,100)
ret, img = cap.read()
cv2.imwrite("original.jpg", img)

# increase contrast, write it
con = increase_contrast(img)
cv2.imwrite("contrast.jpg", con)

# increase brightness, write it
bright = increase_brightness(con)
cv2.imwrite("bright.jpg", bright)


fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
out = cv2.VideoWriter("inverted_video.mp4", fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))

# mul = np.full(img.shape, 1.2)

img = getBackgroundImage(cap, 400)
cap = cv2.VideoCapture(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray[gray > 30] = 0
gray = np.multiply(gray, np.full(gray.shape, 15))
gray[gray > 255] = 0
t = gray.astype(np.uint8)
t = cv2.morphologyEx(t, cv2.MORPH_OPEN, np.ones((1,1),np.uint8))
initial = t

cap.set(1, 1000)
while cap.get(1) < 1450:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # bright = increase_brightness(img)
    # contrast = increase_contrast(bright)
    # ret,thresh = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),200,255,cv2.THRESH_BINARY_INV)
    # diff = cv2.subtract(contrast, initial)
    # img = invert(img)
    # gray = cv2.blur(gray, (5,5))
    gray[gray > 20] = 0
    gray = np.multiply(gray, np.full(gray.shape, 15))
    gray[gray > 255] = 0
    t = gray.astype(np.uint8)
    t = cv2.blur(t, (7,7))
    t = cv2.morphologyEx(t, cv2.MORPH_OPEN, np.ones((1,1),np.uint8))

    # take difference image
    diff = cv2.subtract(t, initial)
    # diff = cv2.dilate(diff,np.ones((1,1),np.uint8),iterations = 1)

    ret,thresh = cv2.threshold(diff,5,255,cv2.THRESH_BINARY)

    # find contours
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    potential_contours = []
    for c in contours:
        area = cv2.contourArea(c)
        if area > 5 and area < 100:
            potential_contours.append(c)

    cv2.drawContours(img, potential_contours, -1, (100,200,60), -1)

    cv2.imshow("thesh", diff)
    cv2.waitKey(1)
    if cap.get(1) % 100 == 0:
        cv2.imwrite("frame_{}.jpg".format(int(cap.get(1))), thresh)
    # to write to a video
    diff = np.repeat(diff[:, :, np.newaxis], 3, axis=2)
    out.write(diff)
    print "frame {}".format(cap.get(1))
out.release()
