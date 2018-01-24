import random

class Device(object):
    def __init__(self, methods=None):
        pass

    def get_relay(self, relay_num):
        # Get the actual status
        return random.choice([True, False])

    def set_relay(self, relay_num, state):
        pass
