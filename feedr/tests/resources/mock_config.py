# flake8: NOQA
# IMPORTANT: run "feedr list fake" to see the list of fake data types that can be generated.

import uuid

GENERATOR = {
    'formatters': {
        'MyCustomTestFormatter': {
            'type': 'Custom',
            'format': ['module'],
            'data': {
                'module': ['TESTDATA'],
            },
        },
        'MyJsonFormatter': {
            'type': 'Json',
            'data': {
                'date_time': '$RAND',
                'uuid': [str(uuid.uuid1()) for i in xrange(3)],
                'level': ['ERROR', 'DEBUG'],
                'name': '$RAND',
            },
        },
        'MyMongoFormatter': {
            'type': 'Json',
            'data': {
                'date_time': '$RAND',
                'uuid': [str(uuid.uuid1()) for i in xrange(3)],
                'level': ['ERROR', 'DEBUG'],
                'name': '$RAND',
            },
            'jsonify': False,
        },
        'MyInfluxDBFormatter': {
            'type': 'Json',
            'data': {
                'points': [[[1.1,4.3,2.1],[1.2,2.0,2.0]]],
                'name': ["web_devweb01_load"],
                'columns': [["min1", "min5", "min15"]]
            },
            'jsonify': False,
        },
        'MyCustomFormatter': {
            'type': 'Custom',
            'format': ['date_time', ' ', 'uuid', ' ', 'level', ': ', 'module', ' - ', 'free_email'],
            'data': {
                'date_time': '$RAND',
                'uuid': [str(uuid.uuid1()) for i in xrange(3)],
                'level': ['ERROR', 'DEBUG', 'INFO', 'CRITICAL'],
                'module': ['module1', 'module2'],
                'free_email': '$RAND',
            }
        },
        'MyApacheErrorFormatter': {
            'type': 'ApacheError',
            'data': {
                'ipv4': ['0.0.0.0']
            }
        },
        'MyMetricsFormatter': {
            'type': 'Custom',
            'format': ['zone', '.', 'application', '.', 'metric', '.', 'measurement', ' ', 'value'],
            'data': {
                'zone': ['zone1', 'zone2'],
                'application': ['webserver', 'database', 'registration_server'],
                'metric': ['cpu_percentage', 'memory_percentage', 'hdd_free_percentage'],
                'measurement': ['avg', 'max'],
                'value': [str(i) for i in xrange(100)],
            },
        },
        'MyBadDataFormatter': {
            'type': 'Json',
            'data': {
                'NON_EXISTENT_DATA_FOR_RAND': '$RAND'
            }
        },
    },
    'transports': {
        'MyAmqpTransport': {
            'type': 'AMQP',
            'host': '10.10.10.10',
            'queue': 'myqueue',
            'exchange': '',
            'routing_key': 'myroutingkey',
        },
        'MyFileTransport': {
            'type': 'File',
            'file': 'generated.log',
            'max_bytes': 100000000,
            'backup_count': 20,
        },
        'MyUDPTransport': {
            'type': 'UDP',
            'host': 'localhost',
            'port': 999,
        },
        "MyElasticsearchTransport": {
            'type': 'Elasticsearch',
            'host': '10.0.1.2',
        },
        'MyLogentriesTransport': {
            'type': 'Logentries',
            'token': '94f0e5d3-ad52-4d49-b4f1-feb956cc81b9',
        },
        "MyLogglyTransport": {
            'type': 'Loggly',
            'domain': 'logs-01.loggly.com',
            'token': '68660f49-ad27-4521-9dad-0d9d54924ebd',
        },
        'MyMongoDBTransport': {
            'type': 'MongoDB',
            'host': '10.0.1.2',
        },
        'MyInfluxDBTransport': {
            'type': 'InfluxDB',
            'host': '10.2.2.7',
            'user': 'root',
            'password': 'root',
            'database': 'metrics'
        }
    },
}
