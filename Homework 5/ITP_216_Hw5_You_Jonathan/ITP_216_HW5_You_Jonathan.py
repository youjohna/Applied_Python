# imported the classes from the package
from athlete.Boxer import Boxer
from athlete.Swimmer import Swimmer

def main():
    """
    Creating an object of the Swimmer class
    Testing it out with the inputted parameters
    Testing the get_strokes method
    Testing the add_strokes method
    prints the new updated object
    """
    swimmer1 = Swimmer("Jonathan", "12/25/2001", "Los Angeles, California", ['Gold (2012)', 'Gold (2016)'], ['freestyle', 'breaststroke'])
    print(swimmer1)
    print(swimmer1.get_strokes())
    swimmer1.add_strokes('backstroke')
    print(swimmer1)
    print()

    """
    Creating an object of the Boxer class
    Testing it out with the inputted parameters
    Testing the set_weight_class method
    Testing the win and lose fight methods
    prints the new updated object
    """
    boxer1 = Boxer ("Phillip", "08/15/2001", "Spokane, Washington", ['Bronze (2012)','Bronze (2013)'], 'Flyweight')
    print(boxer1)
    boxer1.set_weight_class('Heavyweight')
    boxer1.win_fight()
    boxer1.lose_fight()
    print(boxer1)





if __name__ == '__main__':
    main()