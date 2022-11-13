# imports
import pyqrcode as qr
from tkinter import *
from tkinter.filedialog import *

#global variables
window = Tk()
window.geometry("500x300")
window.title("QR Code Generator")

linkOrtext = StringVar()

# functions


def qr_generator():
    str1 = linkOrtext.get()
    url = qr.create(str1)
    save_path = asksaveasfilename()
    url.png(save_path+'QRcode.png')


def exitNow():
    window.destroy()


def main():
    lbl0 = Label(window, text="Enter link or text:",
                 width=20, font=("arial", 10, "bold"))
    lbl0.pack()
    ent0 = Entry(window, textvar=linkOrtext)
    ent0.pack()
    btn0 = Button(window, text="Generate QR", width=20,
                  bg='brown', fg='white', command=qr_generator)
    btn0.pack()
    btn1 = Button(window, text="Exit", width=12,
                  bg='brown', fg='white', command=exitNow)
    btn1.pack()


if __name__ == "__main__":
    main()
    mainloop()
