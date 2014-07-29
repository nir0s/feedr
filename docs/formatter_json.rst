==================
The Json Formatter
==================

Allows configuring a json formatter.

Configuration Example
---------------------

.. code-block:: python

 'MyJsonFormatter': {
     'type': 'Custom',  # formatter type (MANDATORY)
     'data': {
         'date_time': '$RAND',
         'uuid': [str(uuid.uuid1()) for i in xrange(3)],
         'level': ['ERROR', 'DEBUG', 'INFO', 'CRITICAL'],
         'module': ['module1', 'module2'],
         'free_email': '$RAND',
     },
     'jsonify': False,  # should the dict be converted to JSON? (OPTIONAL - defaults to True)
     # there is some default data for testing so this is OPTIONAL.
 },

Example Output
--------------

.. code-block:: bash

 {"free_email": "irvin.corwin@gmail.com", "current_date_time": "2014-07-10 15:45:36", "uuid": "160a7858-0830-11e4-aa19-843a4bd58c5c", "module": "module2", "level": "INFO"}
 {"free_email": "torp.wiley@hotmail.com", "current_date_time": "2014-07-10 15:45:36", "uuid": "160a57d8-0830-11e4-aa19-843a4bd58c5c", "module": "module1", "level": "ERROR"}
 {"free_email": "aflatley@yahoo.com", "current_date_time": "2014-07-10 15:45:36", "uuid": "160a1386-0830-11e4-aa19-843a4bd58c5c", "module": "module1", "level": "CRITICAL"}