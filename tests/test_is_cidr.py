import pytest
from IpconfigObject import IpconfigObject
from snc import is_CIDR
from snc import get_network_address
from snc import get_broadcast_address

class TestIsCIDR:
    def test_is_cidr(self):
        assert is_CIDR("1.0.255.254/32") == True, "Test /32"
        assert is_CIDR("1.0.255.254/33") == False, "Test /33"
        assert is_CIDR("1.0.255.254/a") == False, "Test bogus slashmask"

    def test_get_network_address(self):
        # 1.0.255.32/24 = 00000001 00000000 11111111 00100000 / 24
        # 1.0.255.0 = 0000001 00000000 11111111 00000000
        assert get_network_address("0000000100000000111111110010000", 24) == "00000001000000001111111100000000", "/24 network address fails"

        # 4.2.16.127/26 = 00000100 00000010 00001000 01111111 / 26
        # 4.2.16.64 = 00000100 00000010 00001000 01000000
        assert get_network_address("00000100000000100000100001111111", 26) == "00000100000000100000100001000000", "/26 network address fails"

    def test_get_broadcast_address(self):
        # 4.2.2.1/23 = 00001000 00000010 00000010 00000001 / 23
        # 4.2.3.255 = 00001000 00000010 00000011 11111111
        assert get_broadcast_address("00001000000000100000001000000001", 23) == "00001000000000100000001111111111", "/23 broadcast address fails"