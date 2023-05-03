### Entire code including the implementation of clientside.py####

from tkinter import *
import socket

import RPi.GPIO as GPIO
import time
import subprocess

BUTTON_PIN = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


WIDTH = 1800
HEIGHT = 1600
WHITE = [255, 255, 255]


class Screen:
    def __init__(self, name):
        self.name = name
        self.background = WHITE
        self.buttons = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value

    @property
    def buttons(self):
        return self._buttons

    @buttons.setter
    def buttons(self, value):
        self._buttons = value


class Program(Frame):
    def __init__(self):
        self.__orderedItems = []
        self.__itemCount = 0
        self.__itemStrings = []
        self.__itemPrices = []

    @property
    def orderedItems(self):
        return self.__orderedItems

    @orderedItems.setter
    def orderedItems(self, value):
        self.__orderedItems.append(value)

    @property
    def itemCount(self):
        return self.__itemCount

    @itemCount.setter
    def itemCount(self, value):
        self.__itemCount = value

    @property
    def itemStrings(self):
        return self.__itemStrings

    @itemStrings.setter
    def itemStrings(self, value):
        self.__itemStrings = value

    @property
    def itemPrices(self):
        return self.__itemPrices

    @itemPrices.setter
    def itemPrices(self, value):
        self.__itemPrices = value

    def createText(self):
        self.T = Text(win, height=60, width=40)
        self.T.pack(side=RIGHT)
        self.T.config(state="disabled")

    def begin(self):
        pass

    def changeScreen(self, value):
        win.title(value.name)

    def createItems(self):
        self.items = {"burger": 3.50, "pizza": 4.50, "steak": 15, "spagetti": 12.50,
                      "fruit bowl": 4.00, "water": 1.00, "soda": 2.00, "tea": 1.50, "lemonade": 2.00}

    def addItem(self, item):
        self.__itemCount += 1
        self.__itemStrings.append(item)

        self.__itemPrices.append(self.items[item])
        self.writeItem(item)

    def writeItem(self, item):
        self.T.config(state="normal")
        receiptLine = f"{item} -- {self.items[item]}"
        self.T.insert(END, receiptLine + "\n")
        self.T.config(state="disabled")

    def clearOrder(self):
        self.T.config(state="normal")
        self.T.delete("1.0", END)

    def formatOrder(self):
        totalOrder = ""
        totalPrice = 0
        receiptTop = f"You ordered {self.__itemCount} items total. \n"
        itemSequence = ""
        for i in range(self.__itemCount):
            itemSequence += f"{self.__itemStrings[i]} --- {self.__itemPrices[i]} \n"
        for i in range(len(self.__itemPrices)):
            totalPrice += self.__itemPrices[i]
        priceAlert = f"total price: ${totalPrice}"
        totalReceipt = receiptTop + itemSequence + priceAlert
        print(totalReceipt)
        client_program(totalReceipt)

        self.__itemCount = 0
        self.__itemStrings = []
        self.__itemPrices = []
        self.clearOrder()
        # tests

    def openHomeScreen(self):
        s1.b1 = Button(win, text="Open Menu", height=80, width=40, bg="GREY", command=lambda: [
                       self.closeHomeScreen(), self.openMenuScreen()])
        s1.b1.pack()

    def createCoreButtons(self):
        s1.b10 = Button(win, text="Finish Order", height=5, width=15,
                        bg="GREEN", command=lambda: [self.formatOrder()])
        s1.b10.place(x=1100, y=0)
        s1.b2 = Button(win, text="Quit", height=5, width=15,
                       bg="RED", command=win.destroy)
        s1.b2.place(x=0, y=0)

    def closeHomeScreen(self):
        s1.b1.destroy()

    def openMenuScreen(self):
        s1.b3 = Button(win, text="Back", height=5, width=15, bg="ORANGE", command=lambda: [
                       self.closeMenuScreen(), self.openHomeScreen()])
        s1.b4 = Button(win, text="DRINKS", height=30, width=30, bg="BLUE", command=lambda: [
                       self.closeMenuScreen(), self.openDrinkScreen()])
        s1.b5 = Button(win, text="FOOD", height=30, width=30, bg="BROWN", command=lambda: [
                       self.closeMenuScreen(), self.openFoodScreen()])

        s1.b3.place(x=0, y=85)
        s1.b4.place(x=700, y=200)
        s1.b5.place(x=300, y=200)

    def closeMenuScreen(self):
        s1.b3.destroy()
        s1.b4.destroy()
        s1.b5.destroy()

    def openFoodScreen(self):
        s1.b3 = Button(win, text="Back", height=5, width=15, bg="ORANGE", command=lambda: [
                       self.closeFoodScreen(), self.openMenuScreen()])
        s1.b4 = Button(win, text="Burger", height=10, width=20,
                       bg="GREEN", command=lambda: self.addItem("burger"))
        s1.b5 = Button(win, text="Pizza", height=10, width=20,
                       bg="YELLOW", command=lambda: self.addItem("pizza"))
        s1.b6 = Button(win, text="Steak", height=10, width=20,
                       bg="BROWN", command=lambda: self.addItem("steak"))
        s1.b7 = Button(win, text="Spagetti", height=10, width=20,
                       bg="ORANGE", command=lambda: self.addItem("spagetti"))
        s1.b8 = Button(win, text="Fruit bowl", height=10, width=20,
                       bg="RED", command=lambda: self.addItem("fruit bowl"))

        s1.b3.place(x=0, y=85)
        s1.b4.place(x=225, y=200)
        s1.b5.place(x=575, y=200)
        s1.b6.place(x=925, y=200)
        s1.b7.place(x=400, y=450)
        s1.b8.place(x=750, y=450)

    def closeFoodScreen(self):
        s1.b3.destroy()
        s1.b4.destroy()
        s1.b5.destroy()
        s1.b6.destroy()
        s1.b7.destroy()
        s1.b8.destroy()

    def openDrinkScreen(self):
        s1.b3 = Button(win, text="Back", height=5, width=15, bg="ORANGE", command=lambda: [
                       self.closeDrinkScreen(), self.openMenuScreen()])
        s1.b4 = Button(win, text="Water", height=10, width=20,
                       bg="BLUE", command=lambda: self.addItem("water"))
        s1.b5 = Button(win, text="Soda", height=10, width=20,
                       bg="BROWN", command=lambda: self.addItem("soda"))
        s1.b6 = Button(win, text="Tea", height=10, width=20,
                       bg="GREEN", command=lambda: self.addItem("tea"))
        s1.b7 = Button(win, text="Lemonade", height=10, width=20,
                       bg="YELLOW", command=lambda: self.addItem("lemonade"))

        s1.b3.place(x=0, y=85)
        s1.b4.place(x=400, y=200)
        s1.b5.place(x=750, y=200)
        s1.b6.place(x=400, y=450)
        s1.b7.place(x=750, y=450)

    def closeDrinkScreen(self):
        s1.b3.destroy()
        s1.b4.destroy()
        s1.b5.destroy()
        s1.b6.destroy()
        s1.b7.destroy()


