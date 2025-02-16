from enum import Enum


class Modules:
    def __init__(self, gui, script_machine, parser):
        self._gui = gui
        self._script_machine = script_machine
        self._parser = parser
        self._control_flow = []
        self._next_module = None
        self._current_process = ""


    class Module_Id(Enum):
        SCRIPT_MACHINE = 1
        PARSER = 2
        GUI = 3
        PRINTER = 4


    _processes = {
        "scan.bat" : [Module_Id.SCRIPT_MACHINE, Module_Id.PARSER, Module_Id.GUI]
    }


    def _load_process(self, process):
        try:
            self._control_flow = Modules._processes.get(process).copy()    # must be a copy
            self._current_process = process
        except:
            raise Exception("Process not found.")


    def receive(self, input):
        if not self._control_flow:    # list is empty
            try:
                self._load_process(input)
            except:
                raise Exception("receive method failed to load process.")
  
        try:
            self._next_module = self._control_flow.pop(0)
        except: 
            raise Exception("control_flow list is empty")
        
        match self._next_module:
            case Modules.Module_Id.SCRIPT_MACHINE:
                self._script_machine.receive(self._current_process)
            
            case Modules.Module_Id.PARSER:
                self._parser.receive(input, self._current_process)

            case Modules.Module_Id.GUI:
                self._gui.receive(input)      