from window import *
from cell import *


def main():
    win = Window(800, 600)

    ce = Cell(win)
    ce.has_left_wall = False
    ce.draw(50, 50, 100, 100)

    ce = Cell(win)
    ce.has_top_wall = False
    ce.has_bottom_wall = False
    ce.draw(200, 200, 250, 250)

    win.wait_for_close()


main()
