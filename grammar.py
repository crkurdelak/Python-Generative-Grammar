"""
grammar.py
A program that generates a sentence based on a specified grammar file.
Ceci Kurdelak
ckurdelak20@georgefox.edu
"""

import sys


def main():
    """
    Main function of grammar.py
    """

    grammar_dict = dict()

    # get filename from command line
    filename = sys.argv[1]

    # read file and create grammar
    read_file(filename, grammar_dict)

    # generate the sentence
    sentence = generate_sentence(grammar_dict)
    print(sentence)


def read_file(filename, grammar_dict):
    """
    read_file
    Reads a grammar file.
    :param: filename the filename of the grammar file
    :param: grammar_dict a dictionary to store the information from the file
    """

    grammar_file = open(filename, "r")
    lines = grammar_file.readlines()

    # becomes true once the first "{" is encountered
    is_started = False
    # true if currently parsing a production, else false
    is_in_production = False

    for line in lines:
        print(line)
        # TODO extract data from line

        ## if line starts with "{", is_started = true
        # ignore everything up until the first "{"
        ## if is_started:
            # if line starts with "{", it is the start of a new production
            ## if current line starts with "{":
                ## if is_in_production, throw exception and exit, we do not allow files with nested brackets
                ## else, is_in_production = True

            # this is mutually exclusive because we don't want the "{" added to the dict
            ## else if is_in_production:
                # first line after "{" should be name of production surrounded by "<>"
                ## if next line surrounded in "<>"
                    ## add contents of "<>" to dict as key, with an empty set as its value

                ## else if current line ends with "}"
                    ## is_in_production = false
                # everything between "<>" and "}" should be semicolon-separated list of lexemes, one on each line
                ## else add line as value to current key

        ## if current line is end of file and is_in_production, throw exception and exit, the file is bad


def generate_sentence(grammar_dict):
    """
    Generates a sentence using the given grammar
    :param grammar_dict: a dictionary containing the grammar
    :return: a sentence generated from the grammar
    """
    sentence = "this is a placeholder"

    #  start at grammar_dict(<start>), push it onto stack
    # while stack not empty:
        # go to production given by top of stack
        # choose one randomly

        # while there are words left in chosen production and current word not surrounded by "<>":
            # append word onto sentence
            # next word
        # if current word surrounded by "<>", push to stack
        # else if no words left, pop from stack


    return sentence


main()
