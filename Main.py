from Parse_Machine import Parse_Machine as Ps
from Controller import Controller as Ctrl
import Script_Machine as Sm
import Gui
import tkinter as tk

def main():
    parser = Ps.Parse_Machine()
    gui = Gui.NetworkScannerGUI(tk.Tk())
    script_machine = Sm.Script_Machine()
    
    modules = Ctrl.Controller(gui, script_machine, parser)

    parser.register(modules)
    gui.register(modules)
    script_machine.register(modules)

    gui.root.mainloop()
    

if __name__ == "__main__":
    main()