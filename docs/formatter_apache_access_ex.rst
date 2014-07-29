====================================
The Apache Access Extended Formatter
====================================

Allows immitating Apache Access Extended logs.
This is an exact replica of the Apache Access formatter with 2 added fields.

Configuration Example
---------------------

.. code-block:: python

 'MyApacheAccessExFormatter': {
     'type': 'ApacheAccessEx',  # formatter type (MANDATORY)
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
         'uri': '$RAND',
         'user_agent': '$RAND',
     },
     # By default, all fields above will be randomized.
     # You CAN override them by supplying specific lists of data for a field.
 },

Example Output
--------------

.. code-block:: bash

 98.156.136.253 - - [29/Jul/14:08:16:35 +0000] "PUT /category/explore HTTP/1.1" 200 6212 "http://www.schuppe.biz/author.jsp" "Opera/9.21.(X11; Linux i686; it-IT) Presto/2.9.181 Version/10.00"
 21.192.37.113 - - [29/Jul/14:08:16:35 +0000] "OPTIONS /app/search HTTP/1.0" 400 6961 "http://walker.com/tags/search/posts/search.jsp" "Mozilla/5.0 (Windows NT 5.0) AppleWebKit/5360 (KHTML, like Gecko) Chrome/13.0.886.0 Safari/5360"
 143.223.90.90 - - [29/Jul/14:08:16:35 +0000] "POST /search/app/app HTTP/1.0" 404 2031 "http://www.johnson.net/" "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; Trident/3.0)"