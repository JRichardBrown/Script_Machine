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
            scan_output = os.popen(f"{command}").read().split('\n', 2)    # ignore the first 2 lines
            return scan_output[2]
        except:
            raise Exception("Script Machine failed to launch script.")

    
    def receive(self, process):
        if process == "scan.bat":

            try: 
                self._modules.receive(self.launch_script(r"Script_Machine\scripts\scan.bat", self.network_address))
            except:
                raise Exception("No Modules object loaded.")


    def register(self, modules):
        self._modules = modules