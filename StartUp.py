import MouseListener
import logging
import time
import UserIdentifier
import ProgramIdentifier

global prgm 
global user


#sets some variables from input which are need to get user or programm
def presetUserorProgram():
    x = input('Geben sie einen Dateinamen an (<Name>.<Programm>)!\r\n')
    fn = x + ".csv"
    global user
    user = input('Geben sie ihre Usernummer an! (1: Thomas, 2: Schwarki, 3: Taha, 4: Bodemann)\r\n')
    global prgm
    prgm = input('Geben sie die Programmnummer an (1: Excel, 2: Visual Studio code, 3: WebEx) \r\n')

    logging.basicConfig(filename= fn, level=logging.INFO, format='%(message)s')
    logging.info("timeInMsSinceStart;x;y;button;dx;dy;pace;Action;user;programm")
    
    print('\r\nAufnahme der Mouse-interaktionen wird gestartet in 5 sekunden')
    y = 5
    while(y>0):
        time.sleep(1)
        y -= 1
        if(y==0):
            print('Okaay Leeets goo')
        else:
         print(y)
    return fn 


#sets some variables from input which are need to create base data
def presetBase():
    x = input('Geben sie einen Dateinamen an! (<Name>.<Programm>)\r\n')
    global user
    user = input('Geben sie ihre Usernummer an! (1: Thomas, 2: Schwarki, 3: Taha, 4: Bodemann)\r\n')
    global prgm
    prgm = input('Geben sie die Programmnummer an! (1: Excel, 2: Visual studio code, 3: Chrome) \r\n')

    logging.basicConfig(filename='Data/'+x + ".csv", level=logging.INFO, format='%(message)s')
    logging.info("timeInMsSinceStart;x;y;button;dx;dy;pace;Action;user;programm")
    
    print('Aufnahme der Mouse-Interaktionen wird gestartet in 5 sekunden')
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
        MouseListener.start(user, prgm)
    elif x == 2:
        file = presetUserorProgram()
        MouseListener.start(user, prgm)
        identifizierteruser = UserIdentifier.KNNgetUser(file)
        print(identifizierteruser)
        exit(0)
    elif x == 3:
        file = presetUserorProgram()
        MouseListener.start(user, prgm)
        identifiziertesprgm = ProgramIdentifier.KNNgetProgram(file)
        print(identifiziertesprgm)
        exit(0)
    else:
        print(' Ungültige Eingabe ')