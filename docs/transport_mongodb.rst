=====================
The MongoDB Transport
=====================

Allows indexing documents in `MongoDB <http://www.mongodb.org/>`_.


Configuration Example
---------------------

.. code-block:: python

 'MyMongoDBTransport': {
     'type': 'MongoDB',  # transport type (MANDATORY)
     'host': 'mymongocluster.com',  # the host to send to (MANDATORY)
     'port': '27100',  # the port to send to (OPTIONAL - defaults to 9200)
     'db': 'mytestdb',  # db to write to (OPTIONAL - defaults to 'test')
     'collection': 'mytestcollection',  # collection to write to (OPTIONAL - defaults to 'my_collection')
     'sleep': 3  # sleep time before printing index docs count (OPTIONAL - defaults to 3)
 },

 .. note:: The `sleep` parameter is a workaround for the time it takes to index all documents before printing the documents count. It will be removed in the future and a smart mechanism will be implemented.