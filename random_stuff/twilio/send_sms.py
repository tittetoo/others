import pdb

import json
import os
import pprint
import requests
from urllib.parse import urljoin, urlparse, urlsplit, quote, unquote, urlencode

from twilio.rest import Client


CONFIG_FILE_NAME = 'config.json'

def load_config():
    # We can extend this method to allow params, but for now, this is sufficient
    this_dir = os.path.dirname(__file__)
    config_file = open(os.path.join(this_dir, CONFIG_FILE_NAME))
    config = json.load(config_file)
    config_file.close()
    return config


if __name__ == '__main__':
    config = load_config()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(config)


    message_body = "Testing sms"


    client = Client(config['acnt_sid'], config['auth_token'])
    message = client.messages.create(
        #from_=config['from_num'],
        messaging_service_sid=config['messaging_service_sid'],
        to=config['test_to_num'],
        body=message_body,
    )
    print(message.sid)
    