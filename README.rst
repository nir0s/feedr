pylog
=====

|Build Status|

|Gitter chat|

|PyPI|

|PypI|

pylog generates events/logs using a specified formatter and sends them
using the specified transport. It can also generate fake data using
fake-factory.

Quick Start
~~~~~~~~~~~

`Quick
Start <http://pylog.readthedocs.org/en/latest/quick_start.html>`__

Documentation
~~~~~~~~~~~~~

`pylog Documentation <http://pylog.readthedocs.org>`__

Installation
~~~~~~~~~~~~

.. code:: shell

     pip install pylog
     # or, for dev:
     pip install https://github.com/nir0s/pylog/archive/develop.tar.gz

Usage Examples
~~~~~~~~~~~~~~

see `pylog
config <http://pylog.readthedocs.org/en/latest/configuration.html>`__
and `advanced
config <http://pylog.readthedocs.org/en/latest/advanced_configuration.html>`__
to configure your transports and formatters.

.. code:: shell

     # this will assume config.py in the cwd and assume default for each option
     pylog gen
     # or.. you can specify whatever you want in the cli..
     pylog gen -c /my/config/file/path.py -t AMQP -f Json -g 0.001 -m 100000000
     pylog gen -t UDP -f Custom -g 0.00001 -m 102831028
     # you can also send in batches
     pylog gen -t UDP -f Custom -g 0.01 -m 102831028 -b 1000
     # and even use some common formatters like apache's..
     pylog gen -t Stream -f ApacheError
     # print fake data types that you can use in the config...
     pylog list fake
     # print a list of available transports
     pylog list transports
     # print a list of available formatters
     pylog list formatters

Additional Information
~~~~~~~~~~~~~~~~~~~~~~

-  `Use Case <http://pylog.readthedocs.org/en/latest/case_study.html>`__
-  `Configuration <http://pylog.readthedocs.org/en/latest/configuration.html>`__
-  `formatters <http://pylog.readthedocs.org/en/latest/formatters.html>`__
-  `transports <http://pylog.readthedocs.org/en/latest/transports.html>`__
-  `API <http://pylog.readthedocs.org/en/latest/api.html>`__
-  `InHouseFaker <http://pylog.readthedocs.org/en/latest/inhousefaker.html>`__

Vagrant
~~~~~~~

A vagrantfile is provided: It will load a machine and install pylog on
it in a virtualenv so that you can experiment with it. In the future,
another machine will be provided with rabbitmq, logstash, elasticsearch
and kibana so that you can experiment with different types of formats
and transports.

.. |Build Status| image:: https://travis-ci.org/nir0s/pylog.svg?branch=develop
   :target: https://travis-ci.org/nir0s/pylog
.. |Gitter chat| image:: https://badges.gitter.im/nir0s/pylog.png
   :target: https://gitter.im/nir0s/pylog
.. |PyPI| image:: http://img.shields.io/pypi/dm/pylog.svg
   :target: http://img.shields.io/pypi/dm/pylog.svg
.. |PypI| image:: http://img.shields.io/pypi/v/pylog.svg
   :target: http://img.shields.io/pypi/v/pylog.svg
