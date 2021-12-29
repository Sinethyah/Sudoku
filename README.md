# Sudoku Puzzle Verifier 
A simple interactive terminal Sudoku puzzle verifier in Python that
allows user to input a number in a specific position and checks for the validity of
the input.

This program is developed using Python. 
It can be run on code editors like Visual Studio Code by clicking on the run button.

The Sudoku grid is a 9x9 grid which is divided into 9 3x3 subgrids.

When the program is run:
1. The user is prompted to type the name of the file from which it retrieves the puzzle data from.
2. The name of the file where the puzzle data is retrieved: 'puzzle.csv'
3. The user is prompted to specify the position and the number. 
4. The position and number are placed as comma-separated. For example: 2,3,4 where 2 is the row number, 3 is the column number and 4 is the number the user would like to input.
5. The input is verified as valid or invalid and a message is displayed with the following information: 
    columns that are invalid, rows that are invalid and subgrids that are invalid (if applicable).
6. An existing number can be removed by typing a '0' in the position of a number. For example: 2,3,0
7. To quit: type 'quit'
8. A message is displayed that contains the following information: 
   1. if the puzzle is complete or not.
   2. how many numbers were typed.
   3. how many of those numbers were invalid.

