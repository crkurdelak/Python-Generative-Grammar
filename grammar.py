"""
grammar.py
A program that generates a sentence based on a specified grammar file.
Ceci Kurdelak
ckurdelak20@georgefox.edu
"""

import sys
import random

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
    print(generate_sentence(grammar_dict))


def read_file(filename, grammar_dict):
    """
    read_file
    Reads a grammar file and creates a grammar dictionary from it.
    :param filename: the filename of the grammar file
    :param grammar_dict: a dictionary to store the information from the file
    """

    grammar_file = open(filename, "r")
    lines = grammar_file.readlines()

    # TODO handle multiple things on 1 line
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
                    if is_nonterminal(line[0]):
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
    sentence_parts = list()
    sentence_stack = list()

    #  start at grammar_dict(<start>), push it onto stack
    sentence_stack.append('start')
    # while stack not empty:
    while len(sentence_stack) > 0:
        # go to production given by top of stack, choose a value randomly
        chosen_val = random.choice(grammar_dict[sentence_stack[-1]])

        individual_words = chosen_val.split(" ")
        i = 0
        # while there are words left in chosen production and current word not surrounded by "<>":
        while i < len(individual_words) and not is_nonterminal(individual_words[i]):
            # append word onto sentence
            sentence_parts.append(individual_words[i])
            # next word
            i += 1
        # if current word surrounded by "<>", push to stack
        if is_nonterminal(individual_words[i]):
            sentence_stack.append(individual_words[i])
        # else if no words left, pop from stack
        else:
            sentence_stack.pop()

    sentence = "".join(sentence_parts)
    return sentence


def is_nonterminal(word):
    """
    Returns True if the given word is a nonterminal symbol, else returns False
    :param word: the word to check
    :return: True if the word is a nonterminal, else returns False
    """
    # TODO implement
    # must start with "<", end with ">", and contain no spaces

main()
