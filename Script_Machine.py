import os
import socket

class Script_Machine:
    
    def __init__(self):
        self._modules = None
        self.network_address = socket.gethostbyname(socket.gethostname()) + "/24"
    
    def launch_script(self, script_name, *args):
        command = script_name

        for i in range(0, len(args)):
            command = command + ' ' + args[i]

        try:
            os.system(f"{command}")
        except:
            raise Exception("Script Machine failed to launch script.")

    
    def receive(self, process):
        if process == "scan.bat":

            self.launch_script(r"scripts\scan.bat", self.network_address)

            try: 
                self._modules.receive("scanresults.xml")
            except:
                raise Exception("No Modules object loaded.")


    def register(self, modules):
        self._modules = modules