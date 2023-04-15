# This code if not for python but instead will be used in the terminal#
# I will create a auto matic code so that it will be automated#

# stty -F /dev/serial 19200
# echo -e "This is a test." > /dev/serial0

from server_client import data
import pyautogui
import time
import os


def main(data):

    os.system("stty -F /dev/serial0 19200")

    time.sleep(1)

    os.system("echo - e {} > /dev/serial0".format(data))


main()
