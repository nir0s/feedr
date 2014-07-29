==================
The File Transport
==================

Allows writing to a file.

.. note:: Currently, only a rotating file transport is supported.

Configuration Example
---------------------

.. code-block:: python

 'MyFileTransport': {
     'type': 'File',  # transport type (MANDATORY)
     'file': 'mylogfile.log',  # the path to the file to write the data to. (OPTIONAL - default is generated.log)
     'max_bytes': 102301202,  # the size of the file afterwhich it is rotated. (OPTIONAL - default is 10000000)
     'backup_count': 5,  # number of files to keep in rotation. (OPTIONAL - default is 20)
 },
