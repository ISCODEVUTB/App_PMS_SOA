import controller.google_API.google as google
import controller.users_API.users as users
from flask import Flask, session, render_template

app = Flask("Login Google")
app.secret_key = "5saf151d5f16adf"


@app.route("/login/google")
def loginApp():
    return google.login()


@app.route("/callback")
def callback_app():
    return google.callback()


@app.route("/logout")
def logout_app():    
    return google.logout()


@app.route("/protect")
@google.login_is_required
def protect():
    return users.create_user(session['family_name'], users.generate_password(),
                      session['given_name'], session['picture'],
                      session['google_id'], session['email'], session['name']) 


# login with name 
@app.route("/a")
def login_app_a():
    pass


if __name__ == "__main__":
    app.run(debug=True)



