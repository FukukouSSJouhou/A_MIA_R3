from subprocess import call
import sys
import cv2

class pyclasstest(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def run(self,callback):
        print("cb:",callback)
        print(sys.path)
        return callback(self.a,self.b,3)
    def __repr__(self):
        return 'pyclasstest(a=%r, b=%r)' % (self.a, self.b)