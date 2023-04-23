from .Athlete import athlete

class Swimmer(athlete):
    swimmer_count = 0

    def __init__(self, name_param, dob_param, origin_param, medals_param, strokes_param):
        """
        a. Description: Constructs a new Swimmer object.
        b. Parameters: 5
            i. name_param (String)
            ii. dob_param (String)
            iii. origin_param (String)
            iv. medals_param (list)
            v. strokes (list)
        c. Returns: 0
        d. Assigns parameters to instance attributes. Increases swimmer_count by 1.

        All inherited class attributes, plus:
        1. self.strokes
            a. the strokes that the swimmer knows (list)
        """
        self.name = name_param
        self.dob = dob_param
        self.origin = origin_param
        self.medals = medals_param
        self.strokes = strokes_param
        Swimmer.swimmer_count +=1

    def __str__(self):
        """
        a. Description: retrieves data about the swimmer when printing.
        b. Parameters: 0
        c. Returns: 1
            i. Data about the swimmer. (String)
        """
        return self.name + " is a swimmer from " + self.origin + " born on " + self.dob + ". "+self.name+" knows "+str(self.strokes)+", and has won "+str(len(self.medals))+" medals: "+str(self.medals)

    def get_strokes(self):
        """
        a. Description: retrieves the strokes attribute
        b. Parameters: 0
        c. Returns: 1
            i. self.strokes
        """
        return self.strokes

    def add_strokes(self, new_stroke_param):
        """
        a. Description: adds a new stroke to the swimmer's repertoire. Checks to make sure the stroke is not already in the list
        b. Parameters: 1
        c. Returns: 0
        """
        if not new_stroke_param in self.strokes:        # Checks to see if the inputted stroke parameter was not already in list
            self.strokes.append(new_stroke_param)
