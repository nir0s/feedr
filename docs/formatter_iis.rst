===========================
The IIS Formatter
===========================

Allows immitating IIS logs.

Configuration Example
---------------------

.. code-block:: python

 'MyIISFormatter': {
     'type': 'IIS',  # formatter type (MANDATORY)
     'data': {
        'current_date_time': $RAND,
        'ipv4': $RAND,
        'port': $RAND,
        'http_verbs': $RAND,
        'uri_path': $RAND,
        'http_error_codes': $RAND,
        'sc-bytes': $RAND,
        'cs-bytes': $RAND,
        'time-taken': $RAND,
        'user_agent': $RAND,
        'uri': $RAND,
     },
     # By default, all fields above will be randomized.
     # You CAN override them by supplying specific lists of data for a field.
 },

Example Output
--------------

.. code-block:: bash

 2002-05-24 20:18:01 172.224.24.114 - 206.73.118.24 80 GET /Default.htm - 200 7930 248 31 Mozilla/4.0+(compatible;+MSIE+5.01;+Windows+2000+Server) http://64.224.24.114/