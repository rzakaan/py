#!/opt/homebrew/bin/python3
import argparse
from tkinter import *
from tkinter import ttk
from enum import Enum


class Layout(Enum):
    LEFT = 0,
    MID = 1,
    RIGHT = 2


# const string values
STR_TITLE = "File Explorer"
FOLDER_ICON_24_BYTES = b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAQAAABKfvVzAAAAVElEQVQ4y2NgGCbgv/v/x/+RQT0hDff/owP8Wv7//f8fiRf+//d/TPD4vwcODTi1PMKpAasr/iOpoYOGfyNRw3+aa3j0nxiAlDQ80JL3fwKJb4gDAP09+NbCRr6DAAAAAElFTkSuQmCC'
FILE_ICON_24_BYTES = b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAAU0lEQVR4Ae3RsRGAMAzAQI8XpmJXexDRUGMQDReiBb5QzBcwgKJvt0DS5xHO4iKBWEAgEugRAQjkPYAE+n4M0PRpYD3wwHqQ+PIOsAHF8woYMV0Ho2+fqGdBTnoAAAAASUVORK5CYII='


def convertBase64(filename: str) -> str:
    import binascii
    import base64
    with open(filename, 'rb') as f:
        content = f.read()
    image_base64 = base64.b64encode(content)
    print(image_base64)


def main():
    window = FileExplorer()
    window.mainloop()


class FileComponent(Frame):
    def __init__(self, master, text, img=None):
        super().__init__(master, background="green")
        ttk.Label(self, image=img).pack()
        ttk.Label(self, text=text).pack()


class FileExplorer(Tk):
    PADX = 5
    PADY = 5

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title(STR_TITLE)
        self.geometry("640x480")
        self.resizable(True, True)

        # string var
        CUR_DIR_VAR = StringVar(self)

        # style
        self.style = ttk.Style(self)
        self.style.theme_use("aqua")
        self.style.configure('TFrame', background='blue', foreground='red', relief='sunken')

        # load icons
        self.FILE_ICON_24 = PhotoImage(data=FILE_ICON_24_BYTES)
        self.FOLDER_ICON_24 = PhotoImage(data=FOLDER_ICON_24_BYTES)

        # component decleration
        favbar = ttk.LabelFrame(self, borderwidth=5, text="Favorites", cursor="hand2")
        favbar.pack(side=LEFT, fill="both", padx=self.PADX, pady=self.PADY)
        ttk.Label(favbar, text="Computer").pack()
        ttk.Label(favbar, text="Home").pack()
        ttk.Label(favbar, text="Desktop").pack()

        searchbar = ttk.LabelFrame(self, text="")
        searchbar.pack(side=TOP, fill="x", pady=self.PADY)
        ttk.Entry(searchbar, textvariable=CUR_DIR_VAR).pack(expand=True, side=LEFT, fill="x")
        ttk.Button(searchbar, image=self.FOLDER_ICON_24).pack(side=RIGHT)

        infobar = ttk.LabelFrame(self)
        infobar.pack(side=RIGHT, fill="both", padx=self.PADX, pady=self.PADY)
        ttk.Label(infobar, text="Information").pack()
        ttk.Label(infobar, text="File Size").pack()
        ttk.Label(infobar, textvariable=CUR_DIR_VAR).pack()

        # file frame
        # directories and files show
        fileframe = ttk.LabelFrame(self, text=" ").pack(side=BOTTOM, fill="both")
        import os
        print(os.curdir)
        CUR_DIR_VAR.set("./Home")
        for f in os.listdir():
            FileComponent(fileframe, text=f, img=self.FILE_ICON_24).pack(side=TOP)

        # fileComponent = ttk.Frame(fileframe)
        # ttk.Label(fileComponent, image=self.FILE_ICON_24).pack()
        # ttk.Label(fileComponent, text="File").pack()
        # fileComponent.pack()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=STR_TITLE)
    parser.add_argument('--icon', help='generate hex dump from png')
    args = parser.parse_args()

    if args.icon:
        convertBase64(args.icon)
        exit(0)

    main()
