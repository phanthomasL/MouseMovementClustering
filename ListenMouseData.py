from pynput.mouse import Listener
import logging
import datetime

global x


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
        delta_x = abs(buffer_x) - abs(x)
        delta_y = abs(buffer_y) - abs(y)
        delta_time = time - buffer_time
        delta_time = delta_time.total_seconds()
        try:
            pace = (delta_x + delta_y) / delta_time
            return pace
        except ZeroDivisionError:
            return ""
    else:
        Buffer.time = time
        Buffer.x = x
        Buffer.y = y
        Buffer.firstMove = True
        return ""


def on_move(x, y):
    action = "moved"
    time = datetime.datetime.now()
    log(time, x, y, "", " ", " ", pace(x, y, time), action)


def on_click(x, y, button, pressed):
    action = "clicked"
    time = datetime.datetime.now()
    if pressed:
        log(time, x, y, button, " ", "  ", "  ", action)


def on_scroll(x, y, dx, dy):
    action = "scrolled"
    time = datetime.datetime.now()
    log(time, x, y, "", dx, dy, " ", action)


def log(dtime, x, y, button, dx, dy, ppace, action):
    logging.info(
        str(dtime) + "; " + str(x) + "; " + str(y) + ";" + str(button) + "; " + str(dx) + "; " + str(dy) + "; " + str(
            ppace) + "; " + action)


def start():
    global x
    with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()


def preset():
    x = input('Dateinamen')
    logging.basicConfig(filename=x + ".csv", level=logging.INFO, format='%(message)s')
    logging.info("Asc_time; x; y; button; dx; dy; pace; Action")
    print('Aufnahme der Mouse-interaktionen wird gestartet')


if __name__ == "__main__":
    preset()
    start()
