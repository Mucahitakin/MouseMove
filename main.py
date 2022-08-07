import pyautogui
import random
import time
def countdown(t):
    print('𝔼𝕞𝕚𝕣 𝕌𝕪𝕘𝕦𝕝𝕒𝕟𝕚𝕪𝕠𝕣....')
    time.sleep(1)
    print('   ¯\_(ツ)_/¯')
    time.sleep(1)
    print('𝔹𝕒𝕤𝕝𝕒𝕥𝕚𝕝𝕚𝕪𝕠𝕣....')
    time.sleep(1)
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
        if t==0:
            Mouse()
            t=10
            continue
def Mouse():
    #print(pyautogui.position())
    #print(pyautogui.size())

    x=random.randint(290,1255)
    y=random.randint(91,568)
    print(y,"Y")
    print(x,"X")
    pyautogui.moveTo(x, 407, duration=1)

if __name__ == '__main__':
    countdown(10)
    #print(pyautogui.position())
    #print(pyautogui.size())

