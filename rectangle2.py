#draw a rectangle

import cv2
import numpy as np
import argparse
import time
import pandas as pd

events = [i for i in dir(cv2) if 'EVENT' in i]

drawing = False # true if mouse is pressed

ix,iy = -1,-1

# mouse callback function

def draw_circle(event,x,y,flags,param):
#tank edge (purple)
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 10, (100,0,100), -1) #purple
        drawing = True
        ix,iy = x,y
        tankstart = np.array([x,y])
        np.savetxt('mydata'+ name[0] + '.csv',tankstart)
        print tankstart
        print "TANK edge START position shown above (upper left)"

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y), 1, (0,0,0), -1) #black

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(100,0,100),5) #purple
        tankend = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, tankend)
        f_handle.close()
        print tankend
        print "TANK edge END position shown above (lower right)"

def draw_circle2(event,x,y,flags,param):
#top mirror (light blue)
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 10, (255,255,0), -1) #lightblue
        drawing = True
        ix,iy = x,y
        topmirrorstart = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, topmirrorstart)
        f_handle.close()

        print topmirrorstart
        print "top mirror start position shown above (upper left)"

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y), 1, (0,0,0), -1) #black


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(255,255,0),5) #lightblue
        topmirrorend = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, topmirrorend)
        f_handle.close()

        print topmirrorend
        print "top mirror end position shown above (lower right)"

def draw_circle3(event,x,y,flags,param):
#bottom mirror (light blue)
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 10, (255,255,140), -1) #lightblue
        drawing = True
        ix,iy = x,y
        bottommirrorstart = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, bottommirrorstart)
        f_handle.close()

        print bottommirrorstart
        print "bottom mirror start position shown above (upper left)"

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y), 1, (0,0,0), -1) #black


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(255,255,140),5) #lightblue
        bottommirrorend = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, bottommirrorend)
        f_handle.close()

        print bottommirrorend
        print "bottom mirror end position shown above (lower right)"

def draw_circle4(event,x,y,flags,param):
#left target (red)
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 10, (0,0,255), -1) #red
        drawing = True
        ix,iy = x,y
        leftscreenstart = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, leftscreenstart)
        f_handle.close()

        print leftscreenstart
        print "left screen start position shown above (upper left)"

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y), 1, (0,0,0), -1) #black


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),5) #red
        leftscreenend = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, leftscreenend)
        f_handle.close()

        print leftscreenend
        print "left screen end position shown above (lower right)"

def draw_circle5(event,x,y,flags,param):
#right target (red)
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 10, (0,60,200), -1) #red
        drawing = True
        ix,iy = x,y
        rightscreenstart = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, rightscreenstart)
        f_handle.close()

        print rightscreenstart
        print "right screen start position shown above (upper left)"

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y), 1, (0,0,0), -1) #black


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,60,255),5) #red
        rightscreenend = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, rightscreenend)
        f_handle.close()

        print rightscreenend
        print "right screen end position shown above (lower right)"

def draw_circle6(event,x,y,flags,param):
#top thigmotaxis box (peach)
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 10, (0,255,0), -1) #peach
        drawing = True
        ix,iy = x,y
        topthigmostart = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, topthigmostart)
        f_handle.close()

        print topthigmostart
        print "top thigmotaxis start position shown above (upper left)"

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y), 1, (0,0,0), -1) #black


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),5) #peach
        topthigmoend = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, topthigmoend)
        f_handle.close()

        print topthigmoend
        print "top thigmotaxis end position shown above (lower right)"

def draw_circle7(event,x,y,flags,param):
#top thigmotaxis box (peach)
    global ix,iy,drawing,mode
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y), 10, (100,255,0), -1) #peach
        drawing = True
        ix,iy = x,y
        bottomthigmostart = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, bottomthigmostart)
        f_handle.close()

        print bottomthigmostart
        print "bottom thigmotaxis start position shown above (upper left)"

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y), 1, (0,0,0), -1) #black


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,(ix,iy),(x,y),(100,255,0),5) #peach
        bottomthigmoend = np.array([x,y])

        f_handle = file('mydata'+ name[0] + '.csv', 'a')
        np.savetxt(f_handle, bottomthigmoend)
        f_handle.close()

        print bottomthigmoend
        print "bottom thigmotaxis end position shown above (lower right)"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-b", "--inputbackgroundImage", help="path to background image associated with video, which will be used to display the drawn boxes")
    args = vars(ap.parse_args())
    imgname = args["inputbackgroundImage"]
    name = str.split(imgname, ".")
    print name[0]
    print imgname
    img = cv2.imread(imgname, cv2.IMREAD_COLOR)
    #img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow('img')

while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
        #press ESC to exit
    cv2.setMouseCallback('img',draw_circle)
    time.sleep(.1)


while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
        #press ESC to exit
    cv2.setMouseCallback('img',draw_circle2)
    time.sleep(.1)


while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
        #press ESC to exit
    cv2.setMouseCallback('img',draw_circle3)
    time.sleep(.1)

while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
        #press ESC to exit
    cv2.setMouseCallback('img',draw_circle4)
    time.sleep(.1)

while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
        #press ESC to exit
    cv2.setMouseCallback('img',draw_circle5)
    time.sleep(.1)

while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
        #press ESC to exit
    cv2.setMouseCallback('img',draw_circle6)
    time.sleep(.1)

while(1):
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
        #press ESC to exit
    cv2.setMouseCallback('img',draw_circle7)
    time.sleep(.1)


cv2.destroyAllWindows()
exit()
