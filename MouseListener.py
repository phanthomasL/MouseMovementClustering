from numpy import sqrt
from pynput.mouse import Listener
from pynput import mouse
import logging
import datetime
from threading import Timer


timebeginn = datetime.datetime.now()
global user
global prgm


# Buffer saves the time for calculating the pace
class Buffer:
    x = int()
    y = int()
    time = datetime.datetime.now()
    firstMove = False


#calculating the pace of mouse moves
def pace(x, y, time):
    buffer_x = Buffer.x
    buffer_y = Buffer.y
    buffer_time = Buffer.time
    is_firstmove = Buffer.firstMove
    if is_firstmove:
        xy =sqrt( (buffer_x *buffer_x) + (x*x)+(buffer_y *buffer_y) - (y*y))
        delta_time = time - buffer_time
        delta_time = delta_time.total_seconds()
        try:
            pace = xy / delta_time
            return pace
        except ZeroDivisionError:
            return "0"
    else:
        Buffer.time = time
        Buffer.x = x
        Buffer.y = y
        Buffer.firstMove = True
        return "0"


# logs the position and the pace
def on_move(x, y):
    action = 1
    time = datetime.datetime.now() - timebeginn
    log(time, x, y, "0", "0", "0", pace(x, y, time), action)


# logs if a button has been pressed
def on_click(x, y, button, pressed):
    action = 2
    global b
    time = datetime.datetime.now()  -timebeginn
    button.name
    if button == mouse.Button.left:
        b = 1
    if button == mouse.Button.right:
        b=9
    else: b= 0
    if pressed:
        log(time, x, y, b, "0", "0", "0", action)


#logs the position if the scroll reel has been used. 
def on_scroll(x, y, dx, dy):
    action = 3
    time = datetime.datetime.now() - timebeginn
    log(time, x, y, "0", dx, dy, "0", action)


def log(dtime, x, y, button, dx, dy, ppace, action):
    time_d_ms  = dtime / datetime.timedelta(milliseconds=1)
    logging.info(
        str(time_d_ms) + ";" + str(x) + ";" + str(y) + ";" + str(button) + ";" + str(dx) + ";" + str(dy) + ";" + str(ppace) + ";" + str(action)+";"+str(user)+";"+ str(prgm))

#starts the logging, duration is the duration in seconds
def start(p_user,p_prgm):
    global user 
    user = p_user
    global prgm
    prgm = p_prgm
    duration = 20
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        Timer(duration,listener.stop).start()
        listener.join()
        print("Ich habe fertig!")
    


