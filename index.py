from Tkinter import *
from PIL import ImageTk, Image


app = Tk()
app.title("DROVEY")
app.geometry('720x620+200+200')

iconImg = ImageTk.PhotoImage(file='img/icon.png')
app.call('wm', 'iconphoto', app._w, iconImg)


#Methods When Calculate Area is Clicked
def openFileBrowse():
    app.destroy()
    import imageBrowse





welcomeMessage = StringVar()
welcomeMessage.set("Wecome to DROVEY!")
lWelcome= Label(app,textvariable=welcomeMessage , height=4)
lWelcome.pack()

bCalculateArea=Button(app,text="Calculate Area" , bg="orange",fg="white", width=20 , command=openFileBrowse)
bCalculateArea.pack(padx=15,pady=15,ipadx=10,ipady=10)

img = ImageTk.PhotoImage(Image.open("img/logo.png"))
panel = Label(app, image = img)
panel.pack( fill = "both",expand="yes")




app.mainloop()