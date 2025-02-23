# Auto Code Raider Rust

Auto Code Raider Rust is a project designed to automate the process of entering codes in a game to perform a code raid. The list of codes is organized based on the most common codes used in the game, and the tool keeps track of your progress through the list. You simply need to press F7 to test all possible combinations, while the system automatically handles the code entry and saves your progress.

## Project Overview

The project functions as follows:

- **Recording Positions:**  
  When the project starts, it checks for the file `positions.json` which stores the coordinates for digits 0 to 9. If the file does not exist, or if re-recording is requested, the script prompts the user to perform 10 mouse clicks corresponding to the digits 0 through 9.

- **Processing Codes:**  
  The project reads a list of 4-digit codes from `codes.txt`. Each digit in a code maps to the recorded positions. When processing a code, the script simulates mouse clicks at the corresponding positions:
  - If a digit does not have an assigned position, an error message is displayed.
  - The script expects each code to have exactly 4 digits.

- **Key Bindings:**  
  - **Double press F5:** Re-record positions.
  - **Double press F6:** Reset the codes index.
  - **Single press F7:** Process the next code in the list.

- **Persistence:**  
  The project's current code index is stored in `last_used.txt`, ensuring that progress through the list is saved between sessions.

## Usage Instructions

1. **Setup:**  
   Ensure the required packages are installed:
   ```
   pip install mouse pynput
   ```

2. **Running the Project:**  
   Run the script:
   ```
   python main.py
   ```
   Follow the on-screen instructions to record positions and process codes.

## Project Purpose

The objective of this project is to automate the repetitive process of code input during a code raid in a game. By doing so, it simplifies testing multiple code combinations while keeping track of progress.

Happy coding!