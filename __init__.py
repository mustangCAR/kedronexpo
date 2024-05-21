from tkinter import *
from tkinter import ttk
from os import path as p
import tkinter.font as tkFont
import webbrowser
class App(Tk):
    cyan = "#00ffff"
    white = "#ffffff"
    grey = "#f3f3f3"
    hyperlink = "#0000ee"
    dir_ = p.dirname(__file__)
    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)
        self.setup()
        self.frames()
        self.top_media()
        self.bottom_media()
        self.credits_media()
        self.mainloop()

        
    def setup(self):
        self.geometry(f"{self.width}x{self.height}+{self.xpos}+{self.ypos}")
        self.title(self.titl)
        self.iconbitmap(p.join(self.dir_, "Logo.ico"))

    def frames(self):
        self.top_frame = Frame(self, bg = self.cyan, width = self.width, height = self.height * 0.2)
        self.top_frame.pack(side = TOP, fill = BOTH, expand = True)
        self.bottom_frame = Frame(self, bg = self.grey, width = self.width, height = self.height * 0.7)
        self.bottom_frame.pack(side = TOP, fill = BOTH, expand = True)
        self.credit = Frame(self, bg = self.white, width = self.width, height = self.height * 0.1)
        self.credit.pack(side = TOP, fill = BOTH, expand = True)

    def top_media(self):
        self.logo = PhotoImage(file = p.join(self.dir_, "Logo.png"))
        Label(self.top_frame, image = self.logo, compound = LEFT, text = "  Kedron Expo 2024", font = ("TkDefaultFont", 30), bg = self.cyan).pack(padx = 20, pady = 20)

    def bottom_media(self):
        self.rabbit = PhotoImage(file = p.join(self.dir_, "rabbit.png"))
        self.ufo = PhotoImage(file = p.join(self.dir_, "shmup.png"))
        self.face = PhotoImage(file = p.join(self.dir_, "SmileyFace.png"))
        ttk.Button(self.bottom_frame, image = self.ufo, compound = LEFT, text = "Play Shmup!, a shoot-em-up game",
                                command = lambda : self.run("shmup")).pack(padx = 20, pady = 20)
        ttk.Button(self.bottom_frame, command = lambda : self.run("jumpy"), image = self.rabbit, compound = LEFT, text = "Play Jumpy!, a platformer").pack(padx = 20, pady = 20)
        ttk.Button(self.bottom_frame, command = lambda : self.run("pong"), image = self.face, compound = LEFT, text = "Play Pong!, with my website's smiley!").pack(padx = 20, pady = 20)
    def credits_media(self):
        Label(self.credit, text = "Created by Raghav Agrawal - ragra3@eq.edu.au - Visit me on", bg = self.white, font = ("TkDefaultFont", 10)).pack(side = LEFT, padx = (50, 0))
        l = Label(self.credit, text = "https://wonderweb.live", font = ("TkDefaultFont", 10), fg = self.hyperlink, bg = self.white, underline = True, cursor = "hand2")
        l.pack(side = LEFT, padx = (0, 50))
        f = tkFont.Font(l, l.cget("font"))
        f.configure(underline = True)
        l.configure(font=f)
        l.bind("<Button-1>", lambda e: webbrowser.open("https:/wonderweb.live"))

    def run(self, file):
        exec(f'''
from {file} import main
main()
        ''')
if __name__ == "__main__":
    global game
    game = App(width = 600, height = 600, xpos = 400, ypos = 10,
               titl = "Choose a game to run!")
