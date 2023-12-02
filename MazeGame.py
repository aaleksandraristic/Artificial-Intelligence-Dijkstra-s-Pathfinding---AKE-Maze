from tkinter import Label, Button, Entry, StringVar, Text
from pyamaze import maze, agent, COLOR, textLabel
import random

def dijkstra(m, *h, start=None):
    if start is None:
        start = (m.rows, m.cols)

    hurdles = [(i.position, i.cost) for i in h]

    unvisited = {n: float('inf') for n in m.grid}
    unvisited[start] = 0
    visited = {}
    revPath = {}
    while unvisited:
        currCell = min(unvisited, key=unvisited.get)
        visited[currCell] = unvisited[currCell]
        if currCell == m._goal:
            break
        for d in 'EWNS':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in visited:
                    continue
                tempDist = unvisited[currCell] + 1
                for hurdle in hurdles:
                    if hurdle[0] == currCell:
                        tempDist += hurdle[1]

                if tempDist < unvisited[childCell]:
                    unvisited[childCell] = tempDist
                    revPath[childCell] = currCell
        unvisited.pop(currCell)

    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[revPath[cell]] = cell
        cell = revPath[cell]

    return fwdPath, visited[m._goal]

enemies=[]
def generate_random_coordinates(myMaze):
    row = random.randint(0, myMaze.rows - 1)
    col = random.randint(0, myMaze.cols - 1)
    return row, col
def create_enemies(num, myMaze):
    enemies = []
    for _ in range(num):
        new_enemy = agent(myMaze, *generate_random_coordinates(myMaze), color=COLOR.red, filled=True)
        new_enemy.cost = 100
        enemies.append(new_enemy)
    return enemies
def set_enemies(myMaze, num):
    # Clear existing agents
    myMaze._agents.clear()

    # Set new enemies based on user input
    enemies = create_enemies(num, myMaze)

    # Add new enemies to the maze
    myMaze._agents.extend(enemies)
def play_game():
    myMaze.run()
def reset_game():
    myMaze._win.destroy()
    create_and_run_maze()

def create_and_run_maze():
    global myMaze  # Use global to reference the outer myMaze variable
    myMaze = maze(15, 15)
    myMaze.CreateMaze(1, 1, loopPercent=100)

    num_enemies = 5
    set_enemies(myMaze, num_enemies)

    start_position = (myMaze.rows, myMaze.cols)
    path, c = dijkstra(myMaze, start=start_position)
    textLabel(myMaze, 'Total Cost', c)

    player_agent = agent(myMaze, *start_position, color=COLOR.blue, filled=False, footprints=True)
    myMaze.tracePath({player_agent: path})

    # Create buttons
    button_play_game = Button(myMaze._win, text="Play Again", height=5, width=25,
                              bg='light green', font='Helvetica 13 bold', command=reset_game)
    button_play_game.pack()
    button_play_game.place(x=1100, y=25)

    button_close_window = Button(myMaze._win, text="End Game", height=5, width=25,
                                 bg='red', font='Helvetica 13 bold', command=myMaze._win.destroy)
    button_close_window.pack()
    button_close_window.place(x=1100, y=145)

    myMaze.obstacle_int = StringVar()
    myMaze.obstacle_entry = Entry(myMaze._win, bg='white', textvariable=myMaze.obstacle_int, width=25)
    myMaze.obstacle_entry.pack()
    myMaze.obstacle_entry.place(x=1150, y=340)

    l = Label(myMaze._win, text="Change Number of Enemies Below:", bg='white', font='Helvetica 13 bold')
    l.pack(side='right')
    l.place(x=1085, y=280)

    play_game()
    myMaze._win.mainloop()

if __name__ == '__main__':
    create_and_run_maze()
