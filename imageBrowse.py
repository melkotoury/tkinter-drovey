from Tkinter import *
from PIL import ImageTk, Image
import tkFileDialog
import tkMessageBox


app = Tk()
app.title("DROVEY")
app.geometry('720x480+200+200')

iconImg = ImageTk.PhotoImage(file='img/icon.png')
app.call('wm', 'iconphoto', app._w, iconImg)


def imageBrowse():
    app.fileName = tkFileDialog.askopenfilename(filetypes=(("PNG Extentions","*.png"),("JPG Extentions","*.jpg"),("All Files", "*.*") ))
    fo = open("imgUrl.txt", "wb")
    fo.write( app.fileName);

    # Close opend file
    fo.close()
    tkMessageBox.showinfo("Your Image was Selected", "You Successfully selected an Image , Go on and open it!!")
    bOpenImage['state'] = 'normal'
def imageOpen():
    app.destroy()
    import use_roipoly

welcomeMessage = StringVar()
welcomeMessage.set("Please Select the Image")
lWelcome= Label(app,textvariable=welcomeMessage , height=4)
lWelcome.pack()

bBrowseImage=Button(app,text="Browse Image" , bg="orange",fg="white", width=20 , command=imageBrowse)
bBrowseImage.pack(padx=15,pady=15,ipadx=10,ipady=10)


bOpenImage=Button(app,text="Open Image" , bg="orange",state=DISABLED,fg="white", width=20 , command=imageOpen)
bOpenImage.pack(padx=15,pady=15,ipadx=10,ipady=10)

app.mainloop()