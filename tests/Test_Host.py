import Host
import Port
import pytest

@pytest.fixture
def setup():
    host = Host.Host()
    port = Port.Port("tcp", "22", "open", "ssh")
    host.add_port(port)
    host.set_ip_address("192.168.2.1")
    
    yield host

def test_add_port(setup):
    host = setup

    assert len(host.ports) > 0

    assert host.ports[0].get_protocol() == "tcp"
    assert host.ports[0].get_port_id() == "22"

def test_get_host_table(setup):
    host = setup
    table = host.get_host_table()

    assert "192.168.2.1" in table["info"]
    assert "Vendor" in table["info"]

    assert table["headers"][0] == "Protocol"

    assert len(table["headers"]) == 4

    assert len(table["ports"]) > 0

    assert table["ports"][0] == "tcp"
