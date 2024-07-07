from auth.decorators import requires_auth
from flask import Blueprint, render_template, session


webapp_bp = Blueprint('webapp', __name__, template_folder="templates")


@webapp_bp.route("/")
def heels():
    """
    Heels endpoint
    """

    return render_template("heels.html")


@webapp_bp.route("/home")
def home():
    """
    Home endpoint
    """

    return render_template("home.html")


@webapp_bp.route("/profile")
@requires_auth
def profile():
    """
    Protected endpoint which displays your profile if you are logged in, otherwise it prompts the user to log in
    """
    return render_template(
        'profile.html',
        session=session.get('user')
    )