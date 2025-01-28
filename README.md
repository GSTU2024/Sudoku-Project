Sudoku GUI Solver : This is a Sudoku solver with a graphical user interface (GUI) built using Pygame. The program allows users to interact with a Sudoku board, input values, and solve the puzzle using a backtracking algorithm.
Prerequisites
Ensure you have Python installed on your system. You also need Pygame, which you can install using:
pip install pygame
Running the Program
1.	Clone or download this repository.
2.	Open a terminal or command prompt in the project directory.
3.	Run the following command:
python GUI.py
How to Play
•	Click on a cell to select it.
•	Use number keys (1-9) to enter values.
•	Press DELETE to remove a number.
•	Press ENTER to confirm an entry.
•	Press SPACE to auto-solve the puzzle.
•	Close the window to exit the game.

********************* For participants **************************
Instruction for unit testing
Implementing Pytest for Time-Driven Development (TDD)
1. Setup pytest pip install pytest pytest-benchmark
2. Define Key Testing Metrics
  A. Bug count
  B. Development time
  C. Code robustness
3. Create a Test File (test_sudoku.py) : You can create your own test_sudoku.py file with using AI tools or use Repo file.
4. Run the Tests : pytest --benchmark-autosave --tb=short
5. Track Bug Count and Time in CI/CD : If you use GitHub Actions or Jenkins, automate the tracking process:
6. Reporting Bug Count & Development Time :  pytest-benchmark compare
  Example output :
Test Name           | Min Time | Max Time | Std Dev | Iterations
---------------------------------------------------------------
test_solve_performance  | 0.452s  | 0.480s  | 0.015s  | 10  
