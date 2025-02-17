from enum import Enum


class Processes:
    SCRIPT_MACHINE = 1
    PARSE_MACHINE = 2
    GUI = 3
    PRINTER = 4

    _processes = {
        "scan.bat" : [SCRIPT_MACHINE, PARSE_MACHINE, GUI]
    }

    @classmethod
    def get_process(cls, process):
        return cls._processes[process]