"""
grammar.py
A program that generates a sentence based on a specified grammar file.
Ceci Kurdelak
ckurdelak20@georgefox.edu
"""

import sys
import random
import re

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

    # becomes true once the first "{" is encountered
    is_started = False
    # true if currently parsing a production, else false
    is_in_production = False
    current_key = ""

    for line in lines:
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
                        raise RuntimeError("Invalid File: " + line)
                    else:
                        is_in_production = True

                # this is mutually exclusive because we don't want the "{" added to the dict
                elif is_in_production:
                    # if current line ends with "}", it is the end of the production
                    if (len(line) == 1 and line[0] == "}") or line[-2] == "}":
                        is_in_production = False

                    # first line after "{" should be name of production surrounded by "<>"
                    # trim off "/n" character before checking
                    elif is_nonterminal(line[0:-1]):
                        # add contents of "<>" to dict as key, with an empty set as its value
                        # trim off brackets and newline
                        current_key = line[1:-2]
                        grammar_dict[current_key] = list()
                    # everything between "<>" and "}" should be semicolon-separated list of lexemes, one on each line
                    else:
                        # add line as value to current key
                        grammar_dict[current_key].append(line[0:-2])

    # if is_in_production after iteration is over, throw exception and exit, the file is bad
    if is_in_production:
        raise RuntimeError("Invalid File:" + lines[-1])
    grammar_file.close()


def generate_sentence(grammar_dict):
    """
    Generates a sentence using the given grammar
    :param grammar_dict: a dictionary containing the grammar
    :return: a sentence generated from the grammar
    """
    sentence = "this is a placeholder"
    sentence_parts = list()
    # a stack to keep track of which production we are in
    sentence_stack = list()
    # a stack to keep track of where we are in the current production
    word_indices_stack = list()


    #  start at grammar_dict(<start>), push it onto stack
    sentence_stack.append('start')
    # start at 0th word
    word_indices_stack.append([0])
    # individual_words starts out empty
    individual_words = list()
    # while stack not empty:
    while len(sentence_stack) > 0:
        # check if there is already something in individual_words
        if len(word_indices_stack[-1]) > 1:
            # get individual_words from word_indices_stack
            individual_words = word_indices_stack[-1][-1]
        else:
            # go to production given by top of stack, choose a value randomly
            dict_vals = grammar_dict[sentence_stack[-1]]
            chosen_val = random.choice(dict_vals)
            # split into individual words
            individual_words = chosen_val.split(" ")
            # save individual_words on word_indices_stack
            word_indices_stack[-1].append(individual_words)

        # get current index in individual_words from word_indices_stack
        i = word_indices_stack[-1][0]

        # while there are words left in chosen production and current word not surrounded by "<>":
        while i < len(individual_words) and not is_nonterminal(individual_words[i]):
            # append word onto sentence
            sentence_parts.append(individual_words[i])
            print(individual_words[i]) # DEBUG, DELETE LATER!
            # next word
            i += 1
            word_indices_stack[-1][0] = i

        # if current word surrounded by "<>", push to stack
        if i < len(individual_words):
            if is_nonterminal(individual_words[i]):
                # trim the angle brackets before pushing to stack
                if individual_words[i][-1] == ">":
                    trimmed_word = individual_words[i][1:-1]
                else:
                    # handle cases where there is a punctuation mark after
                    trimmed_word = individual_words[i][1:-2]
                    # put the punctuation mark in the right place in the list so it doesn't get thrown away
                    individual_words.insert(i + 1, individual_words[i][-1])

                sentence_stack.append(trimmed_word)
                word_indices_stack.append([0])
            # else if no words left, pop from stack
            else:
                sentence_stack.pop()
                word_indices_stack.pop()
                # increment new top of word_indices_stack
                word_indices_stack[-1][0] += 1
        else:
            sentence_stack.pop()
            word_indices_stack.pop()
            # increment new top of word_indices_stack
            word_indices_stack[-1][0] += 1

    sentence = "".join(sentence_parts)
    return sentence


def is_nonterminal(word):
    """
    Returns True if the given word is a nonterminal symbol, else returns False
    A word is a nonterminal symbol if it starts with "<", ends with ">", and contains no spaces.
    :param word: the word to check
    :return: True if the word is a nonterminal, else returns False
    """
    # must be more than 2 characters, start with "<", end with ">", and contain no spaces
    return len(word) > 2 and (word[0] == "<" and (word[-1] == ">" or word[-2] == ">") and " " not in word)

main()
