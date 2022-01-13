import pyautogui
import time
import PySimpleGUI as sg

sg.theme('Dark')
layout = [[sg.Text('Welcome to StayAlive')],
            [sg.Button('Run'),sg.Quit()]]


def runStayAlive():
    pyautogui.typewrite(['f15'])
    time.sleep(45)

def setupGUI():
    window = sg.Window('StayAlive', layout)
    return window

if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    w = setupGUI()
    while True:
        event, values = w.read()
        if event in (sg.WIN_CLOSED, 'Quit'):
            break
    w.close()

    