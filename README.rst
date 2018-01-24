STR116
======

A driver for the `STR116 relay board <https://goo.gl/TPEKJf>`_.
`The source for this project is available here
<https://github.com/llamicron/str116>`_.

Based on the ``str116.py`` module from `adaptiman/adaptibrew <https://github.com/adaptiman/adaptibrew>`_.

----

More to come...

Usage
=====
.. code-block:: python

  from str116 import Device

  # Just sest some relays
  device = Device()
  device.get_relay(4) # true or false
  device.set_relay(4, 1)

  # Here you can specify the name of a method you want to create, and the relay address associated with it.
  relay_methods = {
    'hlt': 4,
    'pump': 5
  }

  device = Device(methods=relay_methods)

  device.hlt(1)   # sets relay 4 to on, because that's what you mapped it to up there
  device.pump(0)  # sets relay 5 to off

  device.pump()   # No arguments gets you the status ie. true or false
