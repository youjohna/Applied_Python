# Jonathan You, youjohna@usc.edu
# ITP 216, Spring 2023
# Section: Tuesday 7pm
# Homework 6
# Description:
# The purpose of this homework is to practice a basic version of front end (html) and backend (database/server).
# This homework utilized provided html files, jSON files, and a provided python file helper.
# This homework utilzied various urls/files to create a web app that allows the user to log in to different accounts (users and admins),
# and view, edit, delete favorite foods and new users.

from flask import Flask, redirect, render_template, request, session, url_for
import os

from util import FileDBHelper as fdb

app = Flask(__name__)

# root end point
# routes to login unless client has already logged in
@app.route("/",  methods = ["POST", "GET"])
def home():
    """
    Checks whether the user is logged in and returns appropriately.
    :return: renders login.html if not logged in,
                redirects to client otherwise.
    """
    # TODO: your code goes here and replaces 'pass' below
    if not session.get("logged_in"):            # set in login(), runs if FALSE
        return render_template("login.html")    # sets up the html for "login"
    else:                                       # if TRUE, or logged in
        return redirect(url_for("client"))      # goes to client function/url



# client endpoint
# renders appropriate template (admin or user)
@app.route("/client")
def client():
    """
    Renders appropriate template (admin or user)
    NOTE: Should only come to /client if /login'ed successfully, i.e. (db_check_creds() returned True)

    :return: redirects home if not logged in,
                renders admin.html if logged in as admin,
                user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if session["username"]=="admin" and session["password"] == "password":                                                  # if the admin inputted the correct username and password
        return render_template("admin.html", username = session["username"], result = fdb.db_get_user_list(foods_db_file))  # returns html for admin
    else:                                                                                                                   # if it's another user
        return render_template("user.html", username = session["username"], fav_food = fdb.db_get_food(session["username"],foods_db_file))  # returns html for that user



# create user endpoint (admin only)
# adds new user to db, then re-renders admin template
@app.route("/action/createuser", methods=["POST", "GET"])
def create_user():
    """
    Gets called from admin.html form submit
    Adds a new user to db by calling db_create_user, then re-renders admin template

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    username = request.form["username"]  # input from admin "create user"
    password = request.form["password"]  # input from admin "create user"
    fdb.db_create_user(username, password, creds_db_file, foods_db_file)        # calls fileDBHelper to create new user and add into the JSON files
    return render_template("admin.html", username = session["username"], result = fdb.db_get_user_list(foods_db_file))  # refreshes the html for admin

# remove user endpoint (admin only)
# removes user from db, then re-renders admin template
@app.route("/action/removeuser", methods=["POST", "GET"])
def remove_user():
    """
    Gets called from admin.html form submit
    Removes user from the db by calling db_remove_user, then re-renders admin template.

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    username = request.form["username"]  # input from admin "delete user"
    fdb.db_remove_user(username, creds_db_file, foods_db_file) # calls fileDBHelper to delete new user and remove from the JSON files
    return render_template("admin.html", username=session["username"], result=fdb.db_get_user_list(foods_db_file)) # refreshes html for admin


# set food endpoint (user only)
# updates user food, then re-renders user template
@app.route("/action/setfood", methods=["POST", "GET"])
def set_food():
    """
    Gets called from user.html form submit
    Updates user food by calling db_set_food, then re-renders user template

    :return: redirects to home if user not logged in,
                re-renders user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    fdb.db_set_food(session["username"], request.form["set_fav_food"], foods_db_file)   # calls fileDBHelper to set the inputted string as the user's new favorite food
    return redirect(url_for("client"))  # redirects the url to the client which will automatically send to user html since it's still logged in


