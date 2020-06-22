# COMP0015 Coursework II
# Group S
# Student ID: 17018962
# Student ID: 18036523

"""Semantic Similarity: starter code
"""

import math


def norm(vec):
    """Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 2.
    """

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    """Return the cosine similarity of sparse vectors vec1 and vec2,
    stored as dictionaries as described in the handout for Project 2.
    """

    dot_product = 0.0  # floating point to handle large numbers
    for x in vec1:
        if x in vec2:
            dot_product += vec1[x] * vec2[x]

    # Make sure empty vectors don't cause an error -- return -1 as
    # suggested in the handout for Project 2.
    norm_product = norm(vec1) * norm(vec2)
    if norm_product == 0.0:
        return -1.0
    else:
        return dot_product / norm_product


def get_sentence_lists(text):
    """Return the sentence lists of the text. One list for each sentence.
    Each element is in lower case and without any punctuations and spaces.
    """
    # initialise
    text = text.lower()
    punctuation = [",", "-", "--", ":", ";", "\"", "\'", "\n"]

    # split each sentence
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    sentences = text.split(".")

    # split each word
    for i in range(len(sentences)):
        each_sen = sentences[i]
        for mark in punctuation:
            each_sen = each_sen.replace(mark, " ")
        sentences[i] = each_sen.split(" ")

    # delete empty elements
    i = 0
    while [''] in sentences:
        if sentences[i] == ['']:
            del sentences[i]
        else:
            i = i + 1

    # delete the empty space a element
    for i in range(len(sentences)):
        j = 0
        while '' in sentences[i]:
            if sentences[i][j] == '':
                del sentences[i][j]
            else:
                j = j + 1
    return sentences


def get_sentence_lists_from_files(filenames):
    """Return the list of every sentence contained in all the text files
    in filenames in order. The list have similar format as the previous
    get_sentence_lists() function.
    """
    # creat an empty list
    sentences = []
    for file in filenames:
        f = open(file)
        sentences.append(get_sentence_lists(f.read()))
    # print(sentences)
    return sentences


def build_semantic_descriptors(all_lists):
    """Return a dictionary which represents the semantic descriptor of
    a specified word. The variable contains lists of strings for sentences.
    """

    dic = {}  # creat an empty dictionary
    for sentences in all_lists:
        for sentence in sentences:
            counted = []

            for word in sentence:
                if word in counted:
                    continue

                counted.append(word)
                try:
                    dic[word]
                except KeyError:
                    dic[word] = {}
                for other in sentence:
                    if word != other:
                        try:
                            dic[word][other] += 1
                        except KeyError:
                            dic[word][other] = 1
        # print (d)
    return dic


def most_similar_word(word, choices, semantic_descriptors):
    """Return the element of choices which has the highest semantic similarity
    to the word. The semantic descriptors is calculated from
    build_semantic_descriptor() function. The semantic similarity supposes to
    be -1 if the value between two words cannot be calculated.
    """

    max_c = -1
    max_w = choices[0]
    for choice in choices:
        try:  # obtain the similarity value
            c = cosine_similarity(semantic_descriptors[word],
                                  semantic_descriptors[choice])
        except KeyError:
            c = -1
        if c > max_c:  # choose the answer with the highest value
            max_c = c
            max_w = choice
    # print(max_w)
    return max_w


def run_similarity_test(filename, semantic_descriptors):
    """Return the percentage of most_similar_word(), and guesses the answer
    using the semantic_descriptors. The filename is the file which is tested.
    """

    questions = open(filename)
    correct = 0
    length = 0

    for question in questions:
        length = length + 1
        words = question.split()
        print(words)
        candidates = words[2:]  # predict the best answer
        best = most_similar_word(words[0], candidates, semantic_descriptors)
        if words[1] == best:
            correct = correct + 1
        print('Predicted answer: ' + best)

    percent = float(correct) / float(length) * 100.0  # calculate the percentage
    return percent
