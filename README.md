# Artificial Intelligence Dijkstra's Pathfinding - AKE Maze

This project presents a maze game that combines classic gameplay with dynamic elements, introducing variability and challenges in each playthrough. The core
feature of the game revolves around the implementation of **Dijkstra's algorithm**, which ensures that the agent can efficiently explore the maze and find the 
shortest path, overcoming obstacles strategically placed by adapting to the dynamic nature of the game. 

# Methods
In the AKE Maze Game, **Dijkstra's algorithm** is used to find the best way for the player to navigate through the maze and reach the goal state. This algorithm is like a
smart guide that excels at finding the shortest path between two points. Imagine the maze as a big puzzle, and Dijkstra's algorithm is like a helpful tool to figure out the
quickest way from the starting point to the finish. **Dijkstra's algorithm** looks at all the possible paths and cleverly chooses the one
that gets you from where you are to where you want to go in the least amount of steps. During the game, this algorithm is always working in the background, recalculating the
best path as the player moves. It helps the game's character (the agent) move through the maze, avoiding obstacles strategically placed in its way. 

# AKE Maze Game Development
- Developing dynamic maze environment: created methods responsible for opening a wall in a maze represented as a 2D grid
- Including obstacles in the form of “enemies” (same features as the main agent)
- Importing function which randomly positions the obstacles in a maze environment
- Implementing Dijkstra's algorithm to find the optimal path and recalculate it for every gameplay
- Developing GUI application

# Results
AKE Maze Game has a **dynamic front-end environment that integrates intelligent agents, changing obstacles or agent’s enemies, and Dijkstra's algorithm** to find the
optimal path to the goal state. The game's uniqueness lies in its dynamic nature, as the environment pattern is randomly generated for each gameplay session, including an
element of unpredictability and freshness in every encounter. Within this dynamic maze, obstacles in the form of enemies are strategically placed,
adding an extra layer of complexity.

The user interface is designed for an intuitive experience, featuring two optional buttons: "Play Again" and "End Game." Clicking "Play Again" triggers the function to create a new maze
environment, complete with a fresh distribution of enemies and a recalculated path. On the other hand, the "End Game" button provides a seamless exit from the application.

![image](https://github.com/aaleksandraristic/Reinforcement-Learning-in-Path-Finding---AKE-Maze/assets/140200824/ab531fc7-d62a-460a-8373-ee6da75a96dc)

![image](https://github.com/aaleksandraristic/Reinforcement-Learning-in-Path-Finding---AKE-Maze/assets/140200824/fb7a426f-3e0a-4391-85b8-ee7452d74703)


**Important note: Since our game has a dynamic environment and obstacle locations, it
is not always possible to calculate the optimal path for the agent so the code will give us
an error. That doesn’t mean that something is wrong with the code, it’s just the
possibility to find the free path (without going through the walls) to the goal state and
avoid all the obstacles.

