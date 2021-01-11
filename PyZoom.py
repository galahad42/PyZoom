import time
import pyautogui
import subprocess
from datetime import time as t
import datetime

# Chrome zoom setting for my PC is set to 67%
# Point(x=1251, y=102)//'Maximise'
# Point(x=514, y=636)//'SFS' shortcut
# Point(x=694, y=357)//'Login' erp
# Point(x=859, y=124)//'Cross' btn
# Point(x=15, y=349)//'E-Connect'
# Point(x=931, y=244),(x=937, y=361), (x=938, y=473)//'Start'(develop better method to use span or href)
# Point(x=727, y=189)//'Open Zoom' dialog
# Point(x=898, y=603)//Video Turn off(essential)
# 15:08:24.789150

# Open Chrome in Maximise
pyautogui.hotkey('winleft')
time.sleep(4)
pyautogui.typewrite("chrome", 0.5)
pyautogui.hotkey("enter")
time.sleep(10)
pyautogui.moveTo(1251, 102) # 'Maximise' btn
pyautogui.click()
time.sleep(3)

# 'SFS' shortcut
pyautogui.moveTo(514, 636) 
pyautogui.click()
time.sleep(10)  

# 'Login' erp
pyautogui.moveTo(694, 357)
pyautogui.click()
time.sleep(10)
pyautogui.moveTo(859, 124)  # 'Cross' btn
pyautogui.click()
time.sleep(2)

# 'E-Connect'
pyautogui.moveTo(15, 349)
pyautogui.click()
time.sleep(7)


# 'Start'(Current method not satifactory, developing better method to use selenium to span or href)
pyautogui.moveTo(931, 244)
pyautogui.click()

pyautogui.moveTo(937, 361)
pyautogui.click()

pyautogui.moveTo(938, 473)
pyautogui.click()

time.sleep(10)


# Working model(bugs fixed) but still under development and most probably not the best method
# slot1 = t(7, 30, 00)
# eslot1 = t(9, 00, 00)

# slot2 = time(9, 28, 00)
# eslot2 = time(10, 28, 00)
# a = datetime.datetime.now()
# if a in (slot1, eslot1):
#     pyautogui.moveTo(934, 473, 0.8)
# else:
#     pyautogui.moveTo(931, 244, 0.8)
#    
# pyautogui.click()
# time.sleep(10)


# 'Open Zoom' dialog
pyautogui.moveTo(727, 189)
pyautogui.click()
time.sleep(10)

# Video Turn off(essential)
pyautogui.moveTo(898, 603)
pyautogui.click()
