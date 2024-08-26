# interface.py
import os
import random
from get_random_line import get_random_line
from colorama import Fore, Style, init

# Initialize colorama
init()

void_dir = os.path.join(os.getcwd(), 'void')
os.makedirs(void_dir, exist_ok=True)

# Look for .txt files in the 'void' subdirectory
txt_files = [f for f in os.listdir(void_dir) if f.endswith('.txt')]

if not txt_files:
    print("No .txt files found in the 'void' subdirectory.")
else:
    while txt_files:
        random_file = random.choice(txt_files)
        file_path = os.path.join(void_dir, random_file)
        void_file_path = os.path.join(void_dir, '0.txt')  # Path for the new file
        while True:  # Infinite loop
            random_file = random.choice(txt_files)
            file_path = os.path.join(void_dir, random_file)
            void_file_path = os.path.join(void_dir, '0.txt')  # Path for the new file
            random_line = get_random_line(file_path)
            if random_line:
                print(Fore.GREEN + random_line + Style.RESET_ALL)
                key_pressed = input("Press Enter to try another line, 's' to stamp, or Ctrl+C to quit: ")
                if key_pressed == 's':
                    with open(void_file_path, 'a', encoding='utf-8') as void_file:
                        void_file.write(random_line + '\n.\n')
                        void_file.flush()
                        os.fsync(void_file.fileno())
                    print(f"Line stamped to '{void_file_path}'.")
            else:
                print("No valid lines found in the current file. Trying another file.")