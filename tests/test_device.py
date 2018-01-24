import unittest

from str116 import Device

class TestDevice(unittest.TestCase):

    def setUp(self):
        self.relay_methods = {
            'hlt': 0,
            'pump': 1
        }

    def test_paramaters(self):
        # It'll take relay methods
        assert type(Device(methods=self.relay_methods)) is Device
        # But doesn't need them
        assert type(Device()) is Device
