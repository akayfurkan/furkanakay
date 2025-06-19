import random
import curses

# Set up the window
curses.initscr()
window = curses.newwin(20, 60, 0, 0)  # y, x
window.keypad(1)
window.timeout(100)

# Create the snake and food
snake = [[10, 15], [10, 14], [10, 13]]
food = [random.randint(1, 18), random.randint(1, 58)]
window.addch(food[0], food[1], 'O')

# Initial direction
key = curses.KEY_RIGHT

score = 0

while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    # Calculate new head position
    head = [snake[0][0], snake[0][1]]
    if key == curses.KEY_DOWN:
        head[0] += 1
    if key == curses.KEY_UP:
        head[0] -= 1
    if key == curses.KEY_LEFT:
        head[1] -= 1
    if key == curses.KEY_RIGHT:
        head[1] += 1

    snake.insert(0, head)

    # Check for collisions
    if head[0] in [0, 19] or head[1] in [0, 59] or head in snake[1:]:
        curses.endwin()
        quit()

    if head == food:
        score += 1
        food = None
        while food is None:
            nf = [random.randint(1, 18), random.randint(1, 58)]
            food = nf if nf not in snake else None
        window.addch(food[0], food[1], 'O')
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    window.addch(snake[0][0], snake[0][1], '#')

