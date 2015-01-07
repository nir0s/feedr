.. cloudify-cli documentation master file, created by
   sphinx-quickstart on Thu Jun 12 15:30:03 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to feedr's documentation!
=================================

feedr (yes, I know, it's a bad name. I'll change it when I come up of something better) can generate custom data and send it away..

It can randomly generate data or get its format and data from a configuration file.

You could use feedr to test your logstash configuration, your elasticsearch cluster performance, load test your RabbitMQ cluster, your InfluxDB handlers.. you get the gist.

feedr even comes with built in Apache Access log (regular and extended) and Apache error log formatters for you to check how you're handling apache logs (and you don't even need apache to do that. how cool is that?)

feedr uses a configuration file in which you can configure your `formatters <http://feedr.readthedocs.org/en/latest/formatters.html>`_ and `transports <http://feedr.readthedocs.org/en/latest/transports.html>`_ to your liking.

Contents:

.. toctree::
   :maxdepth: 2

   quick_start
   configuration
   formatters
   transports
   api
   in_house_faker
   case_study


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

