'''
main file. run this file as administrator with "python final2.py". The program will then wait for a device to be connected. Currently, ending the program requires keyboard Ctrl+C command. 
'''


import wmi
import usb.core
import logger2
import subprocess
from pynput.keyboard import Key, Listener
from pynput import keyboard as kb
from time import time

def ask_user(): #query user method
    check = str(raw_input("Question ? (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return ask_user()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user()



#wait and watch for new USB insertion
raw_wql = "SELECT * FROM __InstanceCreationEvent WITHIN 2 WHERE TargetInstance ISA \'Win32_USBHub\'"
c = wmi.WMI ()
watcher = c.watch_for(raw_wql=raw_wql)

potential_trusted_devices = []

def save_trust():   #saves the potentially trusted devices to the safe file. 
    
    for device in potential_trusted_devices:
        while ( res:=input("Do you want to add " + device + " to safe devices? (Enter y/n)").lower() ) not in {"y", "n"}: pass
        if res == 'y':
            firstfile.write(device +'\n')
            print('device saved')
        else:
            print('device not saved')
        
    firstfile.close()
    potential_trusted_devices.pop(0)
    
    
    
while 1:


    u = watcher ()  #new USB device
    if (u != None):
    
        print("start: ", time())
        
        #new Device added
        firstfile = open('safe.txt','r+')#open text files to store safe usb devices
        safeList = firstfile.read().splitlines()
        trusted = False
        ID = u.DeviceID #ID of the device
        print('Device ID=' + str(ID))
        for line in safeList: #check to see if ID is in list of safe devices
            if line == ID:
                trusted = True
                break
                
        print("after check: ", time())

        if trusted == False:
            #if not trusted, check for logging attack
            if logger2.main() == True: #run the logger program
                print('attack happened: ', time())
                subprocess.run(['pnputil', '/remove-device', ID]) #to disable
                print('device disabled: ', time())
            else:
                print('no attack: ', time())
                potential_trusted_devices.append(ID)

        else:
            print('saved trusted device: ', time())

    ch = input("Press 1 to continue scanning, 2 to stop and add potential devices: ")
    if ch == "2":
        save_trust()


