from Arthropod import arthropod

class arachnid(arthropod):

    arachnid_count = 0

    def __init__(self, name_param, color_param, limbs_count_prim, venomous_param):
        """
        a. Description: Constructs a new Arachnid object.
        b. Parameters: 4
            i. name_param (String)
            ii. color_param (String)
            iii. limbs_count_param (int)
            iv. venomous_param (bool)
        c. Returns: 0
        d. Inherits from Arthropod and extends functionality. Assigns parameters to instance attributes. Increases arachnid_count by 1.
        """
        super().__init__(name_param,color_param,limbs_count_prim)
        self.venom = venomous_param
        arachnid.arachnid_count +=1

    def __str__(self):
        if self.venom == True:
            return 'The '+self.color+" venomous "+self.name+" spider has "+str(self.limbs_count)+" limbs."
        else:
            return 'The ' + self.color + " non-venomous " + self.name + " spider has " + str(self.limbs_count) + " limbs."

    def get_venomous(self):
        """
        a. Description: retrieves whether or not the arachnid is venomous
        b. Parameters: 0
        c. Returns: 1
            i. self.venomous attribute (Boolean)
        """
        return self.venom

    def get_power(self):
        if self.venom == True:
            return (self.limbs_count*2)
        else:
            return (self.limbs_count)
