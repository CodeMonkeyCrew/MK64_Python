import configparser
''' 
    Read config file and return <key:value> pairs
'''
def read_config(config_file):
    if(config_file != None):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config
