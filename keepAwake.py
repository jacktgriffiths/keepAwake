#imports
import pyautogui
import time

#set vars
width, height = pyautogui.size()
mousePosX, mousePosY = pyautogui.position()
newPosX = 0
newPosY = 0
pause = 1.0 #seconds
ticks = 20 #total run time will be ticks*pause

#generate new position for mouse
def getNewPos():
	global mousePosX
	global mousePosY
	global newPosX
	global newPosY
	if isMouseMovePoss():
		mousePosX, mousePosY = pyautogui.position()
		newPosX = mousePosX + 2
		newPosY = mousePosY + 2
	else:
		mousePosX, mousePosY = pyautogui.position()
		newPosX = mousePosX - 2
		newPosY = mousePosY - 2

#check that the mouse wouldnt try to move off the screen and throw an exception
def isMouseMovePoss():
	if (newPosY < width) and (newPosX < height):
		return True
	else:
		return False

#move the mouse to new position
def moveMouse():
	getNewPos()
	pyautogui.moveTo(newPosX,newPosY)
	time.sleep(pause)




i = 1
while i < ticks:
  moveMouse()
  i += 1


