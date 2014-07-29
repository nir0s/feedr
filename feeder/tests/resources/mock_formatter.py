import random


class MockFormatter():
    def __init__(self, config):
        self.format = ['field']
        self.data = {
            'field': ['data']
        }

    def generate_data(self):
        log = ''
        for field_name in self.format:
            for field, data in self.data.items():
                if field_name == field:
                    log += random.choice(self.data[field_name])
            if field_name not in self.data.keys():
                log += field_name
        return log
