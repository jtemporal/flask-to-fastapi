from fastapi import FastAPI
from auth.routes import auth_router
# import your webapp router


app = FastAPI()


# don't forget to add the webapp router here
app.include_router(auth_router)