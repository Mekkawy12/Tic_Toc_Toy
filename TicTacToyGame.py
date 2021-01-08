from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint
activePlayer=1
P1=[]
P2=[]
Buttons=[0,1,2,3,4,5,6,7,8]
root=Tk()
root.title("Tic Toc toy: Active Player 1")
style=ttk.Style()
style.theme_use('classic')
bu1=ttk.Button(root,text='')
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda  : BuClick(1))


#creating buttons
def createButtons():
    global Buttons
    buNumber=0
    for row in range(0,3):
        for column in range(0,3):
            Buttons[buNumber]=ttk.Button(root,text='')
            Buttons[buNumber].grid(row=row,column=column,sticky='snew',ipadx=40,ipady=40)
            Buttons[buNumber].config(command=lambda:BuClick(buNumber))
            buNumber+=1
    
    Buttons[0].config(command=lambda : BuClick(1))
    Buttons[1].config(command=lambda : BuClick(2))
    Buttons[2].config(command=lambda : BuClick(3))
    Buttons[3].config(command=lambda : BuClick(4))
    Buttons[4].config(command=lambda : BuClick(5))
    Buttons[5].config(command=lambda : BuClick(6))
    Buttons[6].config(command=lambda : BuClick(7))
    Buttons[7].config(command=lambda : BuClick(8))
    Buttons[8].config(command=lambda : BuClick(9))

#clink operation
def BuClick(id):
    global activePlayer
    global P1
    global P2
    if activePlayer ==1:
        setLayuot(id,'X')
        P1.append(id)
        root.title('Tic Toc Toy : Active Player 2')
        activePlayer=2
        if len(P1)==3:
            checkWinner(P1,1)
            
    else:
        setLayuot(id,'O')
        
        P2.append(id)
        root.title('Tic Toc Toy : Active Player 1')
        activePlayer=1
        if len(P2)==3:
            checkWinner(P2,2)
        
            
#set and disable buttons
def setLayuot(id,text):
    if id==1:
        Buttons[0].config(text=text)
        Buttons[0].state(['disabled'])
    elif id==2:
        Buttons[1].config(text=text)
        Buttons[1].state(['disabled'])
    elif id==3:
        Buttons[2].config(text=text)
        Buttons[2].state(['disabled'])
    elif id==4:
        Buttons[3].config(text=text)
        Buttons[3].state(['disabled'])
    elif id==5:
        Buttons[4].config(text=text)
        Buttons[4].state(['disabled'])
    elif id==6:
        Buttons[5].config(text=text)
        Buttons[5].state(['disabled'])
    elif id==7:
        Buttons[6].config(text=text)
        Buttons[6].state(['disabled'])
    elif id==8:
        Buttons[7].config(text=text)
        Buttons[7].state(['disabled'])
    elif id==9:
        Buttons[8].config(text=text)
        Buttons[8].state(['disabled'])

#checking the winner
def checkWinner(P,Winner):
  
    if (1 in P) and (2 in P) and (3 in P):
        messagebox.showinfo(title='Cong.',message="Player {} is the Winner".format(Winner))
        clear()
    if (4 in P) and (5 in P) and (6 in P):
        messagebox.showinfo(title='Cong.',message="Player {} is the Winner".format(Winner))
        clear()
    if (7 in P) and (8 in P) and (9 in P):
        messagebox.showinfo(title='Cong.',message="Player {} is the Winner".format(Winner))
        clear()
    if (1 in P) and (5 in P) and (9 in P):
        messagebox.showinfo(title='Cong.',message="Player {} is the Winner".format(Winner))
        clear()
    if (3 in P) and (5 in P) and (7 in P):
        messagebox.showinfo(title='Cong.',message="Player {} is the Winner".format(Winner))
        clear()
    if (1 in P) and (4 in P) and (7 in P):
        messagebox.showinfo(title='Cong.',message="Player {} is the Winner".format(Winner))
        clear()
    if (2 in P) and (5 in P) and (8 in P):
        messagebox.showinfo(title='Cong.',message="Player {} is the Winner".format(Winner))
        clear()
    if (3 in P) and (6 in P) and (9 in P):
        messagebox.showinfo(title='Cong.',message="Player {} is the Winner".format(Winner))
        clear()
#auto play function to play with the computer
def autoPlay():
    global P1
    global P2
    emptyP=[]
    for cell in range(1,10):
        if (cell not in P1) and (cell not in P2):
            emptyP.append(cell)
    index=randint(0,len(emptyP)-1)
    BuClick(emptyP[index])
def clear():
    global activePlayer
    global P1
    global P2
    for button in Buttons:
        button.config(text='',state=NORMAL)
        
    P1=[]
    P2=[]
    root.title("Tic Toc toy: Active Player 1")
    activePlayer=1



createButtons()
root.mainloop()