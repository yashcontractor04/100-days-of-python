# Classic Snake Game with Persistent High Scores
A desktop implementation of Snake featuring modular OOP architecture, Turtle inheritance, manual screen buffer synchronization (`tracer`/`update`), and disk-based file persistence for high score tracking.

### Tech / Concepts
* Class inheritance (`Turtle` base class in `Food` and `Scoreboard`)
* Screen buffer management (`screen.tracer(0)` and `screen.update()`)
* Kinematic segment propagation for body trailing logic
* File I/O (`with open()`) for high score persistence
* 2D spatial distance & bounding-box collision detection

### Quickstart
`python main.py`
