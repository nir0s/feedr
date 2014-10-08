# TODO: (FEAT) support for different statistical distributions
# TODO: (FEAT) support throughput testing thru http://linux.die.net/man/1/pv
# TODO: (IMPRV) remove six and dictconfig from coverage report


import logging
import logger
import os
import sys
from time import sleep
import datetime
import random

# import transports and formatters
import transports as trans
import formatters as forms

# import fakers
from faker import Factory
import format_mappings as fm


DEFAULT_BASE_LOGGING_LEVEL = logging.INFO
DEFAULT_VERBOSE_LOGGING_LEVEL = logging.DEBUG

DEFAULT_CONFIG_FILE = 'config.py'
DEFAULT_GAP = float(0.01)
DEFAULT_NUMBER_OF_MESSAGES = 10

DEFAULT_TRANSPORT = 'File'
DEFAULT_FORMATTER = 'Custom'

lgr = logger.init()


def _set_global_verbosity_level(is_verbose_output=False):
    """sets the global verbosity level for console and the lgr logger.

    :param bool is_verbose_output: should be output be verbose
    """
    global verbose_output
    # TODO: (IMPRV) only raise exceptions in verbose mode
    verbose_output = is_verbose_output
    if verbose_output:
        lgr.setLevel(logging.DEBUG)
    else:
        lgr.setLevel(logging.INFO)
    # print 'level is: ' + str(lgr.getEffectiveLevel())


def _import_config(config_file):
    """returns a Feeder configuration object

    :param string config_file: path to config file
    """
    # get config file path
    config_file = config_file or os.path.join(os.getcwd(), DEFAULT_CONFIG_FILE)
    lgr.debug('config file is: {0}'.format(config_file))
    # append to path for importing
    sys.path.append(os.path.dirname(config_file))
    try:
        lgr.debug('importing generator dict...')
        return __import__(os.path.basename(os.path.splitext(
            config_file)[0])).GENERATOR
    # TODO: (IMPRV) remove from path after importing
    except ImportError:
        lgr.warning('config file not found: {0}.'.format(config_file))
        raise FeederError('missing config file')
    except SyntaxError:
        lgr.error('config file syntax is malformatted. please fix '
                  'any syntax errors you might have and try again.')
        raise FeederError('bad config file')


def get_current_time():
    """returns the current time (no microseconds tho)"""
    return datetime.datetime.now().replace(microsecond=0)


def calculate_throughput(elapsed_time, messages):
    """calculates throughput and extracts the number of seconds for the
    run from the elapsed time

    :param elapsed_time: run time
    :param int messages: number of messages to write
    :return: throughput and seconds
    :rtype: tuple
    """
    ftr = [3600, 60, 1]
    seconds = sum([a * b for a, b in zip(
        ftr, [int(i) for i in str(elapsed_time).split(":")])])
    try:
        return messages / seconds, seconds
    except ZeroDivisionError:
        lgr.warning('caluclating throughput for less-than-a-second '
                    'runs is currently not supported. come back soon..')
        return 'Unknown', seconds


def send(instance, client, formatter, format_config, messages, gap, batch):
    """sends logs and prints the time it took to send all logs

    :param instance: transport class instance
    :param client: client to use to send logs
    :param string format: formatter to use
    :param dict format_config: formatter configuration to use
    :param int messages: number of messages to send
    :param float gap: gap in seconds between 2 messages
    :param int batch: number of messages per batch
    """
    message_count = 0
    lgr.debug('configuring formatter...')
    # get formatter instance
    # TODO: (IMPRV) move formatter instance definition to function inside
    # TODO: (IMPRV) the current function and add _
    if hasattr(forms, formatter):
        formatter_instance = getattr(forms, formatter)(format_config)
    else:
        lgr.error('could not find formatter: {0}. please make sure the '
                  'formatter you\'re calling exists.'.format(formatter))
        raise FeederError('missing formatter')
    # and get the current time
    start_time = get_current_time()
    lgr.debug('start time is: {0}'.format(start_time))
    lgr.info('sending logs... EN GARDE!')
    while True:
        # generate the log data from the formatter
        logs = [formatter_instance.generate_data() for i in xrange(batch)]
        # and send the log through the relevant transport
        for log in logs:
            instance.send(client, log)
        message_count += batch
        # check if the number of messages sent are less than the desired amount
        if message_count < messages:
            # just to get some feedback during execution
            if not message_count % (1 / gap):
                lgr.info('{0} logs written. NICE!'.format(message_count))
            # and sleep the desired amount of time.. zzz zz zZZ zZZzzzz
            sleep(gap)
        else:
            break
    # then get the current time once more
    end_time = get_current_time()
    lgr.debug('end time is: {0}'.format(end_time))
    # and the elapsed time
    elapsed_time = end_time - start_time
    # meH!
    throughput, seconds = calculate_throughput(elapsed_time, messages)
    # TODO: (FEAT) add the option to send the throughput as well to benchmark
    # TODO: (FEAT) the logging process itself.
    lgr.info('DONE! (after {0}h ({1} seconds) with '
             'throughput: {2} logs/sec. now you can go for coffee.)'.format(
                 elapsed_time, seconds, throughput))
    try:
        # create a pretty table to write the statistical data to
        # TODO: (IMPRV) move this to generator function.
        data = instance.get_data()
        lgr.info('statistical data:\n {0}'.format(data))
    except AttributeError:
        lgr.debug(
            'statistical data not implemented for chosen transport.')
    # TODO: (IMPRV) why is this here?
    return


