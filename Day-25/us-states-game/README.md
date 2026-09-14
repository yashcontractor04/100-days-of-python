# U.S. States Educational Map Game
An interactive geographical quiz built with Python's `turtle` and `pandas` libraries. Players identify U.S. states on an interactive map image, with automatic coordinate rendering and export of unlearned states to a study CSV.

### Tech / Concepts
* Tabular data parsing, filtering, and serialization with `pandas`
* Coordinate mapping onto a custom GUI background canvas (`turtle.Screen.addshape`)
* List comprehension for array difference calculation
* Dynamic text placement using scalar series extraction (`.item()`)

### Quickstart
1. Install dependencies:
   `pip install pandas`
2. Run the game:
   `python main.py`
3. Type `Exit` at any prompt to generate `states_to_learn.csv`.
