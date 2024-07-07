from urllib.parse import quote_plus, urlencode

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from config import config
from auth.config import oauth


auth_router = APIRouter()


@auth_router.get("/login")
async def login(request: Request):
    """
    Redirects the user to the Auth0 Universal Login (https://auth0.com/docs/authenticate/login/auth0-universal-login)
    """
    if not 'id_token' in request.session:  # it could be userinfo instead of id_token
        return await oauth.auth0.authorize_redirect(
            request,
            redirect_uri=request.url_for("callback")
        )
    return RedirectResponse(url=request.url_for("profile"))


@auth_router.get("/logout")
def logout(request: Request):
    """
    Redirects the user to the Auth0 Universal Login (https://auth0.com/docs/authenticate/login/auth0-universal-login)
    """
    response = RedirectResponse(
        url="https://" + config['AUTH0']['DOMAIN']
            + "/v2/logout?"
            + urlencode(
                {
                    "returnTo": request.url_for("heels"),
                    "client_id": config['AUTH0']['CLIENT_ID'],
                },
                quote_via=quote_plus,
            )
    )
    request.session.clear()
    return response


@auth_router.get("/callback")
async def callback(request: Request):
    """
    Callback redirect from Auth0
    """
    token = await oauth.auth0.authorize_access_token(request)
    # Store `id_token`, and `userinfo` in session
    request.session['id_token'] = token['id_token']
    request.session['userinfo'] = token['userinfo']
    return RedirectResponse(url=request.url_for("profile"))
