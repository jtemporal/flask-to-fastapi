from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates

from auth.dependencies import protected_endpoint
from utils import to_pretty_json


webapp_router = APIRouter()

templates = Jinja2Templates(directory="webapp/templates")
templates.env.filters['to_pretty_json'] = to_pretty_json


@webapp_router.get("/")
def heels(request: Request):
    """Heels page"""
    
    return templates.TemplateResponse(
        "heels.html",
        {
            "request": request
        }
    )


@webapp_router.get("/home")
def home(request: Request):
    """Home page"""
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request
        }
    )


@webapp_router.get("/profile", dependencies=[Depends(protected_endpoint)])
def profile(request: Request):

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "userinfo": request.session['userinfo']
        }
    )
