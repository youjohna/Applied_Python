from Arthropod import arthropod
import random as rand

class insect(arthropod):
    insect_count =  0

    def __init__(self, name_param, color_param, limbs_count_prim, wings_count_parm):
        """
        a. Description: Constructs a new Insect object.
        b. Parameters: 4
            i. name_param (String)
            ii. color_param (String)
        Class Insect
            iii. limbs_count_param (int)
            iv. wings_count_param (int)
        c. Returns 0
        d. Inherits from Arthropod and extends functionality. Assigns parameters to instance attributes. Increases insect_count by 1.
        """
        super().__init__(name_param,color_param,limbs_count_prim)
        self.wing_count = wings_count_parm
        insect.insect_count += 1

    def __str__(self):
        """
        a. Description: retrieves data about the insect when printing.
        b. Parameters: 0
        c. Returns: 1
            i. Data about the arachnid, such as: "The silver mosquito has 6 limbs and 2 wings." (String)
        """
        return 'The ' + self.color + " " + self.name + " spider has " + str(self.limbs_count) + " limbs and "+str(self.wing_count)+" wings."

    def get_wings_count(self):
        """
        a. Description: Retrieves insect wings count.
        b. Parameters: 0
        c. Returns: 1
            i. self.wings_count instance attribute
        """
        return self.wing_count

    def get_power(self):
        """
        a. Description: retrieves the power of the insect
        b. Parameters: 0
        c. Returns: 1
            i. self.limbs_count + self.wings_count (int)
        """
        return self.limbs_count + self.wing_count

    def lose_fight(self):
        """
        a. Description: insect potentially loses limbs and wings.
        b. Parameters: 0
        c. Returns: 0
        d. Inherits from Arthropod to potentially lose limbs. Additionally, based on the number of existing wings,
        randomly generate a number and lose that number of wings. update self.wings_count instance attribute.
        """
        limbLost = rand.randint(0, self.limbs_count)
        self.limbs_count = self.limbs_count - limbLost

        wingLost = rand.randint(0, self.wing_count)
        self.wing_count = self.wing_count - wingLost
