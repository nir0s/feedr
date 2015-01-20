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
     'queue': 'nice_queue',  # queue to write to (OPTIONAL - default is an empty string)
     'exchange': 'nice_exchange',  # exchange to use (OPTIONAL - default is not to use one)
     'routing_key': 'nice_key',  # routing key to use (OPTIONAL - default is the queue name)
     'exchange_type': 'topic',  # exchange type to use (OPTIONAL - defaults to fanout)
     'delivery_mode': 2,  # pika delivery mode (OPTIONAL - defaults to 2)
     'durable': True,  # whether the queue should be durable and survive server restarts (OPTIONAL - defaults to True)
     'auto_delete': True,  # should the queue auto delete itself once there are no messages in it (OPTIONAL - defaults to True)
     'exclusive': False,  # should messages be exclusive to the client who published them (OPTIONAL - defaults to False)
 },