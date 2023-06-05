from moviedb import movieDatabase

COMMAND = 0
TITLE = 1
YEAR = 2
REVIEW = 3

NEW_COMMAND = 'NEW'
REVIEW_COMMAND = 'REV'
SHOW_COMMAND = 'SHO'
PRINT_COMMAND = 'PRI'


def readFile(input):
    """
    :param input: the file input
    :return: the long review
    """
    databaseFinal = movieDatabase()

    with open(input, 'r') as fh:
        for line in fh:
            data = line.strip().split('-')

            command = data[COMMAND]

            if command == NEW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                # try and except to see any KeyError and store the title and year
                try:
                    databaseFinal.addMovie(title, year)
                except KeyError:
                    pass

            elif command == REVIEW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                ReviewFinal = int(data[REVIEW])
                # create variable to check if it exists and use findMovie
                ExistMovie = databaseFinal.findMovie(title, year)

                if ExistMovie is not None:
                    ExistMovie.addReview(ReviewFinal)

            elif command == SHOW_COMMAND:
                databaseFinal.showAll()

            elif command == PRINT_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                ExistMovie = databaseFinal.findMovie(title, year)
                # print long review if its already not printed
                if ExistMovie is not None:
                    print(ExistMovie.longReview())


def main():
    file_input = (input("Enter the name of the file: "))
    readFile(file_input)


main()
