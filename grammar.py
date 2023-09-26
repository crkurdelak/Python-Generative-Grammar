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
    read_file(filename, grammar_dict)

    # generate the sentence
    # start at start symbol
    # use a stack


def read_file(filename, grammar_dict):
    """
    read_file
    Reads a grammar file.
    :param: filename the filename of the grammar file
    :param: grammar_dict a dictionary to store the information from the file
    """

    grammar_file = open(filename, "r")
    lines = grammar_file.readlines()
    for line in lines:
        print(line)
        # TODO extract data from line


def generate_sentence(grammar_dict):
    """
    Generates a sentence using the given grammar
    :param grammar_dict: a dictionary containing the grammar
    :return: a sentence generated from the grammar
    """
    return "this is a placeholder"


main()
