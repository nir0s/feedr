===========================
The Elasticsearch Transport
===========================

Allows indexing documents in `Elasticsearch <http://www.elasticsearch.org>`_.


Configuration Example
---------------------

.. code-block:: python

 'MyElasticsearchTransport': {
     'type': 'Elasticsearch',  # transport type (MANDATORY)
     'host': 'myelasticsearchcluster.com',  # the host to send to (MANDATORY)
     'port': '9921',  # the port to send to (OPTIONAL - defaults to 9200)
     'url_prefix': 'yo',  # url prefix to append (OPTIONAL - defaults to an empty string)
     'timeout': 1,  # connection timeout (OPTIONAL - defaults to 10)
     'index': 'myindex',  # index to write to (OPTIONAL - defaults to 'logstash-YYYY.MM.dd' to)
     'doc_type': 'mydoctype',  # doc type to write (OPTIONAL - defaults to 'doc')
     'sleep': 3  # sleep time before printing index docs count (OPTIONAL - defaults to 3)
 },

.. note:: The `sleep` parameter is a workaround for the time it takes to index all documents before printing the documents count. It will be removed in the future and a smart mechanism will be implemented.
