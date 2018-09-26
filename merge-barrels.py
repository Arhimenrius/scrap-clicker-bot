from __future__ import print_function
import pyxhook
from pymouse import PyMouse
from time import sleep
import random

m = PyMouse()

tl_x = 3290
tl_y = 260
br_x = 3630
br_y =830

game_width = br_x-tl_x
game_height = br_y-tl_y

distance_x = game_width/3
distance_y = game_height/4

def randomDistance():
	return random.randint(-25,25)

def mergeToRow(mergeFromRow):
	if(running == False):
		return;
	mergeToRow = mergeFromRow-1
	for element in range(4):
		m.press(tl_x+(distance_x*element)+randomDistance(), tl_y+(distance_y*mergeFromRow)+randomDistance())
		sleep(0.05)
		m.release(tl_x+(distance_x*element)+randomDistance(), tl_y+(distance_y*mergeToRow)+randomDistance())
		sleep(0.05)
		m.click(tl_x-random.randint(60,80), random.randint(tl_y, br_y))
	sleep(0.2) 

def mergeFirstRowAndRemove():
	# MERGE_TO_FINALIZE
	m.press(tl_x+(distance_x), tl_y)
	sleep(0.05)
	m.release(tl_x, tl_y)
	sleep(random.uniform(0.05,0.1))

	m.press(tl_x+(distance_x*3), tl_y)
	sleep(0.05)
	m.release(tl_x+(distance_x*2), tl_y)
	sleep(random.uniform(0.05,0.1))

	m.press(tl_x+(distance_x*2), tl_y)
	sleep(0.05)
	m.release(tl_x, tl_y)
	sleep(random.uniform(0.05,0.1))

	m.click(tl_x,tl_y);
	m.click(tl_x,tl_y);
	sleep(0.2)
	m.click(tl_x+(distance_x*2), tl_y+(distance_y*3))

	sleep(random.uniform(0.2,0.3))

# This function is called every time a key is presssed
def kbevent(event):
    global running
    # print key info
    print(event)

    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 32:
        running = False


# Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True
while running:
    # STEP 1
	mergeToRow(1);
	mergeToRow(2);
	mergeToRow(1);
	if(running == False):
		break;
	# STEP 2
	mergeToRow(2);
	mergeToRow(3);
	mergeToRow(2);
	mergeToRow(1);


	if(running == False):
		break;
	# STEP 2
	mergeToRow(2);
	mergeToRow(3);
	mergeToRow(2);
	mergeToRow(3);
	mergeToRow(4);
	mergeToRow(3);
	mergeToRow(2);
	mergeToRow(1);

	if(running == False):
		break;

	mergeFirstRowAndRemove()

# Close the listener when we are done
hookman.cancel()
