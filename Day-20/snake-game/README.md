# Days 20-21: Snake

The Snake game, made with `turtle`. Steer with W, A, S and D, eat the food to grow and score points.

The code is split into files, and each file has a small job:

- `snake.py`: the snake and how it moves
- `food.py`: the food, which jumps to a new spot when it is eaten
- `scoreboard.py`: shows the score and the high score
- `main.py`: the game loop

The high score is saved in `data.txt`, so it is still there the next time you play. If you hit a wall or your own tail, the snake and score start over (the game doesn't end) and a new high score gets saved at that moment.

To run it: `python main.py`
