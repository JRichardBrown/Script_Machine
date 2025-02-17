import Nmap_Parser as Ps
import pytest

def test_parse():
    parser = Ps.Nmap_Parser()

    assert parser._parse("scanresults.xml") == "?"
