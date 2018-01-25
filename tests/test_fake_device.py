import unittest

import str116

class TestDevice(unittest.TestCase):
    def setUp(self):
        self.dev = str116.FakeDevice()

    def test_device_type(self):
        assert type(self.dev) is str116.FakeDevice

    def test_get_relay_status(self):
        assert type(self.dev.relay(0)) is bool

    def test_set_relay(self):
        self.dev.relay(0, 1)
        assert self.dev.relay(0)
        self.dev.relay(0, 0)
        assert not self.dev.relay(0)
