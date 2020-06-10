
from tkinter import *
from random import *
#-----------------------------------------Getting random Words------------------------------------------------------------------
import requests

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

response = requests.get(word_site)
WORDS = response.content.splitlines()
#----------------------------------------Defining some helper functions-----------------------------------------------------------
def getRandom(n):
    res = ''
    for i in range(n - 1):
        res += chr(randint(33, 126))
    
    return res

def replaceRandom(text):
    for i in len(text)//2:
        text.replace(text[i], chr(randint(33,126)))
    return text  
# 1 = HumanReadable
# 2 = Complete random
# 3 = Only word

condOne = False
condTwo = False
condThree = False
def setOne():
    global condOne
    condOne = not condOne
def setTwo():
    global condTwo
    condTwo = not condTwo
def setThree():
    global condThree
    condThree = not condThree

#---------------------------------------------Making the main App-------------------------------------------------------------
root = Tk()
root.title("Random Password Generator")
root.geometry('400x300')
root.resizable(width = False, height = False)
#------------------------------------------Creating the frame------------------------------------------------------------------
frame = Frame(root,bg = "black",height = 300,width = 400)
frame.grid()
#-----------------------------------------------Creating Lable------------------------------------------------------------------
mainlab = Label(root,text = "Password : ",bg = "black", font = "Elianto",padx = 4,pady = 4,fg = '#21d136')
mainlab.place(x = 13,y = 30)
#-----------------------------------------------Creating the display box---------------------------------------------------------
display = Entry(root,width = 30)
display.config(bg = 'black', fg = "#21d136",bd = 5)
display.place(x = 98, y = 30)
#-----------------------------------------------Making some CheckBoxes------------------------------------------------------------
def makeCheckBox(label,xpos,ypos,comm,wdth):
    cbox = Checkbutton(root, bg = "black", fg = "#21d136",font = "Elianto",height = 1, width = wdth, text = label,command = comm)
    cbox.place(x = xpos, y = ypos)
    
makeCheckBox("Easy to Read",50,100,setOne,12)
makeCheckBox("Completely Random", 50, 135, setTwo, 17)
makeCheckBox("Random Word", 50, 170, setThree, 13)
#---------------------------------------------Creating an Entry For Length---------------------------------------------------------
getLen = Entry(root, width = 5)
getLen.config(bg = 'black', fg = "#21d136",bd = 2)
getLen.place(x = 120,y = 200)
labb = Label(root, text = "Length :")
labb.config(bg = "black", font = "Elianto",padx = 4,pady = 4,fg = '#21d136')
labb.place(x = 46, y = 200)
k = [i for i in WORDS if len(i) == getLen.get()]
#----------------------------------------------Helper Method for Generating Password----------------------------------------------------------
def getLengthedWord(n):
    res = ''
    res = k[randint(0,len(k))]
    return res
def makePassword():
    res = ''
    c1 = condOne
    c2 = condTwo
    c3 = condThree
    if c1:
        try:
            
            res = replaceRandom(getLengthedWord(getLen.get()))
          
        except:
            display.delete(0,len(display.get()))
            display.insert(0, "Please Enter a valid length or press generate again")
    if c2:
        try:
            res = getRandom(int(getLen.get()))
        except:
            display.delete(0,len(display.get()))
            display.insert(0, "Please Enter a valid length or press generate again")
    if c3:
        try:
            res = WORDS[randint(0, len(WORDS))][:int(getLen.get())]
        except:
            display.delete(0,len(display.get()))
            display.insert(0, "Please Enter a valid length or press generate again")
    
    display.delete(0,len(display.get()))
    display.insert(0, res)
            
    


#----------------------------------------------Making the Generate button---------------------------------------------------------
passWord = Button(root, text = "Generate",height = 4)
passWord.config(bg = '#000000', fg = "#21d136", font = ("Elianto", 15), pady = 2,bd = 2,padx = 5, command = makePassword)
passWord.place(x = 250,y = 100)
#---------------------------------------------------------------------------------------------------------------------------------
labbb = Label(root, text = "|The 'Easy To Read' needs some Work * ~ *|")
labbb.config(bg = "black", font = "Elianto",padx = 4,pady = 4,fg = '#21d136')
labbb.place(x = 46, y = 250)
root.mainloop()
