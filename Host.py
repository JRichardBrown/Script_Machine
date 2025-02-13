import Port


class Host:
    def __init__(self):
        self.ports = []
        self.ip_address = None
        self.vendor = None

    def add_port(self, port):
        if port:
            self.ports.append(port)
        else:
            raise Exception("Port object cannot be None.")

    def set_ip_address(self, address):
        if address:
            self.ip_address = address
        else:
            raise Exception("ip_address cannot be None.")
        
    def set_vendor(self, vendor):
        self.vendor = vendor

    def get_ports(self):
        return self.ports
    
    def get_ip_address(self):
        if self.ip_address:
            return self.ip_address
        
        return "unknown"
    
    def get_vendor(self):
        if self.vendor:
            return self.vendor
        
        return "unknown"

    def get_host_table(self):
        ports_table = []

        # create a table of the ports information
        for port in self.ports:
            ports_table.append(port.get_row())

        return {"info": f"IP Address: {self.get_ip_address()}\nVendor: {self.get_vendor()}\n\n",
                      "headers": Port.Port.HEADERS,
                      "ports": ports_table}
