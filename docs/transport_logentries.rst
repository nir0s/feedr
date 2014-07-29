========================
The Logentries Transport
========================

Allows sending messages to `logentries <http://loentries.com>`_.

.. note:: Follow `this <https://github.com/logentries/le_python>`_ (configure section) to get your token.

Configuration Example
---------------------

.. code-block:: python

 'MyLogentriesTransport': {
     'type': 'Logentries',  # transport type (MANDATORY)
     'token': '94f0e5d3-ad52-4d49-b4f1-feb956cc1111' (MANDATORY)
 },