def config_transport(transports, transport, transport_config):
    """returns a configured instance and client for the transport

    :param transports: transport classes to choose from.
    :param string transport: transport to use
    :param dict transport_config: transport configuration
    """
    lgr.debug('configuring transport...')
    # get transport instance
    if hasattr(transports, transport):
        transport_instance = getattr(transports, transport)(transport_config)
    else:
        lgr.error('could not find transport: {0}. please make sure the '
                  'transport you\'re calling exists.'.format(transport))
        raise FeederError('missing transport')
    # get logging client
    client = transport_instance.configure()
    return transport_instance, client


def generator(config=None, transport=None, formatter=None, gap=None,
              messages=None, batch=False, verbose=False):
    """generates log messages

    this will generate log message in the requested format and protocol.

    :param string config: path to config file path
    :param string transport: transport type to use
    :param string formatter: formatter to use
    :param float gap: gap in seconds between 2 messages
    :param int messages: number of messages to send
    :param int batch: number of messages to stack before sending
    :param bool verbose: sets verbose state for internal logging.
    """
    # set verbosity level for internal logging
    _set_global_verbosity_level(verbose)
    # set params for basic Feeder configuration
    # import config file
    config = _import_config(config) if config else {}
    transport = transport if transport else DEFAULT_TRANSPORT
    formatter = formatter if formatter else DEFAULT_FORMATTER
    gap = float(gap) if gap else DEFAULT_GAP
    messages = int(messages) if messages else DEFAULT_NUMBER_OF_MESSAGES
    batch = int(batch) if batch else 1

    # TODO: (IMPRV) move config to different function.
    # declare transport and formatter configuration. will assume defaults
    # if config file wasn't imported.
    transports_config = config.get('transports', {}) \
        if config else {}
    formatters_config = config.get('formatters', {}) \
        if config else {}
    transport_config = transports_config.get(transport, {}) \
        if transports_config.get(transport) else {}
    formatter_config = formatters_config.get(formatter, {}) \
        if formatters_config.get(formatter) else {}
    transport = transport_config.get('type', transport) \
        if transport_config else transport
    formatter = formatter_config.get('type', formatter) \
        if formatter_config else formatter

    # configure transport class instance and logging client
    lgr.debug('transport: {0}'.format(transport))
    lgr.debug('formatter: {0}'.format(formatter))
    lgr.debug('gap: {0}'.format(gap))
    lgr.debug('message count: {0}'.format(messages))

    # well.. you can't have that right? that would be stupid.
    if batch > int(messages):
        raise FeederError('batch number larger than total amount of messages')
    else:
        lgr.debug('batch: {0}'.format(batch))
    # define transport class instance and shipping client
    instance, client = config_transport(
        trans, transport + 'Transport', transport_config)
    # send the stuff
    send(instance, client, formatter + 'Formatter', formatter_config,
         messages, gap, batch)
    # maybe close a connection to the host is required...
    try:
        instance.close()
    except AttributeError:
        lgr.debug('connection closing not implemented for chosen transport.')


def list_fake_types():
    """prints a list of random data types with an example"""
    fake = Factory.create()
    ignore_list = [
        'add_provider',
        'format',
        'get_formatter',
        'set_formatter',
        'parse',
        'provider',
        'providers',
        'get_providers',
    ]
    fakes_list = []

    # yes, the following is sort of disgusting. will have to find a better way
    # to implement this...
    # list from fake-factory
    for fake_type in dir(fake):
        if not fake_type.startswith('_') and fake_type not in ignore_list:
            fakes_list.append('*** {0} ({1})'.format(
                fake_type, getattr(fake, fake_type)()))
    # list from format mappings default handler
    for fake_type, data in fm.DATA.items():
        fakes_list.append('*** {0} ({1})'.format(
            fake_type, random.choice(data)))
    # list from format mappings additional handlers
    for fake_type in dir(fm.InHouseFaker):
        if not fake_type.startswith('_') and not fake_type == 'default':
            fakes_list.append('*** {0} ({1})'.format(
                fake_type, getattr(fm.InHouseFaker(), fake_type)()))
    print("\n".join(fakes_list))


def list_transports():
    for transport in dir(trans):
        if 'Transport' in transport:
            print('*** {0}'.format(transport.replace('Transport', '')))


def list_formatters():
    for formatter in dir(forms):
        if 'Formatter' in formatter:
            print('*** {0}'.format(formatter.replace('Formatter', '')))


class FeederError(Exception):
    pass
