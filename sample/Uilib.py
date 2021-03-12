import sys
import os
import curses

EXIT = 0
CONTINUE = 1

FOCUS = curses.A_BOLD | curses.A_STANDOUT
NO_FOCUS = curses.A_NORMAL

class Pyref():
    UP = -1
    LEFT = -1
    DOWN = 1
    RIGHT = 1
    MARKING = curses.A_STANDOUT
    NO_MAKING = curses.A_NORMAL

    def __init__(self):
        self.win = curses.newwin(y, x, 0, 0)
        self.Y, self.X = self.win.getmaxyx()
        self.WIN_LINES = curses.LINES -3
        self.topLineNum = 0
        self.highlightLineNum = 0
        self.markedLineNum = []
        self.topbarFocus = 0
        self.display_pos = []

        self.MakeMainWindow()

    def MakeMainWindow(self):
        y, x = 2, 1
        self.topBar = self.win.subwin(0, self.X, 0, 0)

        # indexWin
        height, width = self.Y-3, int(self.X*0.3)-2
        self.indexWin = self.win.subwin(height, width, y, x)
        self.indexTextLengdth = width

        # titleWin
        y, x = 2, int(self.X*0.3)+1
        height, width = 2, self.X - (int(self.X*0.3))-2
        self.titleWin = self.win.subwin(height-1, width, y, x)

        # previewWin
        y, x = height*3, int(self.X*0.3)+1
        height, width = self.Y-y, self.X-int(self.X*0.3)-2
        self.previewWin = self.win.subwin(height-1, width, y, x)

        self.Frame()
        self.Topbar()
        self.win.refresh()


    def Frame(self):
        # indexFrame
        self.win.attrset(color_red | curses.A_BOLD)
        y, x = 2, 1
        height, width = self.Y-3, int(self.X*0.3)-2
        rectangle(self.win, y-1, x-1, height+2, width+x)

        self.win.attrset(color_blue | curses.A_BOLD)
        # titleFrame
        y, x = 2, int(self.X*0.3)+1
        height, width = 2, self.X-(int(self.X*0.3))-2
        rectangle(self.win, y-1, x-1, height+2, width+x)

        #prewiew
        y, x = 2, height*3, int(self.X*0.3)+1
        height, width = self.Y-y, self.X-(int(self.X*0.3))-2
        rectangle(self.win, y-1, x-1, height+(y-1), width+x)

        self.win.attrset(color_normal | curses.A_NORMAL)

        def Topbar(self):
            space = 2
            self.menufunc = ('Compose', 'Save', 'Delete')
            self.topBar.addstr(0, 0, ' '*x, curses.A_STANDOUT | curses.A_BOLD)
            for f in self.menufunc:
                self.topBar.addstr(0, space, f[0], curses.A_STANDOUT | curses.A_BOLD | curses.A_UNDERLINE)
                self.topBar.addstr(0, space+1, f[1:], curses.A_STANDOUT | curses.A_BOLD)
                self.display_pos.append(space)
                space = space + len(f) + 2
            self.topBar.addstr(0, x-10, "Pyref", curses.A_STANDOUT)
            self.topBar.addstr(0, self.display_pos[self.tobarFocus], self.menufunc[self.topbarFocus][0], )
            self.topBar.addstr(0, self.display_pos[self.topbarFocus]+1, self.menufunc[self.topbarFocus][1:], )
            self.topBar.refresh()


def main(stdscr):
    global screen, color_red, color_green, color_blue, color_normal, y, x
    screen = stdscr

    screen.keypad(True)
    curses.noecho()
    curses.cbreak()
    y, x = screen.getmaxyx()

    # setting colors
    curses.start_color()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, 0)
    curses.init_pair(2, curses.COLOR_GREEN, 0)
    curses.init_pair(3, curses.COLOR_BLUE, 0)
    curses.init_pair(4, 7, 0)
    color_red = curses.color_pair(1)
    color_green = curses.color_pair(2)
    color_blue = curses.color_pair(3)
    color_normal = curses.color_pair(4)




if __name__ == "__main__":
    curses.wrapper(main)
