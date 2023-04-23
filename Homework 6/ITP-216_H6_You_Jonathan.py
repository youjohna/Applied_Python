# Jonathan You, youjohna@usc.edu
# ITP 216, Spring 2023
# Section: Tuesday 7pm
# Homework 6
# Description:
#  The purpose of this program is use data from a csv of all of Robert Deniro's movies up until 2016
#  to calculate the average Robert Deniro movie score, and then use it to generate a list of all the
#  movies which were rated above average. Multiple functions were created in this program

def file_reader(fileName):
    """
    a. Description: Retrieves the entire contents of a text file.
    b. Parameters: 1
        i. File name (string)
    c. Returns: 2
        i. The header from the file (list)
        ii. All the rest of data from the file (list)
    """

    f_in = open(fileName, 'r')      # opens the file for reading
    title = []                      # creating an empty list for the title and another for the rest of the content
    contents = []
    counter = 0
    for line in f_in:               # goes through each line of the csv and distributes accordingly
        if counter == 0:
            title.append(line.strip())  # split() gets rid of new line
        else:
            line = line.strip().split(',')
            contents.append(line)
        counter += 1
    return title, contents


    # f_in = open(fileName, 'r')  # opens the file for reading
    # title = []  # creating an empty list for the title and another for the rest of the content
    # contents = []
    # counter = 0




def calculate_mean(intList):
    """
    a. Description: calculates the average value of a collection of values.
    b. Parameters: 1
        i. A collection of integers (list)
    c. Returns: 1
        i. The mean score (float)
    """
    total = 0
    for index in intList:               # goes through each index and adds the value to the total sum
        total = total + int(index)
    return total/len(intList)           # divides by total to find average

def find_movies_above_score(movieList, average):
    """
    a. Description: from an initial list, retrieves a list of all the movies with scores above a certain value.
    b. Parameters: 2
        i. A collection of movies (list)
        ii. A score (float)
    c. Returns: 1
        i. A collection of all movies - in the format of [year, score, title] - with a score above the given score (list)
    """
    targetList = []
    for indexes in movieList:               # goes through each movie line in the provided list
        if float(indexes[1]) > average:     # checks to see if the movie's score is better than average
            targetList.append(indexes)      # if so, the line is added to a list
    return targetList


def main():
    """
    a. Description: Primary entrypoint to your codebase.
    b. Parameters: 0
    c. Returns: 0
    d. Loads the contents of the file into two variables, and then analyzes that data and presents the results on the console.
    """
    print("I love Robert Deniro!")
    file_title, file_contents = file_reader('deniro')   # implements the first function

    intList = []
    for index in file_contents:
        intList.append(index[1])                        # creates a new list of just the scores
    average = calculate_mean(intList)                   # implements the second function
    print('The average Rotten Tomatoes score for his movies is', average)

    newList = find_movies_above_score(file_contents, average)       # implements the third function
    print("Of", len(file_contents), "movies,", len(newList), "are above average")
    print("Here they are")
    for listLine in newList:                            # goes through each line and prints out the info (date, score, title)
        print("\t",listLine[0],"",listLine[1],"",listLine[2])

if __name__ == '__main__':
    main()