# Jonathan You, youjohna@usc.edu
# ITP 216, Spring 2023
# Section: Tuesday 7pm
# Homework 4
# Description:
# This homework practices using inheritance of classes. The parent class is this Arthropod class,
# and the two child classes that inherit from this class are Insect and Arachnid.

import random as rand


class arthropod():
    """
    Class Attributes
    1. arthropod_count
        a. The number of arthropods created.
    """
    arthropod_count = 0

    def __init__(self, name_param, color_param, limbs_count_prim):
        """
        a. Description: Constructs a new arthropod object
        b. Parameters: 3
            i. name_param (String)
            ii. color_param (String)
            iii. limbs_count_param (int)
        c. Returns 0
        d. Assigns parameters to instance attributes. Increases arthropod arthropod_count by 1.
        """
        self.name = name_param
        self.color = color_param
        self.limbs_count = limbs_count_prim
        arthropod.arthropod_count +=1

    def get_name(self):
        """
        a. Description: Retrieves arthropod name.
        b. Parameters: 0
        c. Returns: 1
            i. self.name instance attribute
        """
        return self.name

    def get_color(self):
        """
        a. Description: Retrieves arthropod color.
        b. Parameters: 0
        c. Returns: 1
            i. self.color instance attribute
        """
        return self.color

    def get_limbsCount(self):
        """
        a. Description: Retrieves arthropod limbs count.
        b. Parameters: 0
        c. Returns: 1
            i. self.limbs_count instance attribute
        """
        return self.limbs_count

    def set_color(self, color_input):
        """
        a. Description: Changes arthropod color.
        b. Parameters: 1
            i. A color (String)
        c. Returns: 0
        """
        self.color = color_input

    def lose_fight(self):
        """
        a. Description: arthropod potentially loses limbs.
        b. Parameters: 0
        c. Returns: 0
        d. Based on the number of existing limbs, randomly generate a number and lose that number of limbs. update
        self.limbs_count instance attribute.

        """
        limbLost = rand.randint(0, self.limbs_count)
        self.limbs_count = self.limbs_count - limbLost

