# Day 31: Flash Cards

A flash card app for learning German words, made with `tkinter` and pandas. It shows a German word for 3 seconds, then flips the card to show the English word.

- The tick button means you know the word. It is removed from the pile and your progress is saved in `data/words_to_learn.csv`, so next time you carry on where you stopped.
- The cross button means you don't know it yet, so the word stays in the pile.

The words come from `data/deutsch_words.csv`, which has about 10,000 German words with English translations. They appear in random order.

The app needs an `images` folder next to `main.py` with four pictures: `card_front.png`, `card_back.png`, `right.png` and `wrong.png`.

To run it: `python main.py`
