# main.py
import tkinter as tk
from tkinter import ttk
from pages.home import HomePage
from pages.register import RegisterPage
from pages.calendar import CalendarPage
from pages.search import SearchPage
from pages.timetable import TimetablePage
from pages.notify import NotifyPage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("간단 일정관리 (대학생용)")
        self.geometry("900x600")

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        pages = {
            "Home": HomePage,
            "Register": RegisterPage,
            "Calendar": CalendarPage,
            "Search": SearchPage,
            "Timetable": TimetablePage,
            "Notify": NotifyPage
        }

        for name, PageClass in pages.items():
            frame = PageClass(container, self)
            frame.grid(row=0, column=0, sticky="nsew")
            self.frames[name] = frame

        self.show("Home")

    def show(self, name):
        frame = self.frames.get(name)
        if frame:
            frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()