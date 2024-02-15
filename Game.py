#####################################################################
# author:      Danison Zhang    
# date:       1/14/24
# description: program 7, happy valentines
#####################################################################

from tkinter import *
from CardGame import *
from PIL import Image, ImageTk
from time import sleep

ROWS = 4
COLUMNS = 4

## Functions ##

# displays the cards and determines the winner
def play_game():
    if g1.deck.size() == 0:
        l3['text'] = "Out of cards. Press 'Quit' or 'Restart'"
    else:
        # takes out 2 card objects from the list
        card1 = g1.deck.draw()
        card2 = g1.deck.draw()
        
        # retrieves the str of the path to the png
        path1 = card1.imagefile
        path2 = card2.imagefile
        
        img1 = config_image(path1)
        img2 = config_image(path2)
        
        p1.configure(image=img1)
        p1.image = img1
        
        p2.configure(image=img2)
        p2.image = img2
        
        l3['text'] = winner(card1, card2)

# resets the deck and fills it up with new cards, then shuffles
def restart():
    g1.deck.reset()
    g1.deck.shuffle()
    
    # resets the text and image to the default
    l3['text'] = 'Who wins?'
    defimg = config_image('default.png')
    
    p1.configure(image=defimg)
    p1.image = defimg
    
    p2.configure(image=defimg)
    p2.image = defimg
    
# configures the image to be able to display on tkinter
def config_image(path):
    img = ImageTk.PhotoImage(Image.open(f'./images/{path}'))
    return img
    
# determins which card has the higher value
def winner(card1, card2):
    if card1 > card2:
    # converts the score to an int so we can increment it
        text = int(s1['text'])
        s1.config(text = text + 1)
        return "COMPUTER WINS"
    elif card1 == card2:
        return "DRAW"
    else:
        text = int(s2['text'])
        s2.config(text = text + 1)
        return "YOU WIN"

## MAIN ##

window = Tk()

default = PhotoImage(file='./images/default.png')

window.title("CSC131 Card Game")
window.geometry('1100x900')

# creates the deck object and starts the game
g1 = Game()

# Text at the top showing which side is the computer and the person
l1 = Label(window, text="Computer picked", font=('Arial', 20))
l1.grid(row=0, column=0, sticky=W, ipadx=20)

l2 = Label(window, text="You picked", font=('Arial', 20))
l2.grid(row=0, column=4, sticky=E, ipadx=20)

# Picture of the cards
p1 = Label(window, image=default)
p1.grid(row=1, column=0, columnspan=2, sticky=W, padx=10, pady=10)

p2 = Label(window, image=default)
p2.grid(row=1, column=4, columnspan=2, sticky=E, padx=10, pady=10)

# Dynamic text that displays the winner
l3 = Label(window, text="Who wins?", font=('Arial', 25))
l3.grid(row=2, column=0, columnspan=100, sticky=N+S+E+W)

# Keeps score of the game
s1 = Label(window, text='0', font=('Arial', 15))
s1.grid(row=2, column=0)

s2 = Label(window, text='0', font=('Arial', 15))
s2.grid(row=2, column=5)

# The buttons that allow you to play, restart, or quit the game
b1 = Button(window, text="Play", background='light blue', command=lambda: play_game())
b1.grid(row=4, column=0, sticky=W, ipadx=10)

b2 = Button(window, text="Restart", background='light blue', command=lambda: restart())
b2.grid(row=4, column=1, sticky=W, ipadx=10)

b3 = Button(window, text="Quit", background='light blue', command=window.destroy)
b3.grid(row=4, column=4, sticky=E, ipadx=10)

# loops through all the columns so that each one has a weight of 1
for i in range(COLUMNS):
    window.columnconfigure(i, weight=1)
for j in range(ROWS):
    window.rowconfigure(i, weight=1)

window.mainloop()
