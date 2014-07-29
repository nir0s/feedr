==================
The AMQP Transport
==================

Allows sending messages via the amqp protocol using pika.

Configuration Example
---------------------

.. code-block:: python

 'MyAMQPTransport': {
     'type': 'AMQP',  # transport type (MANDATORY)
     'host': 'localhost',  # host to send to (MANDATORY)
     'queue': 'nice_queue',  # queue to write to (OPTIONAL - default is myqueue)
     'exchange': 'nice_exchange',  # exchange to use (OPTIONAL - default is not to use one)
     'routing_key': 'nice_key',  # routing key to use (OPTIONAL - default is myroutingkey)
 },