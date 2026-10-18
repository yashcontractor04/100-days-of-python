# Day 9: Blind Auction

Each person types in their name and a bid. At the end, the program shows who bid the most.

The bids are stored in a dictionary (a list of name and bid pairs) and `max()` finds the highest one.

Two things to know:

- The screen is only cleared at the end, so the next person can still see earlier bids.
- If two people use the same name, the second bid replaces the first.

To run it: `python main.py`
