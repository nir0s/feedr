==========
Formatters
==========

Formatters create a data structure and applies data into it.

Formatters are classes that contain the logic of how to format your data.
They receive data and a format based on your configuration or fake data for you.

Developing new formatters is as easy as as baking a pop-tart. All you have to do is implement a new class and provide your format and data structures. You can check the Apache Access Log implementation as a reference.

To list all formatters run:

.. code-block:: bash

 mouth list formatters


Contents:

.. toctree::
   :maxdepth: 2

   formatter_custom
   formatter_json
   formatter_apache_access
   formatter_apache_access_ex
   formatter_apache_error

.. automodule:: feedr.formatters
   :members:
   :undoc-members:
   :show-inheritance:
