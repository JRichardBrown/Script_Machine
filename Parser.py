# Jeffrey Brown
# CMSC 495-6380
# Parser - Phase A
# January 27, 2025

# Latest Update: 01/27/2025


import xml.etree.ElementTree as ET
import Port as Prt
import os
import Host as Hst


# Parses an .xml file created by NMap and creats a list of Port objects
class Parser:
    def __init__(self):
        self._modules = None

    def _parse(self, file_name):
        try:
            tree = ET.parse(file_name)

            host_tree = tree.findall("host")

            hosts = []

            for node1 in host_tree:
                host = Hst.Host()
                addresses = node1.findall("address")

                host.set_ip_address(addresses[0].get("addr"))

                if len(addresses) > 1:    # if vendor info exists
                    host.set_vendor(addresses[1].get("vendor"))

                port_tree = node1.find("ports").findall("port")

                for node2 in port_tree:
                    port = Prt.Port(node2.get("protocol"), node2.get("portid"))

                    host.add_port(port)

                hosts.append(host.get_host_table())

            return hosts

        except:
            raise Exception("Parse function failed to load file.")
        
        # try:
        #     os.remove(file_name)
        # except:
        #     raise Exception("Parser failed to remove file " + file_name + ". Please remove file manually.")
    
    
    def _is_validated(self):
        pass
    

    def register(self, modules):
        self._modules = modules
    

    def receive(self, file_name, process):
        hosts = self._parse(file_name)

        self._modules.receive(hosts)