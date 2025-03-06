from Parse_Machine.Parsers.Nmap_Parser import Nmap_Parser as Npsr

class Parse_Machine:

    def __init__(self):
        self._modules = None

    def register(self, modules):
        self._modules = modules
    
    def receive(self, output, process):
        if process == "scan.bat":
            self._modules.receive(Npsr.Nmap_Parser.parse(output))

        # elif process == "check_connection.bat":
        #     self._modules.receive(output) 

        else:    # pass the output straight through
            self._modules.receive(output)