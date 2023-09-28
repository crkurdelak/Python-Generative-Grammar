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
    Reads a grammar file and creates a grammar dictionary from it.
    :param filename: the filename of the grammar file
    :param grammar_dict: a dictionary to store the information from the file
    """

    grammar_file = open(filename, "r")
    lines = grammar_file.readlines()

    # becomes true once the first "{" is encountered
    is_started = False
    # true if currently parsing a production, else false
    is_in_production = False
    current_key = ""

    for line in lines:
        print(line)
        # ignore empty lines
        if line[0] != "\n":
            # ignore everything up until the first "{"
            if line[0] == "{" :
                is_started = True
            if is_started:
                # if line starts with "{", it is the start of a new production
                if line[0] == "{":
                    # we do not allow files with nested brackets
                    if is_in_production:
                        raise RuntimeError("Invalid File")
                    else:
                        is_in_production = True

                # this is mutually exclusive because we don't want the "{" added to the dict
                elif is_in_production:
                    # first line after "{" should be name of production surrounded by "<>"
                    # last character of each line is a /n, so check second to last character
                    if line[0] == "<" and line[-2] == ">":
                        # add contents of "<>" to dict as key, with an empty set as its value
                        current_key = line[1:-2]
                        grammar_dict[current_key] = set()

                    # else if current line ends with "}"
                    elif (len(line) == 1 and line[0] == "}") or line[-2] == "}":
                        is_in_production = False
                    # everything between "<>" and "}" should be semicolon-separated list of lexemes, one on each line
                    else:
                        # add line as value to current key
                        grammar_dict[current_key].add(line[0:-2])

    # if is_in_production after iteration is over, throw exception and exit, the file is bad
    if is_in_production:
        raise RuntimeError("Invalid File")


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
