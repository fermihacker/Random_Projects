# Value Converter
#------------------------------------------------------Importing Essential Libraries----------------------------------------------------------
import tkinter
from tkinter import *
#----------------------------------------------------------------Creating The App-------------------------------------------------------------
root = Tk()
root.title("Value Converter")
root.geometry("400x300")
root.resizable(width = False, height = False)
#---------------------------------------------------------------------------------------------------------------------------------------------
frame = Frame(root,height = 300, width = 400, bg = '#478fc9')
frame.grid()
#---------------------------------------------------------------------------------------------------------------------------------------------
def MainConvert():
    val = valEnter.get()
    try:
        binDisp.delete(first = 0, last = len(binDisp.get()))
        binDisp.insert(0,bin(int(val)).replace('0b', ''))
        octDisp.delete(first = 0, last = len(binDisp.get()))
        octDisp.insert(0,oct(int(val)).replace('0o', ''))
        hexDisp.delete(first = 0, last = len(binDisp.get()))
        hexDisp.insert(0,hex(int(val)).replace('0x', ''))
    except:
        valEnter.delete(0,len(valEnter.get()))
        valEnter.insert(0,"ERROR")
#---------------------------------------------------------------------------------------------------------------------------------------------
MainLab = Label(frame,text = "Value : ", bg = '#478fc9',fg = "#404347",height = 3,width = 4, padx = 2, pady = 2)
MainLab.config(font = ("Futera Medium",15))
MainLab.place(x = 10,y = 3)
#---------------------------------------------------------------------------------------------------------------------------------------------
valEnter = Entry(frame, width = 15,bd = 3, bg = '#478fc9',fg = "black")
valEnter.place(x = 70,y = 20)
#---------------------------------------------------------------------------------------------------------------------------------------------
convButton = Button(frame,width = 7, height  = 2, text = "Convert", padx = 2, pady = 2, command = MainConvert)
convButton.place(x = 260, y = 16)
#---------------------------------------------------------------------------------------------------------------------------------------------
binLab = Label(frame, text = "Binary : ",bg = '#478fc9',fg = "#404347",height = 3,width = 5, padx = 2, pady = 2)
binLab.config(font = ("Futera Medium",15))
binLab.place(x = 10,y = 90)
binDisp = Entry(frame, width = 30,bd = 3, bg = '#478fc9',fg = "black")
binDisp.place(x = 70,y = 107)
#---------------------------------------------------------------------------------------------------------------------------------------------
octLab = Label(frame, text = " Octal  :",bg = '#478fc9',fg = "#404347",height = 3,width = 5, padx = 2, pady = 2)
octLab.config(font = ("Futera Medium",15))
octLab.place(x = 7,y = 140)
octDisp = Entry(frame, width = 30,bd = 3, bg = '#478fc9',fg = "black")
octDisp.place(x = 70,y = 157)
#---------------------------------------------------------------------------------------------------------------------------------------------
hexLab = Label(frame, text = " Hex   :",bg = '#478fc9',fg = "#404347",height = 3,width = 5, padx = 2, pady = 2)
hexLab.config(font = ("Futera Medium",15))
hexLab.place(x = 8,y = 190)
hexDisp = Entry(frame, width = 30,bd = 3, bg = '#478fc9',fg = "black")
hexDisp.place(x = 70,y = 207)
#---------------------------------------------------------------------------------------------------------------------------------------------
root.mainloop()
