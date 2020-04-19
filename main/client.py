import os

class Client:

    def __init__(self, username=None, password=None):
        self.username = username if username else os.environ['username']
        self.password = password if password else os.environ['password']

    def get_historical_data(self):
        pass

    def calculate_ema(self):
        pass