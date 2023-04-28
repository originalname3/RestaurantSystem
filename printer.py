# This code is for a button press to print a receipt when after the user orders.
# I will create a automatic code so that it will be automated#

# stty -F /dev/serial 19200
# echo -e "This is a test." > /dev/serial0

# IMPORTS
import RPi.GPIO as GPIO
import time
import os

BUTTON_PIN = 16

# Sets up GPIO, connects printer
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
os.system("stty -F /dev/serial0 19200")


def Printtest(channel):
    print('Printing...')

# Test printing text & image
# os.system("echo 'This is a test.' | lp")
# os.system("lp -o fit-to-page /usr/share/raspberrypi-artwork/raspberry-pi-logo.png")

# Test printing text from file, 18 chars per inch (to fit IPFS ascii art)
# os.system("lp -o cpi=18 /home/pi/Scripts/welcome.txt")

# Test printing from IPFS! See ipfs.io
    os.system("'Hello' | lp")


GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING,
                      callback=Printtest, bouncetime=2000)
while 1:
    time.sleep(1)
