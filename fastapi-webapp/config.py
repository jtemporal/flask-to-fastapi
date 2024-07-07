import configparser
import os
import secrets


def load_config():
    """
    Loads configuration from .config file
    """

    config = configparser.ConfigParser()
    if os.path.exists(".config"):
        config.read(".config")
        return config
    
    config = {
        'WEBAPP': {
            'SECRET_KEY': secrets.token_hex(32)
        },
        'AUTH0': { 
            'DOMAIN': 'YOUR_DOMAIN.eu.auth0.com',
            'CLIENT_ID': 'YOUR_CLIENT',
            'CLIENT_SECRET': 'YOUR_SECRET',
        },
    }
    return config


config = load_config()
