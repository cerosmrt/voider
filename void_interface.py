import os  # Imports the 'os' module for interacting with the operating system, like file paths and directory listings
import random  # Imports the 'random' module for generating random numbers or making random choices
import tkinter as tk  # Imports the 'tkinter' module for creating graphical user interfaces
from tkinter import messagebox  # Imports the 'messagebox' class from 'tkinter' for showing pop-up messages
from get_random_line import get_random_line  # Imports the 'get_random_line_from_directory' function from the 'random_line_stamper' module

class VoidInterface:
    def __init__(self, root, void_dir):
        # Initializes the VoidInterface class with the main window 'root' and the directory 'void_dir'
        self.root = root  # Stores the main window object
        self.void_dir = void_dir  # Stores the directory containing text files
        self.void_file_path = os.path.join(void_dir, '0.txt')
        # Creates the path for the file where stamped lines will be saved
        self.save_button = tk.Button(root, text="Save", command=self.save_file)
        self.save_button.pack()
        
        self.root.title("Void")  # Sets the title of the main window

        # Make the window centered and pagesize, not fullscreen. like docs or word 
        self.root.attributes('-fullscreen', False)
        self.root.geometry("800x600") # Sets the initial size of the window
        self.root.update_idletasks() # Updates the window to get the actual size
        
        # Center the window on the screen
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height //2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        self.label = tk.Label(root, text="Random Line:")
        # Creates a label widget with the text "Random Line:"
        self.label.pack()  # Adds the label to the window
        
        self.text = tk.Text(root)
        # Creates a text widget with specified dimensions
        self.text.pack()  # Adds the text widget to the window
        
        self.summon_button = tk.Button(root, text="Summon Line", command=self.summon_random_line)
        self.summon_button.pack()  # Adds the button to the window
        
        self.inscribe_button = tk.Button(root, text="Inscribe Line", command=self.inscribe_line)
        self.inscribe_button.pack()  # Updates the button to use the new method
        
        self.current_line = None  # Initializes the variable to store the current line of text
        
        self.txt_files = [f for f in os.listdir(void_dir) if f.endswith('.txt')]
        # Creates a list of all .txt files in the 'void_dir' directory
        
        if not self.txt_files:
            # Checks if there are no .txt files in the directory
            messagebox.showerror("Error", "No .txt files found in the 'void' subdirectory.")
            # Displays an error message if no .txt files are found
            root.quit()  # Exits the application
        
        self.load_file()  # Load the initial content of '0.txt' into the text widget
        
    def summon_random_line(self):
    # Check if there are any text files available
        if self.txt_files:  
            while True:
                # Randomly select a file from the list of text files
                random_file = random.choice(self.txt_files)
                file_path = os.path.join(self.void_dir, random_file)
                # Fetch a random line from the selected file
                self.current_line = get_random_line(file_path)
                
                if self.current_line:
                    # Check if there is any currently selected text
                    if self.text.tag_ranges(tk.SEL):
                        # If there is selected text, replace it with the new line
                        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
                    else:
                        # If no text is selected, delete the text in the current line
                        self.text.delete("insert linestart", "insert lineend")
                    
                    # Insert the new line at the current cursor position
                    self.text.insert(tk.INSERT, self.current_line + '\n')
                    
                    # Calculate the start position of the new line for selection
                    start_pos = self.text.index("insert linestart")
                    # Calculate the end position of the new line for selection
                    end_pos = self.text.index("insert + %dc" % (len(self.current_line) + 1))  # +1 for the newline
                    
                    # Add a selection tag from start_pos to end_pos
                    self.text.tag_add(tk.SEL, start_pos, end_pos)
                    # Move the cursor to the end of the newly inserted line
                    self.text.mark_set(tk.INSERT, end_pos)
                    # Scroll the text widget to the cursor position
                    self.text.see(tk.INSERT)
                    # Set focus on the text widget to ensure the user sees the selected text
                    self.text.focus_set()
                    break


    
    def inscribe_line(self):
        if self.current_line:
            with open(self.void_file_path, 'a', encoding='utf-8') as void_file:
                void_file.write(self.current_line + '\n.\n')
                void_file.flush()
                os.fsync(void_file.fileno())
            self.update_text_widget()  # Updates the text widget with the inscribed line
                
    def load_file(self):
        # Defines a method to load and display the content of '0.txt'
        if os.path.exists(self.void_file_path):
            # Checks if the '0.txt' file exists
            with open(self.void_file_path, 'r', encoding='utf-8') as void_file:
                # Opens the '0.txt' file in read mode with UTF-8 encoding
                content = void_file.read()
                # Reads the content of the file
                self.text.delete(1.0, tk.END)
                # Clears any existing text in the text widget
                self.text.insert(tk.END, content)
                # Inserts the content of the file into the text widget
            self.update_text_widget() # Update format of '0.txt'

        else:
            messagebox.showerror("Error", f"File '{self.void_file_path}' not found.")
            # Displays an error message if the file is not found
    
    def update_text_widget(self):
        # Defines a method to update the text widget with the content of '0.txt'
        print("Updating text widget...")  # Debug message
        if os.path.exists(self.void_file_path):
            # Checks if the '0.txt' file exists
            with open(self.void_file_path, 'r', encoding='utf-8') as void_file:
                # Opens the '0.txt' file in read mode with UTF-8 encoding
                content = void_file.read()
                print(f"File content: {content}")  # Debug message
                # Reads the content of the file
                self.text.delete(1.0, tk.END)
                # Clears any existing text in the text widget
                
                # Get the width of the Text widget
                widget_width = int(self.text.cget("width"))
                
                # Split the content by dots and join with newlines
                lines = content.split('.')
                formatted_content = '\n. \n'.join(line.strip() for line in lines if line.strip())
                
                # Center the entire content
                centered_content = '\n'.join(line.center(widget_width) for line in formatted_content.split('\n'))
                
                # Insert the centered content into the text widget
                self.text.insert(tk.END, centered_content)
        else:
            messagebox.showerror("Error", f"File '{self.void_file_path}' not found.")
            # Displays an error message if the file is not found
    
    def save_file(self):
        # Defines a method to save the content of the text widget to '0.txt'
        content = self.text.get(1.0, tk.END).strip()
        with open(self.void_file_path, 'w', encoding='utf-8') as void_file:
            void_file.write(content)