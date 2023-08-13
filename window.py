from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = ("The Maze Solver on Python")
        self.__canvas = Canvas(self.__root, bg="black",
                               width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__winRunning = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__winRunning = True
        while self.__winRunning:
            self.redraw()
        print("Close program")

    def close(self):
        self.__winRunning = False
