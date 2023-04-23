from Arachnid import arachnid
from Insect import insect
import random as rand

def main():
    insectPlayer = insect("Butterfly", "Pink", 6, 2)
    arachnidPlyer = arachnid("Spider", "Silver", 8, True)

    print(insectPlayer)
    print(arachnidPlyer)
    print()

    for rounds in range(0,6):
        print("Round "+str(rounds))
        winner = rand.randint(0,1)

        if winner == 0:
            print(insectPlayer.get_name()+" is the winner!")
            arachnidPlyer.lose_fight()
            print(arachnidPlyer.get_name()+" now has "+str(arachnidPlyer.get_limbsCount())+" limbs left")
        else:
            print(arachnidPlyer.get_name() + " is the winner!")
            insectPlayer.lose_fight()
            print(insectPlayer.get_name() + " now has " + str(arachnidPlyer.get_limbsCount()) + " limbs and "+str(insectPlayer.get_wings_count())+" wings left")
        print()

if __name__ == '__main__':
    main()