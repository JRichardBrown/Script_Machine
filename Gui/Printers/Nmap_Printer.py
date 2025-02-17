import tkinter as tk
from tkinter import ttk


class NMap_Printer:
    @classmethod
    def display(cls, scan_results, text_box):
        """
        Displays scan results in the scrollable text box.
        """
        text_box.insert(tk.END, "Scan Results\n\n", "Header1")
        
        for host in scan_results:
            text_box.insert(tk.END, host["info"])
            text_box.insert(tk.END, "\t\t".join(host["headers"]) + "\n", "Column_Headers")

            for row in host["ports"]:
                text_box.insert(tk.END, "\t\t".join(row) + "\n")
            
            text_box.insert(tk.END, "\n")