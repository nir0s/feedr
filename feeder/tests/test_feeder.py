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

from feeder.feeder import FeederError
import feeder.logger as logger
import feeder.feeder as fd


import testtools
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


class TestBase(testtools.TestCase):

    def test_import_config_file(self):
        outcome = fd._import_config(MOCK_CONFIG_FILE)
        self.assertEquals(type(outcome), dict)
        self.assertIn('transports', outcome.keys())
        self.assertIn('formatters', outcome.keys())

    def test_fail_import_config_file(self):
        ex = self.assertRaises(FeederError, fd._import_config, '')
        self.assertEquals(str(ex), 'missing config file')

    def test_import_bad_config_file(self):
        ex = self.assertRaises(FeederError, fd._import_config, BAD_CONFIG_FILE)
        self.assertEquals(str(ex), 'bad config file')

    def test_get_current_time(self):
        time = str(fd.get_current_time())
        rgx = '\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
        a = re.compile(rgx)
        self.assertTrue(a.match(time) is not None)

    def test_calculate_throughput(self):
        throughput, seconds = fd.calculate_throughput('00:00:10', 100)
        self.assertEquals(throughput, 10)
        self.assertEquals(seconds, 10)

    def test_calculate_throughput_less_than_a_sec(self):
        throughput, seconds = fd.calculate_throughput('00:00:00', 100)
        self.assertEquals(throughput, 'Unknown')
        self.assertEquals(seconds, 0)

    def test_config_transport(self):
        sys.path.append(os.path.dirname(MOCK_TRANSPORT_FILE))
        transports = __import__(os.path.basename(os.path.splitext(
            MOCK_TRANSPORT_FILE)[0]))
        instance, client = fd.config_transport(transports, 'MockTransport', {})
        self.assertIn('send', dir(instance))
        self.assertIn('setLevel', dir(client))

    def test_config_missing_transport(self):
        sys.path.append(os.path.dirname(MOCK_TRANSPORT_FILE))
        transports = __import__(os.path.basename(os.path.splitext(
            MOCK_TRANSPORT_FILE)[0]))
        ex = self.assertRaises(
            FeederError, fd.config_transport, transports,
            'MissingTransport', {})
        self.assertEquals(str(ex), 'missing transport')
        transports = ''
        ex = self.assertRaises(
            FeederError, fd.config_transport, transports, 'MockTransport', {})
        self.assertEquals(str(ex), 'missing transport')

    @log_capture()
    def test_set_global_verbosity_level(self, capture):
        lgr = logger.init(base_level=logging.INFO)

        fd._set_global_verbosity_level(is_verbose_output=False)
        lgr.debug('TEST_LOGGER_OUTPUT')
        capture.check()
        lgr.info('TEST_LOGGER_OUTPUT')
        capture.check(('user', 'INFO', 'TEST_LOGGER_OUTPUT'))

        fd._set_global_verbosity_level(is_verbose_output=True)
        lgr.debug('TEST_LOGGER_OUTPUT')
        capture.check(
            ('user', 'INFO', 'TEST_LOGGER_OUTPUT'),
            ('user', 'DEBUG', 'TEST_LOGGER_OUTPUT'))

    def test_list_fake(self):
        fd.list_fake_types()

    def test_list_transports(self):
        fd.list_transports()

    def test_list_formatters(self):
        fd.list_formatters()


class TestSystem(testtools.TestCase):
    def test_generator_batch_larger_than_messages(self):
        ex = self.assertRaises(FeederError, fd.generator, messages=1, batch=10)
        self.assertIn('batch number', str(ex))

    def test_generator_defaults(self):
        fd.generator(verbose=True, messages=1)

    def test_generator_formatter_json(self):
        fd.generator(formatter='Json', messages=1)

    def test_generator_formatter_apacheaccess(self):
        fd.generator(formatter='ApacheAccess', messages=1)

    def test_generator_formatter_apacheerror(self):
        fd.generator(formatter='ApacheError', messages=1)

    def test_generator_transport_udp(self):
        fd.generator(transport='MyUDPTransport', config=MOCK_CONFIG_FILE,
                     messages=1)

    def test_generator_stream(self):
        fd.generator(transport='Stream', messages=1)

    def test_generator_amqp_connection_fail(self):
        ex = self.assertRaises(RuntimeError, fd.generator,
                               transport='MyAmqpTransport',
                               config=MOCK_CONFIG_FILE,
                               messages=1)
        self.assertEquals(str(ex), 'could not connect to host')

    def test_generator_amqp_no_host(self):
        ex = self.assertRaises(
            RuntimeError, fd.generator, transport='AMQP', messages=1)
        self.assertIn('configuration incomplete', str(ex))

    def test_generator_bad_rand_data(self):
        ex = self.assertRaises(RuntimeError, fd.generator,
                               formatter='MyBadDataFormatter',
                               config=MOCK_CONFIG_FILE,
                               messages=1)
        self.assertIn('cannot randomize data type', str(ex))

# TODO: (TEST) test list transports
# TODO: (TEST) test list formatters
# TODO: (TEST) test missing formatter
# TODO: (TEST) infinite messages config
# TODO: (TEST) test output of all formatters
# TODO: (TEST) test apache extended formatter
