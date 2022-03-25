from gui import *

import os 
import threading
def say():
    os.system('say -v Fred "Welcome, to room 4 all"')
threading.Thread(target=say).start()
values = gui()
values.room4all()