# login endpoint
# allows client to log in (checks creds)
@app.route("/login", methods=["POST", "GET"])
def login():
    """
    Allows client to log in
    Calls db_check_creds to see if supplied username and password are correct

    :return: redirects to client if login correct,
                redirects back to home otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    if request.method == "POST":
        if fdb.db_check_creds(request.form["username"],request.form["password"],creds_db_file) == True: # checks to see if the user credentials are a match
            session["username"] = request.form["username"]  # used in home/welcome, "memory"
            session["password"] = request.form["password"]  # used in home/welcome, "memory"
            session["logged_in"] = True  # checked in home()
            return redirect(url_for("client"))      # sends to client which will now redirect to the appropriate account
        else:
            return redirect(url_for("home"))        # sends back to home

# logout endpoint
@app.route("/logout", methods=["POST", "GET"])
def logout():
    """
    Logs client out, then routes to login
    Remove the user from the session
    :return: redirects back to home
    """
    # TODO: your code goes here and replaces 'pass' below
    session["logged_in"] = False                    # changes the boolean condition required to get out of "home"
    return redirect(url_for("home"))                # redirects the url to back "home"


# main entrypoint
# runs app
if __name__ == "__main__":

    creds_db_file = "./util/creds_db_file.json"
    foods_db_file = "./util/foods_db_file.json"

    # Initialize python dicts
    cred_db_dict = {"admin": "password", "user1": "pass1", "user2": "pass2", "user3": "pass3"}
    food_db_dict = {"user1": "cake", "user2": "popcorn", "user3": "pie"}

    # Save python dicts to their respective json db files
    fdb.save_dict_to_json_file(cred_db_dict, creds_db_file)
    fdb.save_dict_to_json_file(food_db_dict, foods_db_file)

    # Load json db files back to python dicts
    cred_db_dict = fdb.load_json_file_to_dict(creds_db_file)
    food_db_dict = fdb.load_json_file_to_dict(foods_db_file)
    assert cred_db_dict == {"admin": "password", 'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure a new user is created successfully in both tables w/ the proper initial values everywhere
    fdb.db_create_user('newUser', 'newPassword', creds_db_file, foods_db_file)
    creds_db_dict = fdb.load_json_file_to_dict(creds_db_file)
    foods_db_dict = fdb.load_json_file_to_dict(foods_db_file)
    assert creds_db_dict == {"admin": "password", 'user1': 'pass1', 'user2': 'pass2', 'user3': 'pass3', 'newUser': 'newPassword'}
    assert foods_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie', 'newUser': 'not set yet'}

    # Make sure a user is actually removed from the DB
    fdb.db_remove_user('user3', creds_db_file, foods_db_file)
    db_dict = fdb.load_json_file_to_dict(creds_db_file)
    foods_db_dict = fdb.load_json_file_to_dict(foods_db_file)
    assert db_dict == {"admin": "password", 'user1': 'pass1', 'user2': 'pass2', 'newUser': 'newPassword'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure removing a user that doesn't exist behaves properly (no effect on DB)
    fdb.db_remove_user('user doesnt exist', creds_db_file, foods_db_file)
    db_dict = fdb.load_json_file_to_dict(creds_db_file)
    assert db_dict == {"admin": "password", 'user1': 'pass1', 'user2': 'pass2', 'newUser': 'newPassword'}
    assert food_db_dict == {'user1': 'cake', 'user2': 'popcorn', 'user3': 'pie'}

    # Make sure get user list function works
    assert fdb.db_get_user_list(foods_db_file) == {'user1': 'cake', 'user2': 'popcorn', 'newUser': 'not set yet'}

    # Correct username and password (green case)
    assert fdb.db_check_creds('user1', 'pass1', creds_db_file) is True
    # Wrong username but right password
    assert fdb.db_check_creds('wrong user', 'pass1', creds_db_file) is False
    # Right username but wrong password
    assert fdb.db_check_creds('user1', 'wrong password', creds_db_file) is False
    # Wrong everything
    assert fdb.db_check_creds('wrong user', 'wrong password', creds_db_file) is False

    # Spot check values
    assert fdb.db_get_food('user1', foods_db_file) == 'cake'
    assert fdb.db_get_food('newUser', foods_db_file) == 'not set yet'
    assert fdb.db_get_food('user doesnt exist', foods_db_file) == 'Not Found!'

    # Update existing user
    fdb.db_set_food('user1', 'oreos', foods_db_file)
    assert fdb.db_get_user_list(foods_db_file) == {'user1': 'oreos', 'user2': 'popcorn', 'newUser': 'not set yet'}

    app.secret_key = os.urandom(12)
    app.run(debug=True)

