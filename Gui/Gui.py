import os
import threading
import tkinter as tk
from tkinter import ttk
from Gui.Printers import Nmap_Printer as Nmptr

class NetworkScannerGUI:
    def __init__(self, root):
        # test change
        """
        Initialize the GUI and create widgets.
        """
        self.root = root
        self.root.title("Script Machine")
        self.root.config(height=600, width=500)

        # Create and arrange GUI components
        self.create_widgets()

    def create_widgets(self):
        """
        Create GUI components
        """
        self.frame = ttk.Frame(self.root, height=600, width=500)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        control_frame = ttk.Frame(self.frame, height=100, width=500, padding=10)
        
        # "Launch" Button - Full functionality
        self.launch_button = tk.Button(control_frame, text="        Launch        ", command=self.launch)
        # self.start_scan_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.launch_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Dropdown menu for script selection
        self.file_list = [fname for fname in os.listdir(r"scripts")]
        self.script_menu = ttk.Combobox(control_frame, values=self.file_list)
        self.script_menu.current(0)
        self.script_menu.grid(row=0, column=1, padx=10, pady=10)
        
        # "Clear" Button - Full functionality
        self.clear_button = tk.Button(control_frame, text="        Clear        ", command=self.clear_results)
        #self.clear_button.pack(side=tk.RIGHT, padx=10, pady=10)
        self.clear_button.grid(row=0, column=2, padx=10, pady=10)
        
        control_frame.pack(side=tk.TOP, anchor=tk.N)
        
        # Scrollable text box for displaying scan results - Full functionality
        self.results_text_box = tk.Text(self.frame, width=60, height=30, wrap="word")
        self.results_text_box.config(font=("Aptos", 12))
        self.results_text_box.pack(expand=True, fill="both")
        
        # Text tags
        self.results_text_box.tag_config("Header1", font=("Aptos", 16, "bold"))
        self.results_text_box.tag_config("Header2", font=("Aptos", 14, "bold"))
        self.results_text_box.tag_config("Column_Headers", font=("Aptos", 12, "bold"), underline=True)
        

    def launch(self):
        """
        Calls the Modules object's `receive()` method with "full scan" as input.
        """
        if self.module_obj:
            threading.Thread(self.module_obj.receive(self.file_list[self.script_menu.current()]))
        else:
            self.results_text_box.insert(tk.END, "Modules object not registered.\n")



    def clear_results(self):
        """
        Clears the results from the text box and resets stored results.
        """
        self.results_text_box.delete(1.0, tk.END)

    def receive(self, input, process):

        # Prints the results of the parsed script
        if process == "scan.bat":
           Nmptr.NMap_Printer.display(input, self.results_text_box)

    def register(self, module_obj):
        """
        Registers an object of the class Modules.
        """
        self.module_obj = module_obj
