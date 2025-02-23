# Auto Code Raider Rust

This is a Python project that simulates mouse clicks based on recorded positions and a list of 4-digit codes.

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
  The project's current code index is stored in `last_used.txt`, allowing processing continuity between sessions.

## Usage Instructions

1. **Setup:**  
   Make sure you have the required packages installed:
   - `mouse`
   - `pynput`

   You can install them via pip:
   ```
   pip install mouse pynput
   ```

2. **Running the Project:**  
   Execute the script:
   ```
   python main.py
   ```
   Follow the on-screen instructions to record positions and process codes.

## Repository

This project has been initialized as a Git repository under the name **Auto Code Raider Rust**. It is fully version controlled and ready for deployment.

Happy coding!