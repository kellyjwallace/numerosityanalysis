
import cv2
import numpy as np
import argparse
import time
import pandas as pd


ap = argparse.ArgumentParser()
ap.add_argument("-f", "--updatedframefile", help="path to updated csv file with coordinates by frame, to which the 'zone' column will be added")
ap.add_argument("-c", "--coordinatesfile", help="path to file with coordinates of all boxes drawn, while will be used to determine the zone by frame of the updated csv file")
args = vars(ap.parse_args())
framefilename = args['updatedframefile']
print framefilename
print "above is the name of the file with the frames"
coord = args['coordinatesfile']



framefile = pd.read_csv(framefilename)
framefile = pd.DataFrame(framefile, columns = ['x', 'y', 'frame', 'yflip', 'dx', 'dy', 'zone'])
#framefile = framefile.astype(int)
#print framefile
print "above is the file that has all the frames post column 'zone' append"

coord = pd.read_csv(coord, sep="/n", header = None)
coord.columns = ["coordinates"]
coord = coord.astype(int)

print coord
print "above is the file that has all the coordinates of the zones"

tankstartx = coord.loc[0, 'coordinates']
print tankstartx
print "tankstartx above"
tankstarty = coord.loc[1, 'coordinates']
print tankstarty
print "tankstarty above"

tankendx = coord.loc[2, 'coordinates']
print tankendx
print "tankendx above"
tankendy = coord.loc[3, 'coordinates']
print tankendy
print "tankendy above"

topmirrorstartx = coord.loc[4, 'coordinates']
print topmirrorstartx
print "topmirrorstartx above"
topmirrorstarty = coord.loc[5, 'coordinates']
print topmirrorstarty
print "topmirrorstarty above"

topmirrorendx = coord.loc[6, 'coordinates']
print topmirrorendx
print "topmirrorendx above"
topmirrorendy = coord.loc[7, 'coordinates']
print topmirrorendy
print "topmirrorendy above"

bottommirrorstartx = coord.loc[8, 'coordinates']
print bottommirrorstartx
print "bottommirrorstartx above"
bottommirrorstarty = coord.loc[9, 'coordinates']
print bottommirrorstarty
print "bottommirrorstarty above"

bottommirrorendx = coord.loc[10, 'coordinates']
print bottommirrorendx
print "bottommirrorendx above"
bottommirrorendy = coord.loc[11, 'coordinates']
print bottommirrorendy
print "bottommirrorendy above"

lefttargetstartx  = coord.loc[12, 'coordinates']
print lefttargetstartx
print "lefttargetstartx above"
lefttargetstarty = coord.loc[13, 'coordinates']
print lefttargetstarty
print "lefttargetstarty above"

lefttargetendx  = coord.loc[14, 'coordinates']
print lefttargetendx
print "lefttargetendx above"
lefttargetendy = coord.loc[15, 'coordinates']
print lefttargetendy
print "lefttargetendy above"

righttargetstartx  = coord.loc[16, 'coordinates']
print righttargetstartx
print "righttargetstartx above"
righttargetstarty = coord.loc[17, 'coordinates']
print righttargetstarty
print "righttargetstarty above"

righttargetendx  = coord.loc[18, 'coordinates']
print righttargetendx
print "righttargetendx above"
righttargetendy = coord.loc[19, 'coordinates']
print righttargetendy
print "righttargetendy above"

topthigmostartx = coord.loc[20, 'coordinates']
print topthigmostartx
print "topthigmostartx above"
topthigmostarty = coord.loc[21, 'coordinates']
print topthigmostarty
print "topthigmostarty above"

topthigmoendx = coord.loc[22, 'coordinates']
print topthigmoendx
print "topthigmoendx above"
topthigmoendy = coord.loc[23, 'coordinates']
print topthigmoendy
print "topthigmoendy above"

bottomthigmostartx = coord.loc[24, 'coordinates']
print bottomthigmostartx
print "bottomthigmostartx above"
bottomthigmostarty = coord.loc[25, 'coordinates']
print bottomthigmostarty
print "bottomthigmostarty above"

bottomthigmoendx = coord.loc[26, 'coordinates']
print bottomthigmoendx
print "bottomthigmoendx above"
bottomthigmoendy = coord.loc[27, 'coordinates']
print bottomthigmoendy
print "bottomthigmoendy above"


for row in framefile:
    framefile.loc[(framefile["x"] > lefttargetstartx) & (framefile["x"] < lefttargetendx) & (framefile["y"] > lefttargetstarty) & (framefile["y"] < lefttargetendy), 'zone'] = 'LeftScreen'
    framefile.loc[(framefile["x"] > righttargetstartx) & (framefile["x"] < righttargetendx) & (framefile["y"] > righttargetstarty) & (framefile["y"] < righttargetendy), 'zone'] = 'RightScreen'

    framefile.loc[(framefile["x"] > topthigmostartx) & (framefile["x"] < topthigmoendx) & (framefile["y"] > topthigmostarty) & (framefile["y"] < topthigmoendy), 'zone'] = 'TopThigmo'
    framefile.loc[(framefile["x"] > bottomthigmostartx) & (framefile["x"] < bottomthigmoendx) & (framefile["y"] > bottomthigmostarty) & (framefile["y"] < bottomthigmoendy), 'zone'] = 'BottomThigmo'

    framefile.loc[(framefile["x"] > topmirrorstartx) & (framefile["x"] < topmirrorendx) & (framefile["y"] > topmirrorstarty) & (framefile["y"] < topmirrorendy), 'zone'] = 'TopMirror'
    framefile.loc[(framefile["x"] > bottommirrorstartx) & (framefile["x"] < bottommirrorendx) & (framefile["y"] > bottommirrorstarty) & (framefile["y"] < bottommirrorendy), 'zone'] = 'BottomMirror'


print framefile
framefile.to_csv('withzones_' + framefilename + '.csv', header=['x','y','frame','yflip','dx','dy','zone'])
exit()
