import configparser

def read_config(config_file):
    if(config_file != None):
        config = configparser.RawConfigParser()
        config.read(config_file)
        return config
