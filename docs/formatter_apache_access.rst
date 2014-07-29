===========================
The Apache Access Formatter
===========================

Allows immitating Apache Access logs.

Configuration Example
---------------------

.. code-block:: python

 'MyApacheAccessFormatter': {
     'type': 'ApacheAccess',  # formatter type (MANDATORY)
     'data': {
         'ipv4': '$RAND',
         'current_day_of_month': '$RAND',
         'current_month_name_short': '$RAND',
         'current_year': '$RAND',
         'current_time': '$RAND',
         'current_time_zone_number': '$RAND',
         'http_versions': '$RAND',
         'http_verbs': '$RAND',
         'uri_path': '$RAND',
         'http_error_codes': '$RAND',
         'random_int': '$RAND',
     },
     # By default, all fields above will be randomized.
     # You CAN override them by supplying specific lists of data for a field.
 },

Example Output
--------------

.. code-block:: bash

 87.48.231.47 - - [10/Jul/14:15:49:07 +0000] "HEAD /app HTTP/1.1" 501 8959
 216.205.174.8 - - [10/Jul/14:15:49:07 +0000] "POST /main HTTP/1.0" 503 2483
 48.70.200.122 - - [10/Jul/14:15:49:07 +0000] "POST /posts/wp-content/tags HTTP/1.1" 302 322