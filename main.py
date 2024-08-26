import tkinter as tk
import os
from voider_interface import VoiderInterface
from void_interface import VoidInterface

if __name__ == "__main__":
    root = tk.Tk()
    
    void_dir = 'void'  # Define the directory where the void files are stored
    os.makedirs(void_dir, exist_ok=True)
    
    # Create a new window for the Voider Interface
    voider_window = tk.Toplevel(root)
    voider_app = VoiderInterface(voider_window, void_dir)
    
    # Create a new window for the Void Interface
    void_window = tk.Toplevel(root)
    void_app = VoidInterface(void_window, void_dir)
    
    root.mainloop()