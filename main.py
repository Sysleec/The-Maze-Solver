from window import *


def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(200, 0), Point(200, 200)), "white")
    win.draw_line(Line(Point(300, 300), Point(200, 200)), "white")
    win.draw_line(Line(Point(100, 100), Point(150, 150)), "white")

    win.wait_for_close()


main()
