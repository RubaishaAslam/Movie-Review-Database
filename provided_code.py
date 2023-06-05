
COMMAND=0
TITLE=1
YEAR=2
REVIEW=3

NEW_COMMAND = 'NEW'
REVIEW_COMMAND = 'REV'
SHOW_COMMAND = 'SHO'
PRINT_COMMAND = 'PRI'


def readFile(input):

    # SOME CODE MAY NEED TO GO HERE

    with open(input,'r') as fh:
        for line in fh:
            data = line.strip().split('-')

            command = data[COMMAND]

            if command == NEW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]

                # YOUR CODE FOR PROCESSING NEW COMMANDS

            elif command == REVIEW_COMMAND:
                title = data[TITLE]
                year = data[YEAR]

                # YOUR CODE FOR PROCESSING REV COMMANDS

            elif command == SHOW_COMMAND:
                # YOUR CODE FOR PROCESSING SHO COMMANDS

            elif command == PRINT_COMMAND:
                title = data[TITLE]
                year = data[YEAR]
                # YOUR CODE FOR PROCESSING PRI COMMANDS
