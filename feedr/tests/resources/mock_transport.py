#!/usr/bin/env python
import logging
import os


class MockTransport():
    """a RotatingFileHandler transport implementation"""
    def __init__(self, config):
        self.file_path = 'generated.log'
        self.max_bytes = 1000000
        self.backups_count = 1

    def configure(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        logger = logging.getLogger('feedr')
        handler = logging.handlers.RotatingFileHandler(
            self.file_path, maxBytes=self.max_bytes,
            backupCount=self.backups_count)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def send(self, client, log):
        client.debug(log)
