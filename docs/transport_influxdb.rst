===========================
The InfluxDB Transport
===========================

Allows indexing metrics in `InfluxDB <http://http://influxdb.com/>`_.


Configuration Example
---------------------

.. code-block:: python

 'MyInfluxDBTransport': {
     'type': 'InfluxDB',  # transport type (MANDATORY)
     'host': '10.2.2.7',  # the host to send to (MANDATORY)
     'user': 'root',  # the influx database user
     'password': 'root',  # the influx database password
     'database': 'metrics'  # the database to send to
 }


You can define a `Json` formatter to send metrics to influx

.. code-block:: python

 'MyInfluxDBFormatter': {
     'type': 'Json',
     'data': {
         'points': [[[1.1,4.3,2.1],[1.2,2.0,2.0]]],
         'name': ["web_devweb01_load"],
         'columns': [["min1", "min5", "min15"]]
     },
     'jsonify': False,
 },

.. note:: Make sure jsonify is False. Additionally, note that you cannot currently send a list of of timeseries simultaneously. What you CAN do, use randomize different timeseries by providing multiple values in the `name` field.