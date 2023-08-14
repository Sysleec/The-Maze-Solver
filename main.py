from window import Window
from maze import Maze
import sys


def main():
    width = 800
    height = 600
    num_rows = 12
    num_cols = 16
    margin = 60
    cell_size_x = (width - 2 * margin) / num_cols
    cell_size_y = (height - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)

    win = Window(width, height)

    maze = Maze(margin, margin, num_rows, num_cols,
                cell_size_x, cell_size_y, win, 10)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")
    win.wait_for_close()


main()
