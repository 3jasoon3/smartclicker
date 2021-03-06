import configparser
import string
from exceptions import CantParseCfg
def parse(file_path)->list:
    config = configparser.ConfigParser()
    config.read(file_path)
    start_key = config['keys']['start_button']
    end_key = config['keys']['end_button']
    if start_key.lower() in string.ascii_lowercase and end_key.lower() in string.ascii_lowercase:
        return [start_key, end_key]
    raise CantParseCfg