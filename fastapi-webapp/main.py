from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from auth.routes import auth_router
from webapp.routes import webapp_router
from config import config


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key=config['WEBAPP']['SECRET_KEY'])

app.include_router(webapp_router)
app.include_router(auth_router)