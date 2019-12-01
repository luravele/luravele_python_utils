import json


class Utils:

    @staticmethod
    def getConfig(filename):
        with open(filename, 'r') as f:
            config = json.load(f)
        return config

    @staticmethod
    def saveConfig(filename, config):
        with open(filename, 'w') as f:
            json.dump(config, f)