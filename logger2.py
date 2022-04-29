'''
keylogger to track number of keypresses. can be run independently from final2.py.
'''

import pynput
from threading import Timer
from time import time
from pynput.keyboard import Key, Listener
from pynput import keyboard as kb
import copy

word_counts = 0 #number of keys pressed
keys = []
exit_script = False
wait_to_start = True
word_counts2 = 0 #tracking for how many keys pressed

def on_press(key): #method to handle press events
    wait_to_start = False
    global word_counts, keys
    keys.append(key)
    word_counts += 1
    #lines below can be uncommented if you want to see which keys were pressed and how many
    #print(f'{key} pressed')
    #print(word_counts)
    return True

            
def on_release(key):#method to handle key release events
    global exit_script
    if key == Key.esc:
        exit_script = True
        return False


def start_listening(): #method to listen to how many keypresses were made
    word_counts2 = copy.copy(word_counts) #reset word_counts2
    current_time = time()
    listner = Listener(on_press=on_press, on_release=on_release)
    listner.start()
    
    runTime = 5 #how long the logger runs for. Change this value to check over longer or shorter periods
    
    print("timer started: ",time())
    mykb = kb.Controller()
    attack = False
    while time() < current_time + runTime:
        if word_counts-word_counts2 > 25:
            print("Keyboard attack!", time())
            attack = True
            print("attack status: ",attack)

            word_counts2 += word_counts
            mykb.press(kb.Key.esc)
            mykb.release(kb.Key.esc)
            return attack
        else:
            pass
            

    word_counts2 += word_counts
    mykb.press(kb.Key.esc)
    mykb.release(kb.Key.esc)
    return attack

def main():

    with kb.Events() as events: #wait for a keyboard event
                
        event = events.get(10.0) #wait ten seconds for a key press. Change this value for longer wait time
        
        attack_happening = False
        if event is None: #no keypress
            print('You did not press a key within ten seconds')
        else:
            attack_happening = start_listening() #assign attack variable to the listen, if attack happens, it will be recorded here
        return attack_happening          
        
    
    