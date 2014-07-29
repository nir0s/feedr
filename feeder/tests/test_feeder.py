########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

__author__ = 'nir0s'

from feeder.feeder import _import_config
from feeder.feeder import FeederError
from feeder.feeder import get_current_time
from feeder.feeder import calculate_throughput
from feeder.feeder import config_transport
from feeder.feeder import init_logger
from feeder.feeder import _set_global_verbosity_level
from feeder.feeder import list_fake_types
from feeder.feeder import list_transports, list_formatters
from feeder.feeder import generator

import unittest
import os
import sys
from testfixtures import log_capture
import logging
import re


TEST_DIR = '{0}/test_dir'.format(os.path.expanduser("~"))
TEST_FILE_NAME = 'test_file'
TEST_FILE = TEST_DIR + '/' + TEST_FILE_NAME
TEST_RESOURCES_DIR = 'feeder/tests/resources'
MOCK_CONFIG_FILE = os.path.join(TEST_RESOURCES_DIR, 'mock_config.py')
MOCK_TRANSPORT_FILE = os.path.join(TEST_RESOURCES_DIR, 'mock_transport.py')
BAD_CONFIG_FILE = os.path.join(TEST_RESOURCES_DIR, 'bad_config.py')


class TestBase(unittest.TestCase):

    def test_import_config_file(self):
        outcome = _import_config(MOCK_CONFIG_FILE)
        self.assertEquals(type(outcome), dict)
        self.assertIn('transports', outcome.keys())
        self.assertIn('formatters', outcome.keys())

    def test_fail_import_config_file(self):
        try:
            _import_config('')
        except FeederError as ex:
            self.assertEquals(str(ex), 'missing config file')

    def test_import_bad_config_file(self):
        try:
            _import_config(BAD_CONFIG_FILE)
        except FeederError as ex:
            self.assertEquals(str(ex), 'bad config file')

    def test_get_current_time(self):
        time = str(get_current_time())
        rgx = '\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
        a = re.compile(rgx)
        self.assertTrue(a.match(time) is not None)

    def test_calculate_throughput(self):
        throughput, seconds = calculate_throughput('00:00:10', 100)
        self.assertEquals(throughput, 10)
        self.assertEquals(seconds, 10)

    def test_calculate_throughput_less_than_a_sec(self):
        throughput, seconds = calculate_throughput('00:00:00', 100)
        self.assertEquals(throughput, 'Unknown')
        self.assertEquals(seconds, 0)

    def test_config_transport(self):
        sys.path.append(os.path.dirname(MOCK_TRANSPORT_FILE))
        transports = __import__(os.path.basename(os.path.splitext(
            MOCK_TRANSPORT_FILE)[0]))
        instance, client = config_transport(transports, 'MockTransport', {})
        self.assertIn('send', dir(instance))
        self.assertIn('setLevel', dir(client))

    def test_config_missing_transport(self):
        sys.path.append(os.path.dirname(MOCK_TRANSPORT_FILE))
        transports = __import__(os.path.basename(os.path.splitext(
            MOCK_TRANSPORT_FILE)[0]))
        try:
            config_transport(transports, 'MissingTransport', {})
        except FeederError as ex:
            self.assertEquals(str(ex), 'missing transport')
        transports = ''
        try:
            config_transport(transports, 'MockTransport', {})
        except FeederError as ex:
            self.assertEquals(str(ex), 'missing transport')

    @log_capture()
    def test_set_global_verbosity_level(self, capture):
        lgr = init_logger(base_level=logging.INFO)

        _set_global_verbosity_level(is_verbose_output=False)
        lgr.debug('TEST_LOGGER_OUTPUT')
        capture.check()
        lgr.info('TEST_LOGGER_OUTPUT')
        capture.check(('user', 'INFO', 'TEST_LOGGER_OUTPUT'))

        _set_global_verbosity_level(is_verbose_output=True)
        lgr.debug('TEST_LOGGER_OUTPUT')
        capture.check(
            ('user', 'INFO', 'TEST_LOGGER_OUTPUT'),
            ('user', 'DEBUG', 'TEST_LOGGER_OUTPUT'))

    def test_list_fake(self):
        list_fake_types()

    def test_list_transports(self):
        list_transports()

    def test_list_formatters(self):
        list_formatters()


class TestSystem(unittest.TestCase):
    def test_generator_batch_larger_than_messages(self):
        try:
            generator(messages=1, batch=10)
        except FeederError as ex:
            self.assertIn('batch number', str(ex))

    def test_generator_defaults(self):
        generator(verbose=True)
        # with open('generated.log', 'r') as f:
        #     self.assertEquals(f.read(), os.getcwd())

    def test_generator_formatter_json(self):
        generator(formatter='Json')

    def test_generator_formatter_apacheaccess(self):
        generator(formatter='ApacheAccess')

    def test_generator_formatter_apacheerror(self):
        generator(formatter='ApacheError')

    def test_generator_transport_udp(self):
        generator(transport='MyUDPTransport', config=MOCK_CONFIG_FILE)

    def test_generator_stream(self):
        generator(transport='Stream')

    def test_generator_amqp_connection_fail(self):
        try:
            generator(transport='MyAmqpTransport', config=MOCK_CONFIG_FILE)
        except RuntimeError as ex:
            self.assertEquals(str(ex), 'could not connect to host')

    def test_generator_amqp_no_host(self):
        try:
            generator(transport='AMQP')
        except RuntimeError as ex:
            self.assertIn('configuration incomplete', str(ex))

    def test_generator_bad_rand_data(self):
        try:
            generator(formatter='MyBadDataFormatter', config=MOCK_CONFIG_FILE)
        except RuntimeError as ex:
            self.assertIn('cannot randomize data type', str(ex))

# TODO: (TEST) test list transports
# TODO: (TEST) test list formatters
