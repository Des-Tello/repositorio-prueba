'''
import pywhatkit

try:
    #envio de mensaje
    pywhatkit.sendwhatmsg("+56920450536","Hola amigito",2,15)
    print("enviado exitosamente")

except:
    print("algo salio mal")
'''

import pyautogui as pg, webbrowser as web, time as tm

web.open("https://web.whatsapp.com/send?phone=+56920450536")
i=0
tm.sleep(8)
while (True):
    pg.write("Hola amigito")
    i = i+1
    if(i>5000):break;
    pg.press('enter')asdasdasda

