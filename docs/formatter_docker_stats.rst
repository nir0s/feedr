==========================
The Docker Stats Formatter
==========================

Allows Generating Docker Stats for a specific container.

.. note:: Stats are enabled only for Docker API v1.17 and above!

Configuration Example
---------------------

.. code-block:: python

 'MyDockerStatsFormatter': {
     'container': 'elasticsearch'  # the container to read stats from
     'client_config': {  # The Docker API client config.
        'version': '1.17',
        ...
     }
 },

.. note:: The Docker API client config can be found `here <http://docker-py.readthedocs.org/en/latest/api/#client-api>`_.

Example Output
--------------

.. code-block:: bash

 {"read":"2015-02-12T18:57:15.567808366+02:00","network":{"rx_bytes":1038195,"rx_packets":7050,"rx_errors":0,"rx_dropped":0,"tx_by tes":1176,"tx_packets":13,"tx_errors":0,"tx_dropped":0},"cpu_stats":{"cpu_usage":{"total_usage":265217625353,"percpu_usage":[8814 0506837,41897336235,88440908322,46738873959],"usage_in_kernelmode":64780000000,"usage_in_usermode":99160000000},"system_cpu_usage ":346652980000000,"throttling_data":{"periods":0,"throttled_periods":0,"throttled_time":0}},"memory_stats":{"usage":87769088,"max _usage":258166784,"stats":{"active_anon":43143168,"active_file":2564096,"cache":3723264,"hierarchical_memory_limit":1844674407370 9551615,"inactive_anon":40988672,"inactive_file":1159168,"mapped_file":2945024,"pgfault":141225,"pgmajfault":3455,"pgpgin":146589 ,"pgpgout":130271,"rss":84045824,"rss_huge":10485760,"total_active_anon":43143168,"total_active_file":2564096,"total_cache":37232 64,"total_inactive_anon":40988672,"total_inactive_file":1159168,"total_mapped_file":2945024,"total_pgfault":141225,"total_pgmajfa ult":3455,"total_pgpgin":146589,"total_pgpgout":130271,"total_rss":84045824,"total_rss_huge":10485760,"total_unevictable":0,"tota l_writeback":0,"unevictable":0,"writeback":0},"failcnt":0,"limit":8039038976},"blkio_stats":{"io_service_bytes_recursive":[{"majo r":8,"minor":0,"op":"Read","value":141418496},{"major":8,"minor":0,"op":"Write","value":4096},{"major":8,"minor":0,"op":"Sync","v alue":4096},{"major":8,"minor":0,"op":"Async","value":141418496},{"major":8,"minor":0,"op":"Total","value":141422592}],"io_servic ed_recursive":[{"major":8,"minor":0,"op":"Read","value":26770},{"major":8,"minor":0,"op":"Write","value":1},{"major":8,"minor":0, "op":"Sync","value":1},{"major":8,"minor":0,"op":"Async","value":26770},{"major":8,"minor":0,"op":"Total","value":26771}],"io_que ue_recursive":[],"io_service_time_recursive":[],"io_wait_time_recursive":[],"io_merged_recursive":[],"io_time_recursive":[],"sect ors_recursive":[]}}
