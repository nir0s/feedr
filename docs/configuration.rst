=============
Configuration
=============

feedr's config is a python file with a single dictionary called GENERATOR.
(It's a python file (rathern than JSON) to allow you to use code when generating the data or configuring the transports.)

In the configuration file, you can configure your `formatters <http://feedr.readthedocs.org/en/latest/formatters.html>`_ and `transports <http://feedr.readthedocs.org/en/latest/transports.html>`_.

feedr will, by default, look for a config.py file in your current working directory unless the "-c" flag is used which will let you specify a specific path. If no config file is found, default configuration will be used.

.. code-block:: python

 GENERATOR = {
     'formatters': {
         'MyJsonFormatter': {
             'type': 'Json',
             'data': {
                 'date_time': ['15-04-2014 10:00:00'],
                 'level': ['ERROR', 'DEBUG'],
                 'name': ['myname', 'notmyname'],
             }
         },
         'MyCustomFormatter': {
             'type': 'Custom',
             'format': ['date_time', ' ', 'level', ': ', 'module', ' - ', 'free_email'],
             'data': {
                 'date_time': ['15-04-2014 10:00:00'],
                 'level': ['ERROR', 'DEBUG', 'INFO', 'CRITICAL'],
                 'module': ['module1', 'module2'],
                 'free_email': ['mymail@gmail.com'],
             }
         },
     },
     'transports': {
         'MyAmqpTransport': {
             'type': 'Amqp',
             'host': 'localhost',
             'queue': 'myqueue',
             'exchange': '',
             'routing_key': 'myroutingkey',
         },
         'MyFileTransport': {
             'type': 'File',
             'file': 'generated.log',
             'max_bytes': 100000000,
             'backup_count': 20,
         },
         'MyUDPTransport': {
             'type': 'UDP',
             'host': 'localhost',
             'port': 999,
         }
     },
 }

Advanced Config
---------------

Since the config is really just a python file, you can pretty much do anything with it.
For instance, you could randomize a uuid field as shown below.

Additionaly, you can use the special $RAND string to randomize data.

.. note:: The $RAND string can only be used for fields that are supported by feedr. You can run "feedr list fake" to see which fields can be randomized.

.. note:: Remember that the entire data dict is kept in memory, so don't randomize millions of data objects or they will hog your resources.

.. code-block:: python

 import uuid

 'formatters': {
     'MyCustomFormatter': {
         'format': ['date_time', ' ', 'uuid', ' ', 'level', ': ', 'module', ' - ', 'free_email'],
         'data': {
             'date_time': '$RAND',
             'uuid': [str(uuid.uuid1()) for i in xrange(100)],
             'level': ['ERROR', 'DEBUG', 'INFO', 'CRITICAL'],
             'module': ['module1', 'module2'],
             'free_email': '$RAND',
         }
     },
 },

.. tip:: to generate real unix time fields, use the current_date_time field. this can help you immitate real time event generation.

.. tip:: check `this <https://github.com/nir0s/feedr/blob/develop/feedr/tests/resources/mock_config.py>`_ out for a configuration file example.