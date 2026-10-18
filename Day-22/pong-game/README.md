# Day 22: Pong

Two player Pong made with `turtle`. The left player uses W and S. The right player uses the Up and Down arrow keys.

The ball bounces off the top and bottom walls and off the paddles. Every time it hits a paddle it gets faster. When someone scores, the ball goes back to the middle and the speed starts over.

The code is split into three classes: `Paddle`, `Ball` and `Scoreboard`. The score is only kept while the game is open, and there is no winning score, so it goes on until you close the window.

To run it: `python main.py`
