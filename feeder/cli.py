# flake8: NOQA
"""Script to run feeder via command line

Usage:
    mouth feed [--config=<path> --transport=<string> --format=<string> --gap=<int> --messages=<int> --batch=<int> -v]
    mouth list (fake|transports|formatters)
    mouth --version

Arguments:
    feed                Generates Logs
    list fake           Lists different data options (with an example)
    list transports     Lists the type of transports available
    list formatters     Lists the type of formatters available

Options:
    -h --help                   Show this screen.
    -c --config=<path>          Path to generator config file.
    -t --transport=<string>     transport to use (e.g. File)
    -f --format=<string>        output format (e.g. Json)
    -g --gap=<int>              Number of seconds between messages (can be less than 1)
    -m --messages=<int>         Number of messages to generate (if omitted will assume infinity (good for daemonization))
    -b --batch=<int>            Number of messages to stack before shipping
    -v --verbose                a LOT of output
    --version                   Display current version of feeder and exit

"""

from __future__ import absolute_import
from docopt import docopt
import feeder.logger as logger
from feeder.feeder import _set_global_verbosity_level
from feeder.feeder import generator
from feeder.feeder import list_fake_types, list_transports, list_formatters

lgr = logger.init()


def ver_check():
    import pkg_resources
    version = None
    try:
        version = pkg_resources.get_distribution('feeder').version
    except Exception as e:
        print(e)
    finally:
        del pkg_resources
    return version


def feeder_run(o):
    if o['list']:
        if o['fake']:
            list_fake_types()
        elif o['transports']:
            list_transports()
        elif o['formatters']:
            list_formatters()

    elif o['feed']:
        generator(config=o.get('--config'),
                 transport=o.get('--transport'),
                 formatter=o.get('--format'),
                 gap=o.get('--gap'),
                 messages=o.get('--messages'),
                 batch=o.get('--batch'),
                 verbose=o.get('--verbose'))


def feeder(test_options=None):
    """Main entry point for script."""
    version = ver_check()
    options = test_options or docopt(__doc__, version=version)
    _set_global_verbosity_level(options.get('--verbose'))
    lgr.debug(options)
    feeder_run(options)


def main():
    feeder()


if __name__ == '__main__':
    main()
