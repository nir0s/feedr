====================
The Loggly Transport
====================

Allows sending messages to `Loggly <http://loggly.com>`_.

.. note:: You can get your token by logging in to Loggly and going to http://#USERNAME#.loggly.com/tokens.

 Alternatively, from the home screen, go to "Source Setup" and then to "Customer Tokens".


Configuration Example
---------------------

.. code-block:: python

 'MyLogglyTransport': {
     'type': 'Loggly',  # transport type (MANDATORY)
     'domain': 'logs.loggly.com',  # (OPTIONAL - defaults to logs-01.loggly.com)
     'token': '68660f49-ad27-4521-9dad-0d9d54924111',  # (MANDATORY)
 },
