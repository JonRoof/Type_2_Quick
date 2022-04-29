# Type_2_Quick
A prototype tool to defend Windows 10 computers against keyboard injection attacks from untrustworthy USB sources

**Dependencies:**

**pyusb**
install with "pip install pyusb"

**pynput**
install with "pip install pynput"

**wmi**
install with "pip install wmi"



Use this program by running
"python final2.py"
with admin privilages. (without privilages the program cant eject attacking devices)

The software detects newly connected USB devices and checks to make sure they are not running any key injections by detecting keystrokes for a customizable time period after the device is connected. If an attack is detected, it will be reported, and the device will be disconnected. 
If there is no attack detected, the Device ID will be added to a list. The user will be prompted to add this list to the "safe" list in safe.txt. If a device ID is on this list, it will bypass the scanning process to cut down on wait time. 
After adding to the list or not, the tool will continue scanning for new connections. 


The tool is not designed to handle new USB connections while it is scanning. There is plenty of future work to be done here. 
