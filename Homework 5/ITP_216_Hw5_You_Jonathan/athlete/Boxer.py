from .Athlete import athlete

class Boxer(athlete):
    boxer_count = 0;
    """
    a. The number of boxers created.
    """

    def __init__(self, name_param, dob_param, origin_param, medals_param, weight_class):
        """
        a. Description: Constructs a new Boxer object.
        b. Parameters: 5
            i. name_param (String)
            ii. dob_param (String)
            iii. origin_param (String)
            iv. medals_param (list)
            v. weight_class (String)
        c. Returns: 0
        d. Assigns parameters to instance attributes. Increases boxer_count by 1.

        All inherited class attributes, plus:
        1. self.weight_class
            a. the weight class of the boxer (String)
        2. self.record
            a. the fight record of the boxer (list with two items: [wins (int), losses (int)] )
        """
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        self.wclass = weight_class
        self.record = [0, 0]
        Boxer.boxer_count +=1

    def get_wclass(self):
        """
        a. Description: retrieves the weight class
        b. Parameters: 0
        c. Returns: 1
            i. self.wclass
        """
        return self.wclass

    def get_record(self):
        """
        a. Description: retrieves the record
        b. Parameters: 0
        c. Returns: 1
            i. self.record
        """
        return self.record

    def __str__(self):
        """
        a. Description: retrieves data about the boxer when printing.
        b. Parameters: 0
        c. Returns: 1
            i. Data about the boxer. (String)
        """
        return self.name+" is a "+self.wclass+" boxer from "+self.origin+" born on "+self.dob+". "+self.name+" has a "+str(self.record)+" record, and has won "+str(len(self.medals))+" medals"

    def set_weight_class(self, weight_class_param):
        """
        a. Description: sets an attribute
        b. Parameters: 1
            i. weight_class_param (String)
        c. Returns: 0
        """
        self.wclass=weight_class_param

    def win_fight(self):
        """
        a. Description: adds one to the wins of the boxer's record
        b. Parameters: 0
        c. Returns: 0
        """
        winValue = self.record[0]
        winValue +=1
        self.record[0]=winValue

    def lose_fight(self):
        """
        a. Description: adds one to the losses of the boxer's record, then checks to see if the boxer needs to
retire (after 10 losses)
        b. Parameters: 0
        c. Returns: 1:
            i. A message about the number of fights left before retirement, or 'This boxer has retired.' (String)
        """
        loseValue = self.record[1]
        loseValue += 1
        self.record[1] = loseValue

        fightsLeft = 10-loseValue
        if fightsLeft >0:
            return self.name+" has only "+str(fightsLeft)+" fights left"
        else:
            return "This boxer has retired"