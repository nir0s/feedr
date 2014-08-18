========
Use Case
========

To show off the strength feeder possesses, let's take an example that has nothing to do with logs.

You're now leading a monitoring project where you need to build your first Graphite cluster.

You decided you wanna transport your metrics via AMQP so you have your RabbitMQ cluster installed and Graphite is ready to pull metrics.
It's important that you feed multiple metrics with multiple values and multiple namespaces to test the integrity of your cluster's configuration and performance.

But oh no! How will I test my cluster?
Well.. you could install StatsD or Diamond on all of your instances and configure them to send metrics.. and then find out that your configuration is incorrect and iterate over it 11 times.. or...

*scratches head*... oh wait. I know! I'll use feeder's AMQP transport!

Ok... so the config would look something like this:

.. code-block:: python

 'transports': {
     'TestRabbitCluster': {
         'type': 'AMQP',
         'host': '54.120.11.12',  # your RabbitMQ's host IP Address (or load balancer.. assuming you have multiple nodes)
         'queue': 'test_queue',
         'exchange': 'test_exchange',
         'routing_key': 'test_routing_key',
     },
 }

Great. So you have your transport configured and now you wanna start sending some metrics.
So you need to configure a formatter.

You want to send metrics from 2 availability zones, 3 types of middleware servers, each having 3 base metric types, each with average and max measurements.

So you'd do something like that...

.. code-block:: python

 'MyMetricsFormatter': {
     'type': 'Custom',
     'format': ['zone', '.', 'application', '.', 'metric', '.', 'measurement', ' ', 'value'],
     'data': {
         'zone': ['zone1', 'zone2'],
         'application': ['webserver', 'database', 'registration_server'],
         'metric': ['cpu_percentage', 'memory_percentage', 'hdd_free_percentage'],
         'measurement': ['avg', 'max'],
         'value': [i for i in xrange(100)],
     }
 },

.. note:: This configuration is only logical for a hypothetical case (paradox, aye?). You might want to define multiple formatters with multiple types of metrics. For instance, the values here (1-100) are only relevant to specific types of metrics (in our case, %).

Then, all you have to do is run:

.. code-block:: bash

 mouth feed -t TestRabbitCluster -f MyMetricsFormatter -c my_config_file.py -g 0.001 -m 100000000

The (partial) output, might look like this (if you printed it to a file):

.. code-block:: text

 zone1.database.hdd_free_percentage.max 55
 zone1.registration_server.hdd_free_percentage.avg 91
 zone2.database.hdd_free_percentage.avg 40
 zone1.database.cpu_percentage.avg 93
 zone1.webserver.memory_percentage.max 14
 zone1.database.hdd_free_percentage.max 93
 zone2.database.cpu_percentage.avg 10
 zone1.database.memory_percentage.avg 6
 zone2.database.cpu_percentage.max 4
 zone2.database.memory_percentage.max 79
 zone2.registration_server.memory_percentage.avg 49
 zone2.webserver.cpu_percentage.avg 53
 zone1.database.memory_percentage.max 68
 zone2.registration_server.hdd_free_percentage.max 68
 zone2.webserver.cpu_percentage.max 66
 zone2.database.cpu_percentage.max 98
 zone1.database.memory_percentage.max 61
 zone2.database.cpu_percentage.max 24
 zone1.webserver.memory_percentage.max 24
 zone1.registration_server.cpu_percentage.avg 43
 zone2.database.hdd_free_percentage.avg 23
 zone2.registration_server.cpu_percentage.max 48
 zone2.database.memory_percentage.max 78
 zone1.registration_server.memory_percentage.avg 76
 zone2.database.memory_percentage.avg 83
 zone1.database.cpu_percentage.max 39
 zone2.webserver.cpu_percentage.avg 23
 zone2.database.memory_percentage.avg 41
 zone2.webserver.memory_percentage.max 29
 zone2.registration_server.memory_percentage.max 33
 zone1.webserver.cpu_percentage.max 25
 zone1.database.cpu_percentage.avg 11
 zone2.webserver.cpu_percentage.avg 3
 zone2.registration_server.cpu_percentage.max 24
 zone2.database.cpu_percentage.max 22
 zone2.database.hdd_free_percentage.avg 50
 zone2.webserver.memory_percentage.max 42
 zone2.webserver.hdd_free_percentage.avg 2
 zone2.webserver.memory_percentage.max 83
 zone2.registration_server.memory_percentage.max 59
 zone2.webserver.hdd_free_percentage.avg 35
 zone2.registration_server.hdd_free_percentage.avg 43
 zone2.registration_server.cpu_percentage.avg 90
 zone2.registration_server.cpu_percentage.max 45
 zone1.database.cpu_percentage.max 34
 zone1.database.hdd_free_percentage.max 90


Now, you would be able to, for instance, use Vagrant to load a cluster of feeder instances in AWS that would bombard your cluster with metrics.. and then, POOF! Just "vagrant destroy" the machines when you're done.

Of course... I would say that you should periodically run these tests (even randomly) to check that your cluster can withstand surges of metrics.. but.. i'm not your production manager. You can daemonize the process and omit  the -m flag so that messages are sent constantly.