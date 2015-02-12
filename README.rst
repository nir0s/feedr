feedr
=====

|Build Status|

|Gitter chat|

|PyPI|

|PypI|

|Documentation Status|

feedr generates events/logs using a specified formatter and sends them
using the specified transport. It can also generate fake data using
fake-factory.

Quick Start
~~~~~~~~~~~

`Quick
Start <http://feedr.readthedocs.org/en/latest/quick_start.html>`__

Documentation
~~~~~~~~~~~~~

`feedr Documentation <http://feedr.readthedocs.org>`__

Installation
~~~~~~~~~~~~

.. code:: shell

     pip install feedr
     # or, for dev:
     pip install https://github.com/nir0s/feedr/archive/master.tar.gz

Usage Examples
~~~~~~~~~~~~~~

see `feedr
config <http://feedr.readthedocs.org/en/latest/configuration.html>`__
and `advanced
config <http://feedr.readthedocs.org/en/latest/advanced_configuration.html>`__
to configure your transports and formatters.

.. code:: shell

     # this will assume config.py in the cwd and assume default for each option
     mouth feed
     # or.. you can specify whatever you want in the cli..
     mouth feed -c /my/config/file/path.py -t AMQP -f Json -g 0.001 -m 100000000
     mouth feed -t UDP -f Custom -g 0.00001 -m 102831028
     # you can also send in batches
     mouth feed -t UDP -f Custom -g 0.01 -m 102831028 -b 1000
     # and even use some common formatters like apache's..
     mouth feed -t Stream -f ApacheError
     # print fake data types that you can use in the config...
     mouth list fake
     # print a list of available transports
     mouth list transports
     # print a list of available formatters
     mouth list formatters

Additional Information
~~~~~~~~~~~~~~~~~~~~~~

-  `Use Case <http://feedr.readthedocs.org/en/latest/case_study.html>`__
-  `Configuration <http://feedr.readthedocs.org/en/latest/configuration.html>`__
-  `formatters <http://feedr.readthedocs.org/en/latest/formatters.html>`__
-  `transports <http://feedr.readthedocs.org/en/latest/transports.html>`__
-  `API <http://feedr.readthedocs.org/en/latest/api.html>`__
-  `InHouseFaker <http://feedr.readthedocs.org/en/latest/in_house_faker.html>`__

Vagrant
~~~~~~~

A vagrantfile is provided: It will load a machine and install feedr on
it in a virtualenv so that you can experiment with it. For a machine
containing feedr, ELK and RabbitMQ see the `elk-workshop
repo <https://github.com/nir0s/elk-workshop>`__.

.. |Build Status| image:: https://travis-ci.org/nir0s/feedr.svg?branch=master
   :target: https://travis-ci.org/nir0s/feedr
.. |Gitter chat| image:: https://badges.gitter.im/nir0s/feedr.png
   :target: https://gitter.im/nir0s/feedr
.. |PyPI| image:: http://img.shields.io/pypi/dm/feedr.svg
   :target: http://img.shields.io/pypi/dm/feedr.svg
.. |PypI| image:: http://img.shields.io/pypi/v/feedr.svg
   :target: http://img.shields.io/pypi/v/feedr.svg
.. |Documentation Status| image:: https://readthedocs.org/projects/feedr/badge/?version=latest
   :target: https://readthedocs.org/projects/feedr/?badge=latest
