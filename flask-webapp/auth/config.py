from authlib.integrations.flask_client import OAuth
from flask import current_app
from config import config


oauth = OAuth(current_app)


oauth.register(
    "auth0",
    client_id=config["AUTH0"]["CLIENT_ID"],
    client_secret=config["AUTH0"]["CLIENT_SECRET"],
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{config["AUTH0"]["DOMAIN"]}/.well-known/openid-configuration'
)
