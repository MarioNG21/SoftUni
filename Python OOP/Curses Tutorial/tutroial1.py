import curses
from curses import wrapper

stdscr = curses.initscr()


def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.getch()


wrapper(main)
