from typing import Final


class Port:
    HEADERS:Final = ["Protocol", "Port ID", "Service"]

    
    def __init__(self, protocol = "unknown", port_id = "unknown", service = "unknown"):
        self._protocol = protocol
        self._port_id = port_id
        self._service = service
        self._modules = None
    
    def set_protocol(self, val_):
        if val_:
            self._protocol = val_

    def set_port_id(self, val_):
        if val_:
            self._port_id = val_
    
    def set_service(self, val_):
        if val_:
            self._service = val_
    
    def get_protocol(self):
        return self._protocol
    
    def get_port_id(self):
        return self._port_id
    
    def get_service(self):
        return self._service
    
    def is_validated(self):
        valid_protocol = ["tcp", "udp", "unknown"]

        if not self._protocol in valid_protocol:
            return False

        valid_port_id = ["unknown"]

        if not 0 <= int(self._port_id) <= 65535:
            if not self._port_id in valid_port_id:
                return False
        
        return True
    

    def get_row(self):
        return [self._protocol, self._port_id, self._service]