# Jonathan You, youjohna@usc.edu
# ITP 216, Spring 2023
# Section: Tuesday 7pm
# Homework 11
# Description:
# The purpose of this homework is to practice a basic version of front end (html) and backend (database/server).
# However, homework 11 was different from homework 10 because it utilizes SQLlite as a database instead provided JSON
# files. This homework practices getting, creating, and modifying data from databaess.

from flask import Flask, redirect, render_template, request, session, url_for
import os
import sqlite3 as sl

app = Flask(__name__)           # Flask is utilized for front end
db = "favouriteFoods.db"        # imports the database file


# root end point
# routes to login unless client has already logged in
@app.route("/")
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
    if session["username"] == "admin" and session["password"] == "passwords":  # if the admin inputted the correct username and password
        return render_template("admin.html", username=session["username"], result=db_get_user_list()) # returns html for admin
    else:  # if it's another user
        return render_template("user.html", username=session["username"], fav_food=db_get_food(session["username"]))  # returns html for that user


# create user endpoint (admin only)
# adds new user to db, then re-renders admin template
@app.route("/action/createuser", methods=["POST", "GET"])
def create_user():
    """
    Callable from admin.html only
    Adds a new user to db by calling db_create_user, then re-renders admin template

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    username = request.form["username"]  # input from admin "create user"
    password = request.form["password"]  # input from admin "create user"
    db_create_user(username, password)  # calls db function to create new user and add into the database
    return render_template("admin.html", username=session["username"], result=db_get_user_list())  # refreshes the html for admin


# remove user endpoint (admin only)
# removes user from db, then re-renders admin template
@app.route("/action/removeuser", methods=["POST", "GET"])
def remove_user():
    """
    Callable from admin.html only
    Removes user from the db by calling db_remove_user, then re-renders admin template.

    :return: redirects to home if user not logged in,
                re-renders admin.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    username = request.form["username"]  # input from admin "delete user"
    db_remove_user(username)  # calls db function to delete new user and remove from the database
    return render_template("admin.html", username=session["username"],result=db_get_user_list())  # refreshes html for admin


# set food endpoint (user only)
# updates user food, then re-renders user template
@app.route("/action/setfood", methods=["POST", "GET"])
def set_food():
    """
    Callable from user.html only,
    Updates user food by calling db_set_food, then re-renders user template

    :return: redirects to home if user not logged in,
                re-renders user.html otherwise
    """
    # TODO: your code goes here and replaces 'pass' below
    db_set_food(session["username"], request.form["set_fav_food"])  # calls db function to set the inputted string as the user's new favorite food
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
        if db_check_creds(request.form["username"],request.form["password"]) == True: # checks to see if the user credentials are a match
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
    session["logged_in"] = False  # changes the boolean condition required to get out of "home"
    return redirect(url_for("home"))


def db_get_user_list() -> dict:
    """
    Queries the DB's userfoods table to get a list
    of all the user and their corresponding favorite food for display on admin.html.
    Called to render admin.html template.

    :return: a dictionary with username as key and their favorite food as value
                this is what populates the 'result' variable in the admin.html template
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()

    stmt = 'SELECT * FROM userfoods'    # SQL statement to call all users and their corresponding foods
    results = curs.execute(stmt)        # executes statement

    return dict(results)                # returns a dictionary of the results


def db_create_user(un: str, pw: str) -> None:
    """
    Add provided user and password to the credentials table
    Add provided user to the userfoods table
    and sets their favorite food to "not set yet".
    Called from create_user() view function.

    :param un: username to create
    :param pw: password to create
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()

    v = (un, pw,)                       # tuple of inputted strings
    stmt = 'INSERT INTO credentials(username, password) VALUES (?,?)'  # SQL statement to create a new user and password
    curs.execute(stmt, v)               # executes statement

    v1 = (un,)                          # tuple of inputted string
    stmt2 = 'INSERT INTO userfoods(username, food)VALUES (?,NULL)' # SQL statement to create a new user and NULL food
    curs.execute(stmt2, v1)             # executes statement

    conn.commit()                       # saves changes




def db_remove_user(un: str) -> None:
    """
    Removes provided user from all DB tables.
    Called from remove_user() view function.

    :param un: username to remove from DB
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()

    v = (un,)                           # tuple of inputted string
    stmt = 'DELETE FROM credentials WHERE username =?'  # SQL statement to delete user and password

    stmt2 = 'DELETE FROM userfoods WHERE username =?'   # SQL statemnt to delete user and food choice


    curs.execute(stmt, v)           # executes statement
    curs.execute(stmt2, v)          # executes statement
    conn.commit()                   # saves changes


def db_get_food(un: str) -> str:
    """
    Gets the provided user's favorite food from the DB.
    Called to render user.html fav_food template variable.

    :param un: username to get favorite food of
    :return: the favorite food of the provided user as a string
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()

    v = (un,)                           # tuple of inputted string
    stmt = 'SELECT food FROM userfoods WHERE username=?'    # SQL statement to return the food of selected user
    curs.execute(stmt, v)               # executes statement
    result = curs.fetchone()            # selects a single result
    return str(result[0])               # returns string value

def db_set_food(un: str, ff: str) -> None:
    """
    Sets the favorite food of user, un param, to new incoming ff (favorite food) param.
    Called from set_food() view function.

    :param un: username to update favorite food of
    :param ff: user's new favorite food
    :return: None
    """
    # TODO: your code goes here and replaces 'pass' below
    conn = sl.connect(db)
    curs = conn.cursor()

    v = (ff, un)                        # tuple of inputted strings
    stmt = 'UPDATE userfoods SET food =? WHERE username=?'  # updates food value for selected user
    curs.execute(stmt, v)               # executes statement
    conn.commit()                       # saves changes


# database function
# connects to db and checks cred param (all clients)
def db_check_creds(un, pw):
    """
    Checks to see if supplied username and password are in the DB's credentials table.
    Called from login() view function.

    :param un: username to check
    :param pw: password to check
    :return: True if both username and password are correct, False otherwise.
    """
    conn = sl.connect(db)
    curs = conn.cursor()
    v = (un,)                           # tuple of inputted strings
    stmt = "SELECT password FROM credentials WHERE username=?"  # checks the password of inputted user string
    results = curs.execute(stmt, v)     # results is an iterable cursor of tuples (result set)
    correct_pw = ''                     # empty string for password
    for result in results:              # goes through all tuples of password
        correct_pw = result[0]          # each result is a tuple of 1, so grab the first thing in it
    conn.close()
    if correct_pw == pw:                # checks to see if the inputted password matches with the correct password
        return True                     # if password matches, returns as true
    return False                        # otherwise, returns as false


# main entrypoint
# runs app
if __name__ == "__main__":
    # DB function unit testing:
    assert db_check_creds('alice', 'alicesSecurePassWord') == True
    assert db_check_creds('wrongUser', 'alicesSecurePassWord') == False
    assert db_check_creds('alice', 'wrongPassword') == False

    # TODO: Unit test your other db_ functions here

    app.secret_key = os.urandom(12)
    app.run(debug=True)

