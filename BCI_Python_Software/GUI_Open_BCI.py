# Felix Fees GUI for generating individual Data sets for Deep learning
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image




class GUI:
    def __init__(self):
        self.root = Tk()
        self.count = 0
        self.data = StringVar()
        self.image = StringVar()
        # self.var = 0
        self.Path = ''

        self.root.title("MEXLE Open BCI GUI by Felix F. Fees")
        self.root.geometry("1530x790+0+0")
        self.root.iconbitmap("mexle_icon.ico")

        self.label0 = Label(self.root, text="Open BCI-GUI for Data connection with MEXLE BCI",
                            font='Helvetica 10 bold').place(x=320, y=5)
        self.label1 = Label(self.root, text="Hardware: MEXLE IOT, MEXLE BCI-Platine",
                            font='Helvetica 10 bold').place(x=320, y=25)
        self.label2 = Label(self.root, text="Path:", font='Helvetica 10 bold').place(x=5, y=770)
        self.label3 = Label(self.root, text="(c) Hochschule Heilbronn / B. Eng. Felix F. Fees 2020 / 2021",
                            font='Helvetica 10 bold').place(x=1130, y=770)
        self.button0 = Button(self.root, text="Select Path", font='Helvetica 10 bold',
                              command=self.select_path).place(x=1350, y=80)
        self.button1 = Button(self.root, text="Start Data-Collection", font='Helvetica 10 bold',
                              command=self.start_data).place(x=1350, y=120)
        self.button2 = Button(self.root, text="Stop Data-Collection", font='Helvetica 10 bold',
                              command=self.stop_data).place(x=1350, y=160)
        self.button3 = Button(self.root, text="Reset ESP", font='Helvetica 10 bold',
                              command=self.reset_esp).place(x=1350, y=200)
        self.button4 = Button(self.root, text="Exit", font='Helvetica 10 bold',
                              command=self.root.destroy).place(x=1350, y=240)
        # Img 1
        self.canv = Canvas(self.root, width=210, height=90, bg='white')
        self.canv.place(x=5, y=5)
        width = 190
        height = 70
        img = Image.open("HHN.png")
        img = img.resize((width, height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.canv.create_image(10, 10, anchor=NW, image=img)
        # Img2
        self.canv1 = Canvas(self.root, width=90, height=90)
        self.canv1.place(x=220, y=5)
        img1 = Image.open("mexle-logo-large.jpg")
        width1 = 90
        img1 = img1.resize((width1, width1), Image.ANTIALIAS)
        img1 = ImageTk.PhotoImage(img1)
        self.canv1.create_image(0, 0, anchor=NW, image=img1)
        # Plot

        self.canvas1 = Canvas(self.root, width=1340, height=670, bg='white')  # A tk.DrawingArea.
        self.canvas1.place(x=5, y=95)

        self.root.mainloop()

    def select_path(self):
        # Datei auswahl
        self.root.directory = fd.askdirectory()
        print(self.root.directory)
        self.Path = self.root.directory
        self.label4 = Label(self.root, text=self.root.directory, font='Helvetica 10 bold').place(x=50, y=770)

    def start_data(self):
        name = fd.askopenfilename()
        print(name)

    def stop_data(self):
        name = fd.askopenfilename()
        print(name)

    def reset_esp(self):
        name = fd.askopenfilename()
        print(name)


app = GUI()

