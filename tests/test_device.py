import unittest

import str116

class TestDevice(unittest.TestCase):

    def setUp(self):
        self.dev = str116.Device()
        self.relay_methods = {
            'hlt': 0,
            'pump': 1
        }

    def test_make_one(self):
        # It'll take relay methods
        assert type(str116.Device(self.relay_methods)) is str116.Device
        # But doesn't need them
        assert type(str116.Device()) is str116.Device

    def test_write(self):
        assert self.dev.write('data')

    def test_checksum(self):
        bytestring = '0714020010'
        checksum = '2d'
        assert str116.get_checksum(bytestring) == checksum

    def test_prepare_bytestring(self):
        bytestring = '55AA07140200102d77'
        print(str116.prepare_bytestring())
        assert str116.prepare_bytestring() == bytestring