def makeScreens():
    # creation of screens

    # the home screen, this will be returned to after each order
    # and will give the option to continue to the menu or to quit the program
    # button 1: quit
    # button 2: menu
    # this also has the thing to the side
    global s1
    s1 = Screen("screen1")

    # a split between food items and drinks, from here on out there is an additonal section
    # to the right listing off ordered itemsa and their costs
    # the order has a limit on the amount of thing, this may be circumvented by having things order in multiples
    # x2, x3, etc
    # button 1: back button, will take to the homescreen and wipe the order (strech, are you sure feature)
    # button 2: food half
    # button 3: drink half
    # button 4: finish order
    global s2
    s2 = Screen("screen2")
    # food menu
    # back menu, takes to previous page
    # finish order button
    # several value buttons, assigns to order
    global s3
    s3 = Screen("screen3")

    # same as food but for drinks
    # s4

    # creations of buttons, sorted by scenes
    # s1.b1 = Button(1, 2, 3)
    # s2.b1 = Button(2,2,3)


def client_program(totalReceipt):
    host = "169.254.37.31"  # Replace with host IP
    port = 5000  # socket server port number

    client_socket = socket.socket()
    client_socket.connect((host, port))

    # NEEEDS TO BE CHANGED TO WHATEVER THE VARIABLE HAYDEN'S CODE MAKES####
    message = (totalReceipt)

    client_socket.send(message.encode())

    client_socket.close()


def Printtest(channel):
    subprocess.run(["lp", "-o", "cpi=18", "/home/pi/Desktop/Welcome.txt"])


GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING,
                      callback=Printtest, bouncetime=2000)

win = Tk()
win.title("default")
win.geometry("1800x1200")
p = Program()
p.createText()
p.createItems()


makeScreens()


p.openHomeScreen()
p.createCoreButtons()


p = Program()
p.begin()


p.changeScreen(s1)
win.mainloop()
