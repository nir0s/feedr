# TODO: (FEAT) support additional apache formats (http://ossec-docs.readthedocs.org/en/latest/log_samples/apache/apache.html)  # NOQA
# TODO: (FEAT) maybe consolidate Json and Custom formatters to the same class, to let other custom formatters use them both for each type implemented  # NOQA
# TODO: (FEAT) implement Tomcat Formatter

import random
from abc import abstractmethod, ABCMeta
from faker import Factory
from format_mappings import InHouseFaker
import json
import uuid


DEFAULT_CUSTOM_FORMAT = [
    'current_date_time', ' ', 'uuid', ' ', 'level', ': ',
    'module', ' - ', 'free_email'
]
DEFAULT_CUSTOM_DATA = {
    'current_date_time': '$RAND',
    'uuid': [str(uuid.uuid1()) for i in xrange(100)],
    'level': ['WARNING', 'ERROR', 'DEBUG', 'INFO', 'CRITICAL'],
    'module': ['module1', 'module2'],
    'free_email': '$RAND',
}
DEFAULT_JSONIFY = True


def fake_data(data_type):
    """returns fake data for the data type requested.

    will try and get fake data from the local format mappings.
    if fake data for the specific data type wasn't found, it will try and use
    fake-factory to fake the data.

    :param string data_type: the type of data to fake.
    :rtype: string
    """
    fake = Factory.create()
    try:
        return getattr(InHouseFaker(), 'default')(data_type)
    except KeyError:
        if hasattr(InHouseFaker, data_type):
            return getattr(InHouseFaker(), data_type)()
        elif hasattr(fake, data_type):
            return str(getattr(fake, data_type)())
        # except AttributeError:
        print('cannot randomize data for {0}. run "feeder list fake" '
              'to print a list of possible types.'.format(data_type))
        raise RuntimeError('cannot randomize data type {0}'.format(
            data_type))


