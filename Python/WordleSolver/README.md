# Wordle Solver

This folder contains the code and file for a command line based 'wordle' solver.

# About Wordle

Wordle is a web-based game, popularised in early 2022. It is based around guessing a 5 letter word. 
Each guess made is coloured to show what each letter means.
| Meaning | Wordle |
|---------|--------|
| Correct and In place | Green |
| Correct but not in that position | Yellow |
| Not in the word | Grey |

These results then allow the user to make the next guess in the hopes of guessing the word.

# Using the software

When the software is run, it will ask a selection of options. These are
0: Testing of the algorithm - Shows the current success rate of the algorithm.
1: Using algorithm one on a current game.
2: Using algorithm two on a current game.

To enter a result there will be 3 different letters.
| Letter | Purpose | Wordle Colour |
|--------|---------|---------------|
| G      | Correct and In place | Green |
| Y      | Correct but not in that position | Yellow |
| N      | Not in the word | Grey |

The results are formatted in 5 letter string. Eg. 'gynnn'
