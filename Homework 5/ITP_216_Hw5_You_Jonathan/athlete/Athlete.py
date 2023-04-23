# Jonathan You, youjohna@usc.edu
# ITP 216, Spring 2023
# Section: Tuesday 7pm
# Homework 5
# Description:
# This homework builds on the concepts that were explored last week, but primarily focuses on the creation of a package and modules
# The package is called athlete with the modules Athlete, Boxer, Swimmer, and __init__.py
# The main method that runs the program is outside the package, or ITP_216_HW5_You_Jonathan.py


class athlete():
    athlete_count = 0;

    def __init__(self, name_param, dob_param, origin_param, medals_param):
        """
        a. Description: Constructs a new Athlete object.
        b. Parameters: 4
            i. name_param (String)
            ii. dob_param (String)
            iii. origin_param (String)
            iv. medals_param (list)
        c. Returns: 0
        d. Assigns parameters to instance attributes. Increases athlete_count by 1.
        """
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        athlete.athlete_count +=1

    def get_name(self):
        """
        a. Description: retrieves the name
        b. Parameters: 0
        c. Returns: 1
            i. self.name
        """
        return self.name

    def get_dob(self):
        """
        a. Description: retrieves the date of birth
        b. Parameters: 0
        c. Returns: 1
            i. self.dob
        """
        return self.dob

    def get_origin(self):
        """
        a. Description: retrieves the origin
        b. Parameters: 0
        c. Returns: 1
            i. self.origin
        """
        return self.origin

    def get_medals(self):
        """
        a. Description: retrieves the list of medals
        b. Parameters: 0
        c. Returns: 1
            i. self.medals
        """
        return self.medals

    def add_medal(self, medal_param):
        """
        a. Description: adds a new medal to the medal list
        b. Parameters: 1
            i. medal_param (String)
        c. Returns: 0
        """
        self.medals.append(medal_param)
