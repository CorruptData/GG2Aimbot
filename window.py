import win32gui
import win32ui 
import win32con
import numpy
import struct
import cv2

class Window:
	# Loads in the active window and prepares it for screenshotting
	def __init__(self):
		self.handle = win32gui.GetForegroundWindow()

		self.screen_w = self.get_rect()[2]
		self.screen_h = self.get_rect()[3]

		wDC = win32gui.GetWindowDC(self.handle)
		self.dcObj = win32ui.CreateDCFromHandle(wDC)
		self.cDC = self.dcObj.CreateCompatibleDC()
		self.dataBitMap = win32ui.CreateBitmap()
		self.dataBitMap.CreateCompatibleBitmap(self.dcObj,self.screen_w,self.screen_h)
		self.cDC.SelectObject(self.dataBitMap)

	def screenshot(self):
		self.cDC.BitBlt((0,0), (self.screen_w,self.screen_h), self.dcObj, (0,0), win32con.SRCCOPY)
		self.dataBitMap.SaveBitmapFile(self.cDC, 'temp.png')
		return cv2.imread('temp.png',1)

	# X Y W H
	def get_rect(self):
	 	rect =  win32gui.GetWindowRect(self.handle)
	 	return [rect[0],rect[1], rect[2] - rect[0], rect[3] - rect[1]]

	def finish(self):
		# Free Resources
		dcObj.DeleteDC()
		cDC.DeleteDC()
		win32gui.ReleaseDC(hwnd, wDC)
		win32gui.DeleteObject(dataBitMap.GetHandle())

	@staticmethod
	def get_current_active_window_name():
		return win32gui.GetWindowText(win32gui.GetForegroundWindow())


