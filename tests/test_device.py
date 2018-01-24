import unittest

from str116 import Device

class TestDevice(unittest.TestCase):

    def setUp(self):
        self.relay_methods = {
            'hlt': 0,
            'pump': 1
        }

    def test_make_one(self):
        # It'll take relay methods
        assert type(Device(self.relay_methods)) is Device
        # But doesn't need them
        assert type(Device()) is Device

    def test_get_relay_status(self):
        dev = Device()
        status = dev.get_relay(1)
        assert status is True or status is False

    def test_set_relay(self):
        dev = Device()
        dev.set_relay(0, 1)
        assert dev.get_relay(0)
        dev.set_relay(0, 0)
        assert not dev.get_relay(0)
