from time import sleep
from tkinter import *
VERBS = ["go","look","take"]
QUIT_COMMANDS = ["exit","quit","bye"]

######################################################
# the blueprint for a room
class Room:
    # the constructor
    def __init__(self, name, image):
    # rooms have a name, exits (e.g., south), exit
    # locations (e.g., to the south is room n), items
    # (e.g., table), item descriptions (for each item),
    # and grabbables (things that can be taken into
    # inventory)
        self._name = name
        self._image = image
        self._exits = []
        self._exitLocations = []
        self._items = []
        self._itemDescriptions = []
        self._grabbables = []
    # getters and setters for the instance variables
    @property
    def image(self):
        return self._image
    @image.setter
    def image(self, value):
        self._image = value
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value
    @property
    def exitLocations(self):
        return self._exitLocations
    @exitLocations.setter
    def exitLocations(self, value):
        self._exitLocations = value
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value
    @property
    def itemDescriptions(self):
        return self._itemDescriptions
    @itemDescriptions.setter
    def itemDescriptions(self, value):
        self._itemDescriptions = value
    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits.append(exit)
        self._exitLocations.append(room)
    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and exit to the appropriate lists
        self._items.append(item)
        self._itemDescriptions.append(desc)
    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)
        # removes a grabbable item from the room
        # the item is a string (e.g., key)
    def delGrabbable(self, item):
    # remove the item from the list
        self._grabbables.remove(item)
    # returns a string description of the room
    def __str__(self):
    # first, the room name
        s = "You are in {}.\n".format(self.name)
        # next, the items in the room
        s += "You see: "
        for item in self.items:
            s += item + " "
        s += "\n"
        # next, the exits from the room
        s += "Paths: "
        for exit in self.exits:
            s += exit + " "
        return s
    
