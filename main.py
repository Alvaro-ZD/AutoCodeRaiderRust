import os
import json
import time
import mouse
from pynput import keyboard

# Double press threshold in seconds
DOUBLE_PRESS_THRESHOLD = 0.5

last_press_time = {"f5": 0, "f6": 0}

def record_positions():
    print("Starting to record positions...")
    print("Please perform 10 clicks in the desired order (from 0 to 9).")
    positions = {}
    for i in range(0, 10):
        print(f"Waiting for click for digit {i}...")
        mouse.wait(button='left')
        pos = mouse.get_position()
        positions[str(i)] = {"x": pos[0], "y": pos[1]}
        print(f"Click for {i}: {pos}")
        time.sleep(0.1)
    with open("positions.json", "w") as f:
        json.dump(positions, f, indent=2)
    print("Positions saved in positions.json")
    return positions

def load_positions():
    if not os.path.exists("positions.json"):
        return record_positions()
    else:
        with open("positions.json", "r") as f:
            positions = json.load(f)
        return positions

def load_codes():
    if not os.path.exists("codes.txt"):
        print("The file codes.txt does not exist.")
        return []
    with open("codes.txt", "r") as f:
        codes = [line.strip() for line in f if line.strip()]
    return codes

def load_last_index():
    if not os.path.exists("last_used.txt"):
        return 0
    with open("last_used.txt", "r") as f:
        try:
            idx = int(f.read().strip())
        except:
            idx = 0
    return idx

def save_last_index(index):
    with open("last_used.txt", "w") as f:
        f.write(str(index))

def process_code(code, positions):
    print(f"Processing code: {code}")
    if len(code) != 4:
        print("Invalid code, it must have exactly 4 digits.")
        return
    for digit in code:
        if digit not in positions:
            print(f"Digit {digit} does not have an assigned position.")
            continue
        pos = positions[digit]
        print(f"Clicking for digit {digit} at position ({pos['x']}, {pos['y']})")
        mouse.move(pos['x'], pos['y'], absolute=True, duration=0.2)
        mouse.click('left')
        time.sleep(0.1)
    print("Sequence completed.\n")

def main():
    global positions, codes, index, last_press_time
    positions = load_positions()
    codes = load_codes()
    if not codes:
        print("No codes found in codes.txt")
        return
    index = load_last_index()
    print("Instructions:")
    print(" - Double press F5: Record positions again.")
    print(" - Double press F6: Reset codes index.")
    print(" - Single press F7: Process the next code.")
    print("Waiting for key presses...")

    def on_press(key):
        global positions, codes, index, last_press_time
        current_time = time.time()
        try:
            if key == keyboard.Key.f5:
                # Double press for re-recording positions
                if current_time - last_press_time["f5"] < DOUBLE_PRESS_THRESHOLD:
                    print("Double press F5: Re-recording positions.")
                    positions = record_positions()
                    last_press_time["f5"] = 0  # Reset timer
                else:
                    last_press_time["f5"] = current_time
            elif key == keyboard.Key.f6:
                # Double press for resetting index
                if current_time - last_press_time["f6"] < DOUBLE_PRESS_THRESHOLD:
                    print("Double press F6: Resetting codes index.")
                    index = 0
                    save_last_index(index)
                    last_press_time["f6"] = 0
                else:
                    last_press_time["f6"] = current_time
            elif key == keyboard.Key.f7:
                # Single press F7 to process the next code
                if index >= len(codes):
                    print("All codes processed. Resetting index.")
                    index = 0
                current_code = codes[index]
                process_code(current_code, positions)
                index += 1
                save_last_index(index)
                print("Waiting for next key press...")
        except Exception as e:
            print("Error in on_press:", e)

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Script terminated by the user.")