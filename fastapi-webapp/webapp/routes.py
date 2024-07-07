# import the required modules here
from fastapi import Depends

from auth.dependencies import protected_endpoint


# Define your router

# use the router as a decorator, tip: method should be `get` of `/`
# signature: ("/")
def heels():
    return {'message': 'There should be a template here'}


# use the router as a decorator, tip: method should be `get` of `/home`
# signature: ("/home")
def home():
    return {'message': 'There should be a template here'}

# use the router as a decorator, tip: method should be `get` of `/profile`
# signature: ("/profile", dependencies=[Depends(protected_endpoint)])
def profile():
    # dependecies will be explained with the sessions portion of the tutorial
    return {'message': 'There should be a template here'}
