import pandas
import pyautogui as pg
import time

df = pandas.read_csv('liste.csv')
say = int(len(df))
no = df['NO']
sms = df['SMS']
bas = 0

for bas in range(say):
    numara=(no[bas])
    mesaj=(sms[bas])
    time.sleep(0.1)
    pg.click(240,69)
    time.sleep(0.1)
    pg.write('wa.me/90'+ str(numara))
    time.sleep(0.1)
    pg.press('enter')
    time.sleep(2)
    pg.click(484,301)
    time.sleep(2)
    pg.click(466,375)
    time.sleep(6)
    pg.click(492,697)
    time.sleep(0.1)
    pg.write(mesaj)
    time.sleep(0.1)
    pg.press('enter')
    time.sleep(1)
    print("-->", numara,"-->",mesaj," (ok)")