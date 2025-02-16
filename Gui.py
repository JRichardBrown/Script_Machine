import threading
import tkinter as tk
from tkinter import ttk
import Host

class NetworkScannerGUI:
    def __init__(self, root):
        # test change
        """
        Initialize the GUI and create widgets.
        """
        self.root = root
        self.root.title("Script Machine")
        
        # Variables to store scan results
        self.scan_results = {}

        # Create and arrange GUI components
        self.create_widgets()

    def create_widgets(self):
        """
        Create GUI components and arrange them in a grid layout.
        """
        # "Launch" Button - Full functionality
        self.start_scan_button = tk.Button(self.root, text="Launch", command=self.start_scan)
        self.start_scan_button.grid(row=0, column=0, padx=10, pady=10)
        
        # "Clear" Button - Full functionality
        self.clear_button = tk.Button(self.root, text="Clear", command=self.clear_results)
        self.clear_button.grid(row=0, column=1, padx=10, pady=10)
        
        # Dropdown menu for scan type selection - Placeholder
        self.scan_type_label = tk.Label(self.root, text="Script:")
        self.scan_type_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.scan_type_menu = ttk.Combobox(self.root, values=["Port Scan"])
        self.scan_type_menu.grid(row=1, column=1, padx=10, pady=5)
        
        # Scrollable text box for displaying scan results - Full functionality
        self.results_text_box = tk.Text(self.root, width=60, height=15)
        self.results_text_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def start_scan(self):
        """
        Calls the Modules object's `receive()` method with "full scan" as input.
        """
        if self.module_obj:
            threading.Thread(self.module_obj.receive("full scan"))
        else:
            self.results_text_box.insert(tk.END, "Modules object not registered.\n")

    def display_results(self):
        """
        Displays scan results in the scrollable text box.
        """
        for host in self.scan_results:
            self.results_text_box.insert(tk.END, host["info"])
            self.results_text_box.insert(tk.END, "\t\t".join(host["headers"]) + "\n")

            for row in host["ports"]:
                self.results_text_box.insert(tk.END, "\t\t".join(row) + "\n")
            
            self.results_text_box.insert(tk.END, "\n")
            

        self.results_text_box.insert(tk.END, "Scan completed.\n")

    def clear_results(self):
        """
        Clears the results from the text box and resets stored results.
        """
        self.results_text_box.delete(1.0, tk.END)
        self.scan_results = []

    def receive(self, input_data):
        """
        Receives a 2-dimensional array and displays it in the text box.
        """
        self.scan_results = input_data

        self.display_results()

    def register(self, module_obj):
        """
        Registers an object of the class Modules.
        """
        self.module_obj = module_obj
