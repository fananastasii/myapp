from flask import Flask, render_template, redirect, url_for
from data import test_profiles, usernames_to_profiles, companies
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

auth = HTTPBasicAuth()
loggedin_id = 0

@auth.verify_password
def verify_password(username,password):
    if username in usernames_to_profiles and check_password_hash(test_profiles[usernames_to_profiles[username]]["password"], password):
        global loggedin_id 
        loggedin_id = usernames_to_profiles[username]
        return True

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/profile/<int:profile_id>")
@auth.login_required
def profile(profile_id):
    if loggedin_id != profile_id :
       redirect (url_for("profile", profile_id=loggedin_id)) 
    profile = test_profiles[profile_id]
    return render_template('profile.html', title="Profile", profile=profile, company=company)

@app.route("/logout")
@auth.login_required
def logout(): 
    return render_template('logout.html'), 401

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/aboutus")
@auth.login_required
def aboutus():
    return render_template('aboutus.html')

@app.route("/main")
@auth.login_required
def main():
    return render_template('main.html', profile=loggedin_user())

@app.route("/company/<int:company_id>")
@auth.login_required
def company(company_id): 
    company = companies[company_id]
    return render_template('company.html', company=company)

def loggedin_user(): 
    return test_profiles[loggedin_id]