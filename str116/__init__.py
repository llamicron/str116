import serial
import time
import binascii
import os
import logging
import random

settings = {
    'timeout': 0.05,
    'baudRate': 19200,
    'port': '/dev/ttyAMA0',
    'encoding_type': 'utf8',
    'MA0': '55',
    'MA1': 'AA',
    'MAE': '77',
    'CN': '02',
}

def get_checksum(bytestring):
    checksum = sum(bytearray.fromhex(bytestring))
    checksumstripped = hex(checksum).replace('0x', '')
    return checksumstripped.zfill(2)

def prepare_bytestring():
    s = settings
    bytestring = '0714' + s['CN'] + '0010'
    checksum = get_checksum(bytestring)
    return s['MA0'] + s['MA1'] + bytestring + str(checksum) + s['MAE']

logging.basicConfig(filename='logs/str116.log', level=logging.INFO)

class Device(object):
    def __new__(cls):
        device = Device.hardware()
        if not device:
            return FakeDevice()
        return super(Device, cls).__new__(cls)

    def __init__(self, device, methods=None):
        self.ser = device
        self.ser.timeout = settings['timeout']
        self.bytestring = prepare_bytestring()

    @staticmethod
    def hardware():
        ''' returns a serial device, or raises an IOError '''
        try:
            return serial.Serial(settings['port'], settings['baudRate'])
        except IOError as er:
            logging.error("Failed to connect to STR116 device")
            return False

    def write(self, data):
        data = data.encode(settings['encoding_type'])
        try:
            self.ser.write(data)
        except IOError as err:
            logging.error("Can't write to the STR116 device (%s)" % (err))
            raise
        if self.ser.open:
            time.sleep(0.02)
            size = self.ser.inWaiting()
            if size:
                data = self.ser.read(size)
                return binascii.hexlify(data.encode(settings['encoding_type']))
            return None


class FakeDevice(object):

    def __init__(self):
        # Relay statuses
        # Normally this would be retrieved from the board, but there ain't none lmaooo
        self.relays = [False] * 12

    def relay(self, relay_num, state=None):
        # False with probably be passed to state
        # Can't just say `if not state`
        if state == None:
            return self.relays[int(relay_num)]
        self.relays[int(relay_num)] = bool(state)
