# flake8: NOQA
from time import gmtime, strftime
import datetime
import random


DATA = {
    'syslog_error_levels': ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
    'syslog_error_levels_lower': ['debug', 'info', 'warning', 'error', 'critical'],
    'http_verbs': ['OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE'],
    'http_versions': ['HTTP/1.0', 'HTTP/1.1'],
    'http_error_codes': [
        '100', '101',
        '200', '201', '202', '203', '204', '205', '206',
        '300', '301', '302', '303', '304', '305',
        '400', '401', '402', '403', '404', '405', '406', '407', '408', '409', '410', '411', '412', '413', '414', '415',
        '500', '501', '502', '503', '504', '505'
    ],
    'http_more_verbs': [
        'TRACE', 'CONNECT', 'PROPFIND', 'PROPPATCH', 'MKCOL',
        'COPY', 'MOVE', 'LOCK', 'UNLOCK', 'VERSION-CONTROL',
        'REPORT', 'CHECKOUT', 'CHECKIN', 'UNCHECKOUT', 'MKWORKSPACE',
        'UPDATE', 'LABEL', 'MERGE', 'BASELINE-CONTROL', 'MKACTIVITY',
        'ORDERPATCH', 'ACL', 'draft-dusseault-http-patch', 'PATCH',
        'draft-reschke-webdav-search', 'SEARCH'
    ],
    'time_zone_number': [
        '-1200', '-1100', '-1000', '-0900', '-0800', '-0700', '-0600', '-0500', '-0400', '-0300', '-0200', '-0100', '-0000',
        '+1200', '+1100', '+1000', '+0900', '+0800', '+0700', '+0600', '+0500', '+0400', '+0300', '+0200', '+0100', '+0000',
    ],
    'month_name_short': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'day_of_week_short': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
}


class InHouseFaker():
    def __init__(self):
        self.dt = datetime.datetime.now()

    def default(self, data_type):
        return random.choice(DATA[data_type])

    def current_time(self):
        return str(self.dt.time().replace(microsecond=0))

    def current_date_time(self):
        return str(self.dt.replace(microsecond=0))

    def current_day_of_month(self):
        return str(self.dt.strftime("%d"))

    def current_day_of_week_short(self):
        return str(self.dt.strftime("%A")[0:3])

    def current_year(self):
        return str(self.dt.strftime("%y"))

    def current_month_name_short(self):
        return str(self.dt.strftime("%B")[0:3])

    def current_time_zone_number(self):
        return strftime("%z", gmtime())
