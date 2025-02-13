import os
import Parser as Ps
import socket
import threading

class Script_Machine:
    def __init__(self):
        self._modules = None
        self.network_address = socket.gethostbyname(socket.gethostname()) + "/24"

    
    def launch_script(self, script_name, *args):
        # command = script_name

        # for i in range(0, len(args)):
        #     command = command + ' ' + args[i]

        try:
            os.system(script_name + ' 192.168.1.1/24')
        except:
            raise Exception("Script Machine failed to launch script.")

    
    def receive(self, process):
        if process == "full scan":

            # thread = threading.Thread(target=lambda : self.launch_script("scan.bat", self.network_address))
            # thread.start()

            self.launch_script("scan.bat", self.network_address)

            print("Launching scan.bat")

            try: 
                self._modules.receive("scanresults.xml")
                # print(self._net_address)
            except:
                raise Exception("No Modules object loaded.")


    def register(self, modules):
        self._modules = modules