class Game(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        
    def createRooms(self):
        Game.rooms = []
        r1 = Room("Hobbiton", "hobbiton.gif")
        r2 = Room("Rivendell", "rivendell.gif")
        r3 = Room("Isengard", "isengard.gif")
        r4 = Room("Minas Tirith", "minas.gif")
        r5 = Room("Mordor", "mordor.gif")
        r6 = Room("Mount Doom", "mountdoom.gif")
        
    # add exits to room 1
        r1.addExit("north",r2)
    # add grabbables to room 1
        r1.addGrabbable("sting")
        r1.addGrabbable("map")
        r1.addGrabbable("diary")
    # add items to room 1
        r1.addItem("gandalf", "Gandalf says: 'Go north to Rivendell to find the ring. \nBut first you will need a couple items for your \njourney!' ") 
        r1.addItem("desk", "A drawn out map of Middle Earth lays flat on the desk as well as a diary.")
        r1.addItem("chest", "You open the chest and the first thing you see is a \nsword with name of sting written on the blade.")
        Game.rooms.append(r1)
        
    # add exits to room 2
        r2.addExit("south", r1)
        r2.addExit("east",None)
        r2.addExit("west", r3)
    # add grabbables to room 2
        r2.addGrabbable("ring")
    # add items to room 2
        r2.addItem("elrond", "Elrond says: 'Take the ring to Mordor where it was \ncreated and destroy it inthe lava of Mount Doom!' ")
        r2.addItem("pillar", "A ring lays upon this small pillar")
        r2.addItem("aragorn", "Aragorn says: 'Be careful of certain riddles that might stumble upon you when taking the ring to Mordor.' ")
        r2.addItem("legolas", "Legolas says: 'You will need to head towards Isengard \nwhere you will have to face Saruman the White.' ")
        r2.addItem("gimli", "Gimli says: 'I wouldn't go east unless you want to be \nskinned alive by Orcs!' ")
        Game.rooms.append(r2)
    
    # add exits to room 3
        r3.addExit("east", r4)
    # add items to room 3
        r3.addItem("saruman", "Saruman says: 'In order to get to Mordor will have to \nanswer this riddle.' ")
        
        # This is where I want to create a riddle in order to get to the next path.
        
        Game.rooms.append(r3)
        
    # add exits to room 4
        r4.addExit("north", r5)
        r4.addExit("west", None)
        r4.addExit("south", None)       # DEATH!
        r4.addExit("east", None)
    # add grabbables to room 4    
        r4.addGrabbable("bread")
        r4.addGrabbable("armor")
    # add items to room 4
        r4.addItem("armory","You walk into the armory and see shiny armor.")
        r4.addItem("faramir", "Faramir says: 'Beware of the different paths that are \npresented to you when choosing the path to Mordor.' ")
        r4.addItem("gandalf", "Gandalf says: 'You will need to head north to reach \nMordor but go to the table before you head out.' ")
        r4.addItem("table","Take some food for your final destination.")
        Game.rooms.append(r4)
    #add exits to room 5
        r5.addExit("north", r6)
    # add items to room 5
        r5.addItem("sauron", "Sauron reads into your mind: 'If you answer this \ngquestion correctly, a door will open which will lead \nyou to Mount Doom.' ")
        
        # This is where I want to create a riddle in order to get to the next path.
        
    #add exits to room 5
        r6.addExit("north", True)
        r6.addItem("sam", "Sam says: 'Mr. Frodo you have all the items now. All you have to do is walk north to end this evilness!")
        Game.currentRoom = r1
        Game.inventory = []
    def win(self):
        self.setStatus("You reach Mount Doom and you destroy the ring by \nthrowing it into the lava. Congratulations you have saved Middle Earth from the evils of Sauron!")
        
        
    #sets up the GUI
    def setupGUI(self):
        # organize the GUI
        self.pack(fill=BOTH, expand=1)
        # setup the player input at the bottom of the GUI
        # the widget is a Tkinter Entry
        # set its background to white
        # bind the return key to the function process()
        # bind the Tab key to the function complete()
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()
        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH // 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)
        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH // 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgray", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)
      
    # set the current room image on the left of the GUI
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="orcs.gif")
        elif (Game.currentRoom == True):
            Game.img = PhotoImage(file="mountdoom.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)
        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img
    
    # sets the status displayed on the right of the GUI
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disable it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        Game.inventory.sort()
        x = ["sting","map","ring","armor","bread","diary"]
        x.sort()
        if (Game.currentRoom == True and Game.inventory == x):
            Game.text.insert(END, "You reach Mount Doom and you destroy the ring by throwing it into the lava. Congratulations you have saved \nMiddle Earth from the evils of Sauron!")
        if (Game.currentRoom == True and Game.inventory != x):
            Game.text.insert(END, "You need all the items in order to finish the game")
        if (Game.currentRoom == None):# if dead, let the player know
            Game.text.insert(END, "A pack of Orcs surround you and burns you alive. \nYou will have to restart the game again :(((")
        else:# otherwise, display the appropriate status
            Game.text.insert(END, "{}\n\n{}\nIn your pack, you are holding: {}""\n\n".format(status, Game.currentRoom, Game.inventory))
            
            Game.text.config(state=DISABLED)
            # support for tab completion
            # add the words to support
            #if (Game.currentRoom != None):
             #   Game.words = VERBS + QUIT_COMMANDS + Game.inventory + Game.currentRoom.exits + Game.currentRoom.items + Game.currentRoom.grabbables
                
    def play(self):
        self.createRooms()
        self.setupGUI()
        self.setRoomImage()
        self.setStatus(
            "WELCOME TO MIDDLE EARTH! Along your journey to destroy \nthe one ring, you will meet some people that will guide you to Mount doom. Make sure you grab any items might \nbe hinted!")
        
        
    # processes the player's input
    def process(self, event):
        # grab the player's input from the Entry widget
        action = Game.player_input.get()
        # set the user's input to lowercase
        action = action.lower().strip()
        
        # exit the game if the player wants to leave
        if (action in QUIT_COMMANDS):
            exit(0)
            
        # if the current room is None, then the player is dead
        # this only happens if the player goes south when in room 4
        if (Game.currentRoom == None):
            # clear the player's input
            Game.player_input.delete(0, END)
            return
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs\nare {}.".format(", ".join(VERBS))
    
        # split the user input into words (words are separated by
        #  spaces) and store the words in a list
        words = action.split()
    
        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]
    
        # we need a valid verb
        if (verb in VERBS):
            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "You can't go in that direction."
            
                # check if the noun is a valid exit
                if (noun in Game.currentRoom.exits):
                    # get its index
                    i = Game.currentRoom.exits.index(noun)
                    # change the current room to the one
                    # that is associated with the specified
                    # exit
                    Game.currentRoom = Game.currentRoom.exitLocations[i]
                    # set the response (success)
                    response = "You walk {} and your path leads to another \npart of Middle Earth.".format(noun)
            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "You don't see that item."
            
                # check if the noun is a valid item
                if (noun in Game.currentRoom.items):
                    # get its index
                    i = Game.currentRoom.items.index(noun)
                    # set the response to the item's
                    # description
                    response = Game.currentRoom.itemDescriptions[i]
            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "You don't see that item."
            
                # check if the noun is a valid grabbable and
                # is also not already in inventory
                if (noun in Game.currentRoom.grabbables and noun not in Game.inventory):
                    # get its index
                    i = Game.currentRoom.grabbables.index(noun)
                    # add the grabbable item to the player's
                    # inventory
                    Game.inventory.append(Game.currentRoom.grabbables[i])
                    # set the response (success)
                    response = "You take {}.".format(noun)
        # display the response on the right of the GUI
        # display the room's image on the left of the GUI
        # clear the player's input
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)
    
    def complete(self,event):
        pass
    
    
############    
### MAIN ###
############
WIDTH = 800
HEIGHT = 800

window = Tk()
window.title("Lord of the Rings(Room Adventure)")
g = Game (window)
g.play()
window.mainloop()