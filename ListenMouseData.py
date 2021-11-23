from numpy import sqrt
from pynput.mouse import Listener
from pynput import mouse
import logging
import datetime
import time
from threading import Timer
import cluster 

global x
timebeginn = datetime.datetime.now()
global user


class Buffer:
    x = int()
    y = int()
    time = datetime.datetime.now()
    firstMove = False


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


def on_move(x, y):
    action = 1
    time = datetime.datetime.now() - timebeginn
    log(time, x, y, "0", "0", "0", pace(x, y, time), action)


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


def on_scroll(x, y, dx, dy):
    action = 3
    time = datetime.datetime.now() - timebeginn
    log(time, x, y, "0", dx, dy, "0", action)


def log(dtime, x, y, button, dx, dy, ppace, action):
    time_d_ms  = dtime / datetime.timedelta(milliseconds=1)
    logging.info(
        str(time_d_ms) + ";" + str(x) + ";" + str(y) + ";" + str(button) + ";" + str(dx) + ";" + str(dy) + ";" + str(ppace) + ";" + str(action))


def start():
    global x
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        Timer(10,listener.stop).start()
        listener.join()
        print("Ich habe fertig!")
    

def presetUser():
    x = input('Geben sie einen Dateinamen an (<Name>.<Programm>)!\r\n')
    fn = x + ".csv"
    logging.basicConfig(filename= fn, level=logging.INFO, format='%(message)s')
    logging.info("timeInMsSinceStart;x;y;button;dx;dy;pace;Action")
    print('Aufnahme der Mouse-interaktionen wird gestartet in 5 sekunden')
    y = 5
    while(y>0):
        time.sleep(1)
        y -= 1
        if(y==0):
            print('Okaay Leeets goo')
        else:
         print(y)
    return fn 



def presetBase():
    x = input('Geben sie einen Dateinamen an (<Name>.<Programm>)!\r\n')
    global user
    user = input('Geben sie ihren User an 1: Thomas, 2: Schwarki, 3: Taha, 4: Bodemann \r\n')
    logging.basicConfig(filename='Data/'+x + ".csv", level=logging.INFO, format='%(message)s')
    logging.info("timeInMsSinceStart;x;y;button;dx;dy;pace;Action;user")
    
    print('Aufnahme der Mouse-interaktionen wird gestartet in 5 sekunden')
    y = 5
    while(y>0):
        time.sleep(1)
        y -= 1
        if(y==0):
            print('Okaay Leeets goo')
        else:
         print(y)
    


if __name__ == "__main__":
    print('Was möchten sie tun? 1.Basisdaten erzeugen;  2. Nutzer identifizieren ;  3. Programm identifizieren\r\n')
    x = int(input())

    if x == 1:
        presetBase()
        start()
    elif x == 2:
        file = presetUser()
        start()
        user = cluster.KNNgetUser(file)
        print(user)
        exit(0)
    elif x == 3:
        print('Noch nicht implementiert')
        exit(0)
    else:
        print(' Ungültige Eingabe ')
