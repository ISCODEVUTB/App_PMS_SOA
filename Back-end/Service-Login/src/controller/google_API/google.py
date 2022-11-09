import os
import pathlib
import requests
from flask import jsonify, render_template, session, abort, request, redirect
import controller.users_API.users as users
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import google.auth.transport.requests
from pip._vendor import cachecontrol


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

GOOGLE_CLIENT_ID = "883006890009-t77ir0eo7kbobhakiadtr8buu37cb5tf.apps.googleusercontent.com"
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="http://127.0.0.1:5000/callback"
)


def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            # Authorization required
            return abort(401)
        else:
            return function()
        
    return wrapper


def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state
    return redirect(authorization_url)


def callback():
    flow.fetch_token(authorization_response=request.url)
   
    if not session["state"] == request.args["state"]:
        # State does nor math
        return abort(500)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    session["google_id"] = id_info.get("sub")
    session["family_name"] = id_info.get("family_name")
    session["given_name"] = id_info.get("given_name")
    session["picture"] = id_info.get("picture")
    session["locale"] = id_info.get("locale")
    session["name"] = id_info.get("name")
    session["email"] = id_info.get("email")
    
    return redirect("/protect")


def logout():
    session.clear()
    return redirect("/")



    