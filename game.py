import serial
import pyautogui
#pip install pyserial
#pip install pyautogui
port=serial.Serial("COM7",9600)
while True:
    line = port.readline() #read data line by line
    if line:
        string = line.decode()  # convert the byte string to a unicode string                                                                                                                                                                                                        
        num = int(string) # convert the unicode string to an int                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        if num==1:
            pyautogui.press('space') #it will press space key!
                      
                        