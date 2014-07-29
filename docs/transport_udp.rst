=================
The UDP Transport
=================

Allows sending messages via udp.

Configuration Example
---------------------

.. code-block:: python

 'MyUDPTransport': {
     'type': 'UDP',  # transport type (MANDATORY)
     'host': 'www.google.com',  # the host to send to (MANDATORY)
     'port': '9921',  # the port to send to (MANDATORY)
 },
