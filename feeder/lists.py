import random
# import fakers
from faker import Factory
import format_mappings as fm

import transports as trans
import formatters as forms


def list_fake_types(printout=True):
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
            fakes_list.append('*** {} ({})'.format(
                fake_type, getattr(fake, fake_type)()))
    # list from format mappings default handler
    for fake_type, data in fm.DATA.items():
        fakes_list.append('*** {} ({})'.format(fake_type, random.choice(data)))
    # list from format mappings additional handlers
    for fake_type in dir(fm.InHouseFaker):
        if not fake_type.startswith('_') and not fake_type == 'default':
            fakes_list.append('*** {} ({})'.format(
                fake_type, getattr(fm.InHouseFaker(), fake_type)()))
    if printout:
        print("\n".join(fakes_list))
    return fakes_list


def list_transports():
    for transport in dir(trans):
        if 'Transport' in transport:
            print('*** {}'.format(transport.replace('Transport', '')))


def list_formatters():
    for formatter in dir(forms):
        if 'Formatter' in formatter:
            print('*** {}'.format(formatter.replace('Formatter', '')))
