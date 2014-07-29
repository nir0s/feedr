====================
The Custom Formatter
====================

Allows configuring a custom formatter... which will pretty much do whatever you want. YES, YOU CAN BE A GOD!

Configuration Example
---------------------

.. code-block:: python

 'MyCustomFormatter': {
     'type': 'Custom',  # formatter type (MANDATORY)
     'format': ['date_time', ' ', 'uuid', ' ', 'level', ': ', 'module', ' - ', 'free_email'],
     # format is an ordered list of fields that will be used to create your message string.
     # there is a default format.. so this is OPTIONAL.
     'data': {
         'date_time': '$RAND',
         'uuid': [str(uuid.uuid1()) for i in xrange(3)],
         'level': ['ERROR', 'DEBUG', 'INFO', 'CRITICAL'],
         'module': ['module1', 'module2'],
         'free_email': '$RAND',
     }
     # the data corresponds to the format by the name of the key.
     # again, there is default data for testing, so this is OPTIONAL.
 },

Example Output
--------------

.. code-block:: bash

 2014-07-10 15:44:31 ef00aa3e-082f-11e4-8e1a-843a4bd58c5c INFO: module2 - fay.wilkie@hotmail.com
 2014-07-10 15:44:31 ef01261c-082f-11e4-8e1a-843a4bd58c5c INFO: module1 - feil.alfreda@hotmail.com
 2014-07-10 15:44:31 ef008e5a-082f-11e4-8e1a-843a4bd58c5c ERROR: module1 - clark02@gmail.com