class BaseFormatter(object):
    """base class for all formatters
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, config):
        return

    @abstractmethod
    def generate_data(self):
        return

    def f(self, config, name):
        """retrieves configuration keys

        if config wasn't supplied or a key doesn't exist, returns $RAND
        which will initiate data faking
        """
        return config['data'].get(name, '$RAND') if config else '$RAND'


class CustomFormatter(BaseFormatter):
    """returns a generated log string in a custom format

    this is also a formatter other formatters
    can rely on to generate application specific logs.
    see the ApacheAccessFormatter class for reference.

    for every item in the format list, if an item in the data dict
    corresponds with it and the field's data equals "$RAND", use faker
    to fake an item for it. else, choose one item from the list randomly.
    if there no item in the data to correspond with the format, it will
    just append to format's field name to the log.

    example:

    .. code-block:: python

     'CustomFormatter': {
         'format': ['name', ' - ', 'level'],
         'data': {
             'name': $RAND,
             'level': ['ERROR', 'DEBUG', 'INFO', 'CRITICAL'],
         }
     }

    the output of the above example might be:

    .. code-block:: python

     Sally Fields - ERROR
     or
     Jason Banks - DEBUG
     or
     Danny Milwee - ERROR
     or
     ...
    """
    def __init__(self, config):
        self.format = config.get('format', DEFAULT_CUSTOM_FORMAT)
        self.data = config.get('data', DEFAULT_CUSTOM_DATA)

    def generate_data(self):
        """this will generate a message according to `self.format`
        with data from `self.data`.

        all fields in the data dict will be iterated over and matched to
        the items in the format list. if a match is found and $RAND is set
        in one of the fields, random data will be generated for that field.
        If not, data will be chosen from the list.
        If no match is found, the explicit item in the format list will be
        appended.

        example:

        .. code-block:: python

         format = ['Mr. ' 'first_name', 'last_name']
         data = {
             'first_name': ['Jason, Josh]',
             'last_name': '$RAND'
         }

        the output of the above example might be:

        .. code-block:: python

         'Mr. Jason Williams'
         or
         'Mr. Josh Brolin'
         or
         'Mr. Jason Bananas'
         ...
        """
        log = ''
        # iterate over the format
        for field_name in self.format:
            # for each field in the data dictionary
            for field, data in self.data.items():
                # if the field name exists in the format and the data
                if field_name == field:
                    # and rand is set
                    if data == '$RAND':
                        # fake the data
                        log += fake_data(field_name)
                    else:
                        # else choose randomly from the field
                        log += random.choice(self.data[field_name])
            # if the field doesn't exist in the data, only in the format
            if field_name not in self.data.keys():
                # we'll assume that the field name in the format itself
                # should be appended to the log.
                log += field_name
        return log


class JsonFormatter(BaseFormatter):
    """generates log strings in json format (or leave as dict)

    all fields in the data dict will be iterated over.
    if $RAND is set in one of the fields, random data will be generated
    for that field. If not, data will be chosen from the list.

    example:

    .. code-block:: python

     'JsonFormatter': {
         'data': {
             'date_time': '$RAND',
             'level': ['ERROR', 'DEBUG'],
             'address': '$RAND',
         }
     },

    the output of the above example might be:

    .. code-block:: python

     {"date_time": "2006-11-05 13:31:09", "name": "Miss Nona Breitenberg DVM", "level": "ERROR"}  # NOQA
     or
     {"date_time": "1985-01-20 11:41:16", "name": "Almeda Lindgren", "level": "DEBUG"}  # NOQA
     or
     {"date_time": "1973-05-21 01:06:04", "name": "Jase Heaney", "level": "DEBUG"}  # NOQA
     or
     ...
    """
    def __init__(self, config):
        self.data = config.get('data', DEFAULT_CUSTOM_DATA)
        self.jsonify = config.get('jsonify', DEFAULT_JSONIFY)

    def generate_data(self):
        # TODO: (FEAT) support randomizing data fields in Json formatter
        log = {}
        for field, data in self.data.items():
            if data == '$RAND':
                log[field] = fake_data(field)
            else:
                log[field] = random.choice(data)
        if self.jsonify:
            return json.dumps(log)
        return log


class ApacheAccessFormatter(CustomFormatter):
    """returns an apache-access-log like string

    you can easily construct new formatters by inheriting the custom formatter.

    all you have to do is specify the format and the data. a helper
    method `f` is supplied in the `BaseFormatter` Class that will allow you to
    retrieve basic formatter configuration for your fields.

    """
    # 192.168.72.177 - - [22/Dec/2002:23:32:19 -0400] "GET /search.php HTTP/1.1" 400 1997 www.yahoo.com "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ...)" "-"  # NOQA
    # %{IPORHOST:clientip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] "(?:%{WORD:verb} %{NOTSPACE:request}(?: HTTP/%{NUMBER:httpversion})?|%{DATA:rawrequest})" %{NUMBER:response} (?:%{NUMBER:bytes}|-)  # NOQA
    def __init__(self, config):
        self.format = [
            'ipv4', ' - - [', 'current_day_of_month', '/',
            'current_month_name_short', '/',
            'current_year', ':', 'current_time', ' ',
            'current_time_zone_number', '] "', 'http_verbs',
            ' /', 'uri_path', ' ', 'http_versions', '" ',
            'http_error_codes', ' ', 'random_int'
        ]
        self.data = {
            'ipv4': self.f(config, 'ipv4'),
            'current_day_of_month': self.f(config, 'current_day_of_month'),
            'current_month_name_short': self.f(config, 'current_month_name_short'),  # NOQA
            'current_year': self.f(config, 'current_year'),
            'current_time': self.f(config, 'current_time'),
            'current_time_zone_number': self.f(config, 'current_time_zone_number'),  # NOQA
            'http_versions': self.f(config, 'http_versions'),
            'http_verbs': self.f(config, 'http_verbs'),
            'uri_path': self.f(config, 'uri_path'),
            'http_error_codes': self.f(config, 'http_error_codes'),
            'random_int': self.f(config, 'random_int'),
        }


class ApacheAccessExFormatter(CustomFormatter):
    """returns an apache-extended-access-log like string"""
    # http://httpd.apache.org/docs/2.2/logs.html
    # 127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326  # NOQA
    # 192.168.2.20 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395  # NOQA
    # %{IPORHOST:clientip} %{USER:ident} %{USER:auth} \[%{HTTPDATE:timestamp}\] "(?:%{WORD:verb} %{NOTSPACE:request}(?: HTTP/%{NUMBER:httpversion})?|%{DATA:rawrequest})" %{NUMBER:response} (?:%{NUMBER:bytes}|-)  # NOQA
    def __init__(self, config):
        self.format = [
            'ipv4', ' - - [', 'current_day_of_month', '/',
            'current_month_name_short', '/',
            'current_year', ':', 'current_time', ' ',
            'current_time_zone_number', '] "', 'http_verbs',
            ' /', 'uri_path', ' ', 'http_versions', '" ',
            'http_error_codes', ' ', 'random_int', ' "',
            'uri', '" "', 'user_agent', '"'
        ]
        self.data = {
            'ipv4': self.f(config, 'ipv4'),
            'current_day_of_month': self.f(config, 'current_day_of_month'),
            'current_month_name_short': self.f(config, 'current_month_name_short'),  # NOQA
            'current_year': self.f(config, 'current_year'),
            'current_time': self.f(config, 'current_time'),
            'current_time_zone_number': self.f(config, 'current_time_zone_number'),  # NOQA
            'http_versions': self.f(config, 'http_versions'),
            'http_verbs': self.f(config, 'http_verbs'),
            'uri_path': self.f(config, 'uri_path'),
            'http_error_codes': self.f(config, 'http_error_codes'),
            'random_int': self.f(config, 'random_int'),
            'uri': self.f(config, 'uri'),
            'user_agent': self.f(config, 'user_agent'),
        }


class ApacheErrorFormatter(CustomFormatter):
    """returns an apache-error-log like string"""
    # [Fri Dec 16 01:46:23 2005] [error] [client 1.2.3.4] Directory index forbidden by rule: /home/test/  # NOQA
    # [Mon Dec 19 23:02:01 2005] [error] [client 1.2.3.4] user test: authentication failure for "/~dcid/test1": Password Mismatch  # NOQA
    def __init__(self, config):
        self.format = [
            '[', 'current_day_of_week_short', ' ', 'current_month_name_short',
            ' ',
            'current_day_of_month', ' ', 'current_time', ' ', 'current_year',
            '] [',
            'syslog_error_levels_lower', '] [client ', 'ipv4', '] ',
            'catch_phrase'
        ]
        self.data = {
            'current_day_of_week_short': self.f(config, 'current_day_of_week_short'),  # NOQA
            'ipv4': self.f(config, 'ipv4'),
            'current_day_of_month': self.f(config, 'current_day_of_month'),
            'current_month_name_short': self.f(config, 'current_month_name_short'),  # NOQA
            'current_year': self.f(config, 'current_year'),
            'current_time': self.f(config, 'current_time'),
            'catch_phrase': self.f(config, 'catch_phrase'),
            'syslog_error_levels_lower': self.f(config, 'syslog_error_levels_lower'),  # NOQA
        }
