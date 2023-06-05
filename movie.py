# Rubaisha Aslam
# this program would simulate a movie reviewing system
# we will create classes, functions, if statements and for loops to create this program

class Movie:
    def __init__(self, title, year):
        self.__title = title
        self.__year = year
        self.__addedReview = []

    def addReview(self, review):
        """
        check if its an integer or not and if its from 1 to 5 if it is append to the empty list
        :param review:
        :return: the list with reviews
        """
        if isinstance(review, int):
            if 5 >= review >= 1:
                self.__addedReview.append(review)
            else:
                pass

    def shortReview(self):
        """
        create short review by taking the sum of the list and dividing by the length
        :return: short review
        """
        average = self.__calcAverage()
        return '{} ({}): {}/5'.format(self.__title, self.__year, average)

    def longReview(self):
        """
        do nested loop to add to the value of the star
        later print it as a format
        :return: the long review
        """
        average = self.__calcAverage()
        one = 0
        two = 0
        three = 0
        four = 0
        five = 0
        for checkReview in self.__addedReview:
            if 1 == checkReview:
                one = one + 1
            elif 2 == checkReview:
                two = two + 1
            elif 3 == checkReview:
                three = three + 1
            elif 4 == checkReview:
                four = four + 1
            elif 5 == checkReview:
                five = five + 1
        # format it like they asked us
        return "{} ({}) \nAverage review: {}/5\n*****: {}\n**** : {}\n***  : {}\n**   : {}\n*    : {}".format(
            self.__title, self.__year, average, five, four, three, two, one)

    def getTitle(self):
        """
        :return: Movie Title
        """
        return self.__title

    def getYear(self):
        """
        :return: Movie Year
        """
        return self.__year

    def __calcAverage(self):
        """
        calculate the average and gives with one decimal place
        :return: the average of the review
        """
        if len(self.__addedReview) > 0:
            # calculates the average first and than round it to one decimal place
            sumAndDivide = round((sum(self.__addedReview)) / (len(self.__addedReview)), 1)
        else:
            # if there is no review (less than 1 or equal to zero) return 0.0
            sumAndDivide = 0.0
        return sumAndDivide
