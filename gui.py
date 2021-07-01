import tkinter
from tkinter import *
import logging
import ListenMouseData
import restart

global listener


def generate_data():
    global listener
    if input_field.get() != "":
        logging.basicConfig(filename=input_field.get() + ".csv", level=logging.INFO, format='%(message)s')
        listener = ListenMouseData.start()
    else:
        frame2 = Tk()
        l = Label(frame2, text="Bitte geben sie den Dateiname ein ")
        frame2.geometry("100X50")
        l.grid(row=0, column=0)

# geht noch nicht wie gedacht
def stop():
    restart.call_python(None)
    input_field.delete(0, 'end')


def getuser():
    pass


def getprogramm():
    pass


frame = Tk()
frame.geometry("450x250")
frame.title("Get User by MouseMove")
input_field = Entry(frame, bd=5, width=42)
input_field.insert('end', "user + Programm")
my_label = Label(frame, text="Bitte Dateiname eingeben ")
my_label.place(x=170, y=10)
input_field.place(x=170, y=30)
button_start = tkinter.Button(frame, text="Datenmenge erstellen", command=generate_data)
button_stop = tkinter.Button(frame, text="Erstellen stoppen", command=stop)
button_analyse_user = tkinter.Button(frame, text="Nutzer analysieren", command=getuser)
button_analyse_programm = tkinter.Button(frame, text="Programm analysieren", command=getprogramm)
button_start.place(x=10, y=30, width=150, height=30)
button_stop.place(x=10, y=80, width=150, height=30)
button_analyse_user.place(x=10, y=130, width=150, height=30)
button_analyse_programm.place(x=10, y=180, width=150, height=30)
frame.mainloop()
