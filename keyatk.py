# tool to mimic a keyboard attack

'''
Code to test the keylogger capabilities. 
This code runs via python on windows 10. It opens a cmd terminal and navigates to the D drive, where it then tries to run a "malicious code" file. 
'''


from pynput.keyboard import Key, Controller
import pyautogui as kb
import time

kb = Controller()
def typ(k):
    kb.press(k)
    kb.release(k)

def write(words):
    for x in words:
        typ(x)

kb.press(Key.cmd_l)
kb.press("r")
kb.release(Key.cmd_l)
kb.release("r")
time.sleep(1)
write("cmd")
kb.press(Key.enter)
kb.release(Key.enter)
time.sleep(1)
write("this is simulated attack code. assume that text being typed here is malicious")
kb.press(Key.enter)
kb.release(Key.enter)
write("d:")
kb.press(Key.enter)
kb.release(Key.enter)
write("python malicious_code.py")
kb.press(Key.enter)
kb.release(Key.enter)


