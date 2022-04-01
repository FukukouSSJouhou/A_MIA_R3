
import cv2
from PIL import Image

from A_MIA_R3_Core.Face_Process import Face_Process
import ctypes
from tkinter import Image, ttk
from PIL import Image, ImageTk

import tkinter as tk
from A_MIA_R3_Core.Graph_Process import Graph_Process
from A_MIA_R3_Core.Loggingkun.Loggerkun import MIALogger
from A_MIA_R3_Core.faceproc.FPCallbackFaceSelector import FPCallbackFaceSelected, FPCallbackFaceSelector
def tintin(a,b):
    return a*b+1