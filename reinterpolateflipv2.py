__author__ = 'kjw2539'
__version__= '1.0.1'
'''
///////////////////////////////////////////////////////////
//  Permission is hereby granted, free of charge,
//  to any person obtaining a copy of
//  this software and associated documentation files
//  (the "Software"), to deal in the Software without
//  restriction, including without limitation the rights
//  to use, copy, modify, merge, publish, distribute,
//  sublicense, and/or sell copies of the Software, and
//  to permit persons to whom the Software is furnished
//  to do so, subject to the following conditions:
//
//  The above copyright notice and this permission notice
//  shall be included in all copies or substantial portions
//  of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
//  ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
//  TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
//  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
//  THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
//  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
//  OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
//  IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
//  DEALINGS IN THE SOFTWARE.
'''

import cv2
import os
import numpy as np
import pandas as pd
import argparse


def update(data):
    data.interpolate(method='linear', inplace=True)
    data['yflip'] = 720 - data['y']
    data['dx'] = data['x'].diff(1)
    data['dy'] = data['y'].diff(1)
    return data

def remove(data):
    for i in data['dx']:
    #while in dataframe (recurseive by row)
        data.loc[(abs(data['dx']) > 200)] = np.nan
        data['dx'] = data['x'].diff(1)
        data['dy'] = data['y'].diff(1)
        data['sumdx']= data['dx'].cumsum()
        data['sumdy']= data['dy'].cumsum()
        #if it finds a place where dx>100:
            #data['dx'1::2] = 'endofjump'
            #framebegin= frame of the first jump (where dx>100)
            #frameend = frame of second jump (where dx>100) and where frame > framebegin
            #change everything except frame (x, y, xflip, dx, dy) in between those two jumps (frambegin ...frameend) to np.nan
    print data
    print "data should now have removed jumps and replaced with NaN, not yet interpolated"
    data.interpolate(method='linear', inplace=True)
    print data
    print "now interpolated"
    return data


def refine(data):
    data.loc[str(len(data))] = pd.Series({'x', 'y', 'frame', 'yflip', 'dx', 'dy'})
    return data


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--trackingData", help="tracking data .csv file, no path?")
    args = vars(ap.parse_args())
    track = args["trackingData"]
    print track
    print 'imported tracking data'
    data = pd.read_csv(args["trackingData"])
    print data
    print "original data shown above"
    #data.interpolate(method='linear', inplace=True)
    refineddata = update(data)
    print refineddata
    print "this is the data before the remove function"
    completedata = remove(refineddata)
    #completedata = pd.DataFrame(columns={'x', 'y', 'frame', 'yflip', 'dx', 'dy'})
    #print completedata
    #print "completed data as a dataframe shown above"
    completedata.to_csv('updated_'+track+'', index=False, columns=['x', 'y', 'frame', 'yflip', 'dx', 'dy'])
exit()
