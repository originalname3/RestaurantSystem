from tkinter import *

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
        self.T = Text(win, height = 60, width = 40)
        self.T.pack(side = RIGHT)
        self.T.config(state = "disabled")
    

    
    def begin(self):
        pass
    def changeScreen(self, value):
        win.title(value.name)
    def createItems(self):
        self.items = {"burger": 3.50, "pizza": 4.50, "steak": 15, "spagetti": 12.50,\
        "fruit bowl": 4.00, "water": 1.00, "soda": 2.00, "tea": 1.50, "lemonade": 2.00}
        
    def addItem(self, item):
        self.__itemCount += 1
        self.__itemStrings.append(item)

        self.__itemPrices.append(self.items[item])
        self.writeItem(item)
        
    def writeItem(self, item):
        self.T.config(state = "normal")
        receiptLine = f"{item} -- {self.items[item]}"
        self.T.insert(END, receiptLine + "\n")
        self.T.config(state = "disabled")
        
    def clearOrder(self):
        self.T.config(state = "normal")
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
        
        
        self.__itemCount = 0
        self.__itemStrings = []
        self.__itemPrices = []
        self.clearOrder()
        #tests
    
    def openHomeScreen(self):
        s1.b1 = Button(win, text = "Open menu", height = 5, width = 10, command = lambda: [self.closeHomeScreen(), self.openMenuScreen()])
        s1.b1.pack()
        s1.b2 = Button(win, text = "Quit", height = 5, width = 10, command = win.destroy)
        s1.b2.pack()
    def createFinishButton(self):
        s1.b10 = Button(win, text = "finish order", height = 5, width = 10, command = lambda: [self.formatOrder()])
        s1.b10.pack()
        
    def closeHomeScreen(self):
        s1.b1.destroy()
        s1.b2.destroy()
        
    def openMenuScreen(self):
        s1.b1 = Button(win, text = "back", height = 5, width = 10, command = lambda: [self.closeMenuScreen(), self.openHomeScreen()])
        s1.b2 = Button(win, text = "drinks", height = 5, width = 10, command = lambda: [self.closeMenuScreen(), self.openDrinkScreen()])
        s1.b3 = Button(win, text = "food", height = 5, width = 10, command = lambda: [self.closeMenuScreen(), self.openFoodScreen()])
        
        s1.b1.pack()
        s1.b2.pack()
        s1.b3.pack()
        
        
    def closeMenuScreen(self):
        s1.b1.destroy()
        s1.b2.destroy()
        s1.b3.destroy()
        
    def openFoodScreen(self):
        s1.b1 = Button(win, text = "back", height = 5, width = 10, command = lambda: [self.closeFoodScreen(), self.openMenuScreen()])
        s1.b2 = Button(win, text = "Burger", height = 5, width = 10, command = lambda: self.addItem("burger"))
        s1.b3 = Button(win, text = "Pizza", height = 5, width = 10, command = lambda: self.addItem("pizza"))
        s1.b4 = Button(win, text = "Steak", height = 5, width = 10, command = lambda: self.addItem("steak"))
        s1.b5 = Button(win, text = "Spagetti", height = 5, width = 10, command = lambda: self.addItem("spagetti"))
        s1.b6 = Button(win, text = "Fruit bowl", height = 5, width = 10, command = lambda: self.addItem("fruit bowl"))
        
        s1.b1.pack()
        s1.b2.pack()
        s1.b3.pack()
        s1.b4.pack()
        s1.b5.pack()
        s1.b6.pack()
        
    def closeFoodScreen(self):
        s1.b1.destroy()
        s1.b2.destroy()
        s1.b3.destroy()
        s1.b4.destroy()
        s1.b5.destroy()
        s1.b6.destroy()
        
    def openDrinkScreen(self):
        s1.b1 = Button(win, text = "back", height = 5, width = 10, command = lambda: [self.closeDrinkScreen(), self.openMenuScreen()])
        s1.b2 = Button(win, text = "water", height = 5, width = 10, command = lambda: self.addItem("water"))
        s1.b3 = Button(win, text = "soda", height = 5, width = 10, command = lambda: self.addItem("soda"))
        s1.b4 = Button(win, text = "tea", height = 5, width = 10, command = lambda: self.addItem("tea"))
        s1.b5 = Button(win, text = "lemonade", height = 5, width = 10, command = lambda: self.addItem("lemonade"))
        
        s1.b1.pack()
        s1.b2.pack()
        s1.b3.pack()
        s1.b4.pack()
        s1.b5.pack()
        
    def closeDrinkScreen(self):
        s1.b1.destroy()
        s1.b2.destroy()
        s1.b3.destroy()
        s1.b4.destroy()
        s1.b5.destroy()
        
        
 
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
    #button 2: food half
    #button 3: drink half 
    # button 4: finish order    
    global s2 
    s2 = Screen("screen2")
    # food menu
    #back menu, takes to previous page
    # finish order button
    # several value buttons, assigns to order
    global s3 
    s3 = Screen("screen3")
    
    #same as food but for drinks
    #s4
    
        
    # creations of buttons, sorted by scenes
    #s1.b1 = Button(1, 2, 3) 
    #s2.b1 = Button(2,2,3)
    



win = Tk()
win.title("default")
win.geometry("1800x1200")
p = Program()   
p.createText()
p.createItems()


makeScreens()



p.openHomeScreen()
p.createFinishButton()


p = Program() 
p.begin()


p.changeScreen(s1)
win.mainloop()
