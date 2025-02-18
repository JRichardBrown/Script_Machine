from Parse_Machine.Nmap_Parser import Nmap_Parser as Npsr

class Parse_Machine:

    def __init__(self):
        self._modules = None

    def register(self, modules):
        self._modules = modules
    
    def receive(self, scan_output, process):
        if process == "scan.bat":
            self._modules.receive(Npsr.Nmap_Parser.parse(scan_output))