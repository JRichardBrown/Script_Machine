# Jeffrey Brown
# CMSC 495-6380
# Parser - Phase A
# January 27, 2025

# Latest Update: 01/27/2025


import xml.etree.ElementTree as ET
from Parse_Machine.Nmap_Parser import Port as Port
import os
from Parse_Machine.Nmap_Parser import Host as Hst


# Parses an .xml file created by NMap and creats a list of Port objects
class Nmap_Parser:
    @classmethod
    def parse(cls, file_name):
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
                    port = Port.Port(node2.get("protocol"), node2.get("portid"))
                    
                    if node2.find("service") is not None:
                        port.set_service(node2.find("service").get("name"))

                    host.add_port(port)

                hosts.append(host.get_host_table())
                
            try:
                os.remove(file_name)
            except:
                raise Exception("Parser failed to remove file " + file_name + ". Please remove file manually.")

            return hosts

        except:
            raise Exception("Parse function failed to load file.")