===========================
The Apache Error Formatter
===========================

Allows immitating Apache Error logs.

Configuration Example
---------------------

.. code-block:: python

 'MyApacheAccessFormatter': {
     'type': 'ApacheAccess',  # formatter type (MANDATORY)
     'data': {
         'current_day_of_week_short': '$RAND',
         'ipv4': '$RAND',
         'current_day_of_month': '$RAND',
         'current_month_name_short': '$RAND',
         'current_year': '$RAND',
         'current_time': '$RAND',
         'catch_phrase': '$RAND',
         'syslog_error_levels_lower': '$RAND',
    },
     # By default, all fields above will be randomized.
     # You CAN override them by supplying specific lists of data for a field.
 },

Example Output
--------------

.. code-block:: bash

 [Thu Jul 10 15:52:39 14] [error] [client 32.23.226.214] Implemented user-facing support
 [Thu Jul 10 15:52:39 14] [error] [client 73.130.255.174] Integrated bi-directional structure
 [Thu Jul 10 15:52:39 14] [critical] [client 120.20.243.249] Secured intangible time-frame