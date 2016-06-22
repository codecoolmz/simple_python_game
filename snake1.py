import curses
import time
import random

screen = curses.initscr()
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_GREEN)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)


curses.curs_set(0)
screen.keypad(1)
screen_size = screen.getmaxyx()


screen.addstr(screen_size[0]//2-2, (screen_size[1] - 7)//2-2, 'GREEN SNAKE', curses.color_pair(2))
screen.addstr(screen_size[0]//2, (screen_size[1] - 10)//2, 'Get Ready!', curses.A_BOLD)
screen.addstr(screen_size[0]//2+3, (screen_size[1] - 50)//2+3, '(Use keyboard arrow keys to change direction)')
screen.refresh()
time.sleep(3)
screen.clear()

def main():

    screen.nodelay(1)
    head = [1,1]
    body = [head[:]] * 5
    fantom = body[-1][:]
    screen.border()

    dead = False
    makefood = False
    direction = 0


    while not dead:
        screen.border(0)
        screen.addstr(0, (screen_size[1]//2-13), ' GREEN SNAKE ', curses.color_pair(2))


        while not makefood:
            y, x = random.randrange(1, screen_size[0]-1) , random.randrange(1, screen_size[1]-1)
            if screen.inch(y, x) == ord(' '):
                makefood = True
                screen.addch(y, x, ord('+'))
        if fantom not in body:
            screen.addch(fantom[0], fantom[1], ' ',)
        screen.addch(head[0], head[1], '+', curses.color_pair(1))

        key = screen.getch()
        if key == curses.KEY_RIGHT and direction != 2:
            direction = 0
        if key == curses.KEY_LEFT and direction != 0:
            direction = 2
        if key == curses.KEY_UP and direction != 1:
            direction = 3
        if key == curses.KEY_DOWN and direction != 3:
            direction = 1
        if direction == 0:
            head[1] += 1
        elif direction == 2:
            head[1] -= 1
        elif direction == 1:
            head[0] += 1
        elif direction == 3:
            head[0] -= 1

        fantom = body[-1][:]
        for z in range(len(body)-1, 0, -1):
            body[z] = body[z-1][:]

        body[0] = head[:]

        if screen.inch(head[0], head[1]) != ord(' '):
            if screen.inch(head[0], head[1]) == ord('+'):
                makefood = False
                body.append(body[-1])
            else:
               dead = True
        screen.move(screen_size[0]-1, screen_size[1]-1)
        screen.refresh()
        time.sleep(0.1)
        score = str(len(body)-5)
    screen.clear()
    screen.nodelay(0)
    screen.addstr(screen_size[0]//2, (screen_size[1] - 8)//2, 'Score: ' + score)
    screen.addstr(screen_size[0]//2-1, (screen_size[1] - 7)//2-1, 'Game Over')
    screen.refresh()
    time.sleep(3)


main()
curses.endwin()
