#------------------------------------------------Importing Essential Libraries---------------------------------------------
import tkinter as tk
from tkinter import *
import tkinter.messagebox as outBox
from math import *
#--------------------------------------------------Creating The Main App----------------------------------------------------
root = Tk()
root.title('Calculator')
root.geometry('375x500')
root.resizable(width = False, height = False)
#--------------------------------------------Creating A Frame to contain Widgets---------------------------------------------
frame = Frame(root,bg = '#000000', height=500, width=400)
frame.grid()
#------------------------------------------------------Creating a Label------------------------------------------------------
disp = Label(frame,text="Display", fg="black", bg="white", height = 3,width=10, font = 'Moon',padx = 6,pady = 2)
disp.config(bg = 'black', fg = "#00db3a", font = ("Moon", 16,'bold'))
disp.place(x = 0, y = 14)
#-------------------------------------------------Creating An Output Display-------------------------------------------------
out = Entry(frame,width = 27,font = ("Apple Symbols",17))
out.config(bg = 'black', fg = "#00db3a",bd = 5)
out.place(x = 98, y = 25)
#--------------------------------------------------Method To create a Button------------------------------------------------
def makeButton(name,x,y,comm):
    butt = Button(root,text = str(name), height = 2,width = 5, font = 'Moon',command = lambda : out.insert(len(out.get()),comm))
    butt.config(bg = '#000000', fg = "#830fff", font = ("Moon", 20), pady = 2,bd = 2,padx = 5)
    butt.place(x = x, y = y)
#--------------------------------------------------Command for the '=' button-----------------------------------------------
def equalscomm():
    try:
        equn = eval(out.get())
        out.delete(0,len(out.get()))
        out.insert(0, equn)
    except:
        out.delete(0, len(out.get()))
        out.insert(0,'Syntax Error')        
#---------------------------------------------Creating number and function buttons-------------------------------------------
makeButton('1',10,100,'1')
makeButton('2',78,100,'2')
makeButton('3',146,100,'3')
makeButton('4',10,153,'4')
makeButton('5',78,153,'5')
makeButton('6',146,153,'6')
makeButton('7',10,206,'7')
makeButton('8',78,206,'8')
makeButton('9',146,206,'9')
makeButton('0',78,259,'0')
makeButton('.',10,259,'.')
makeButton('+',220,153,'+')
makeButton('-',220,206,'-')
makeButton('ₓ',293,153,'*')
makeButton('/',293,206,'/')
makeButton('^',293,259,'**')
makeButton('(',220,312,'(')
makeButton(')',293,312,')')
makeButton('!',220,259,'factorial(')
makeButton('sin',10,312,'sin(')
makeButton('cos',78,312,'cos(')
makeButton('tan',146,312,'tan(')
makeButton('π',220,365,'pi')
makeButton('asin',10,365,'asin(')
makeButton('acos',78,365,'acos(')
makeButton('atan',146,365,'atan(')
makeButton('ln',293,365,'log(')
#------------------------------------------------Creating the clear button------------------------------------------------
clear = Button(root,text = 'Clear', height = 2,width = 5, font = 'Moon',command = lambda : out.delete(0, len(out.get())))
clear.config(bg = '#000000', fg = "#830fff", font = ("Moon", 20), pady = 2,bd = 2,padx = 5)
clear.place(x = 220, y = 100)
#-------------------------------------------------Creating the '=' button---------------------------------------------------
equals = Button(root,text = '=', height = 2,width = 5, font = 'Moon',command = equalscomm)
equals.config(bg = '#000000', fg = "#830fff", font = ("Moon", 20), pady = 2,bd = 2,padx = 5)
equals.place(x = 146, y = 259)
#-------------------------------------------------Creating the delete button------------------------------------------------
delButton = Button(root,text = 'del', height = 2,width = 5, font = 'Moon',command = lambda :out.delete(len(out.get()) - 1))
delButton.config(bg = '#000000', fg = "#830fff", font = ("Moon", 20), pady = 2,bd = 2,padx = 5)
delButton.place(x = 293, y = 100)
#-------------------------------------------------Creating the 'Quit' button-----------------------------------------------
qButton = Button(root,text = 'Quit', height = 2,width = 5, font = 'Moon',command = tk._exit)
qButton.config(bg = '#000000', fg = "#830fff", font = ("Moon", 20), pady = 2,bd = 2,padx = 5)
qButton.place(x = 146, y = 440)
#--------------------------------------------------Running the Application--------------------------------------------------


root.mainloop()
