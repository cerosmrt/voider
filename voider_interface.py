import os  # Import the os module for file path operations
import tkinter as tk  # Import tkinter for GUI elements
from tkinter import messagebox  # Import messagebox for displaying messages
import random  # Import random for random line selection
from get_random_line import get_random_line  # Import get_random_line function

class VoiderInterface:
    def __init__(self, root, void_dir):
        self.root = root  # Reference to the root window
        self.void_dir = void_dir  # Directory where void files are stored
        self.void_file_path = os.path.join(void_dir, '0.txt')  # Path to the void file
        
        self.root.title("Voider")  # Set the title of the window
        
        self.label = tk.Label(root, text="Enter Line to Void:")  # Create a label widget
        self.label.pack()  # Add the label to the window
        
        self.entry = tk.Entry(root, width=50)  # Create an entry widget for user input
        self.entry.pack()  # Add the entry widget to the window
        
        self.entry.bind('<Return>', self.void_line)  # Bind the Enter key to the void_line method
        self.entry.bind('<Key>', self.on_key_press)  # Bind any key press to the on_key_press method
        
        self.void_button = tk.Button(root, text="Void Line", command=self.void_line)  # Create a button to void the line
        self.void_button.pack()  # Add the button to the window
        
        self.current_line = None  # Initialize the variable to store the current line of text
        
        self.txt_files = [f for f in os.listdir(void_dir) if f.endswith('.txt')]
        # Create a list of all .txt files in the 'void_dir' directory
        
        if not self.txt_files:
            # Check if there are no .txt files in the directory
            messagebox.showerror("Error", "No .txt files found in the 'void' subdirectory.")
            # Display an error message if no .txt files are found
            root.quit()  # Exit the application

    def on_key_press(self, event):
        # Method to handle key press events
        if event.keysym == 'Down':
            # If the key pressed is the down arrow key, show a random line
            self.show_random_line()

    def show_random_line(self):
        # Method to display a random line from a randomly selected .txt file
        if self.txt_files:
            # Check if there are .txt files available
            while True:
                random_file = random.choice(self.txt_files)
                # Randomly select a .txt file from the list
                file_path = os.path.join(self.void_dir, random_file)
                # Construct the full path to the selected file
                self.current_line = get_random_line(file_path)
                # Use the 'get_random_line' function to get a random line from the file
                if self.current_line:
                    # Check if a valid line was retrieved
                    self.entry.delete(0, tk.END)
                    # Clear any existing text in the entry widget
                    self.entry.insert(tk.END, self.current_line)
                    # Insert the new random line into the entry widget
                    break

    def void_line(self, event=None):
        # Method to append the current line to the '0.txt' file
        line = self.entry.get()  # Get the text from the entry widget
        if line:  # Check if the entry is not empty
            with open(self.void_file_path, 'a', encoding='utf-8') as void_file:
                # Open the void file in append mode with UTF-8 encoding
                void_file.write(line + '\n.\n')
                # Write the line to the file with a newline and period
                void_file.flush()  # Flush the file buffer
                os.fsync(void_file.fileno())  # Ensure the data is written to disk
            self.entry.delete(0, tk.END)  # Clear the entry widget
            self.entry.focus_set()  # Set the focus back to the entry widget
        else:
            messagebox.showwarning("Warning", "No line entered to void.")  # Show a warning message if entry is empty