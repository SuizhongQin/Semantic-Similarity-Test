from COMP0015.coursework_2.synonyms import get_sentence_lists, build_semantic_descriptors, most_similar_word, \
    get_sentence_lists_from_files

# test for part a
# test 1
s = "Hello, Jack. How is it going? Not bad; pretty good, actually... Very very good, in fact. "
l = [['hello', 'jack'],
     ['how', 'is', 'it', 'going'],
     ['not', 'bad', 'pretty', 'good', 'actually'],
     ['very', 'very', 'good', 'in', 'fact']]
assert (get_sentence_lists(s)[0] == l[0])
assert (get_sentence_lists(s)[1] == l[1])
assert (get_sentence_lists(s)[2] == l[2])
assert (get_sentence_lists(s)[3] == l[3])

# test 2
s = "The St. Bernard is a friendly dog!"
l = [['the', 'st'], ['bernard', 'is', 'a', 'friendly', 'dog']]
assert (get_sentence_lists(s)[0] == l[0])
assert (get_sentence_lists(s)[1] == l[1])

# test for part b
l = get_sentence_lists_from_files(["mini_test.txt"])
assert (l[0][0] == ['aaa', 'bbb', 'ccc', 'this', 'is', 'a', 'test'])

assert (l[0][1] == ['a', 'mini', 'test', 'for', 'testing', 'the', 'part', 'b'])

# test for part c
sen = get_sentence_lists_from_files(['mini_test_2.txt'])
d = build_semantic_descriptors(sen)
assert (d['man'] == {'i': 3, 'am': 3, 'a': 2, 'sick': 1, 'spiteful': 1, 'an': 1, 'unattractive': 1})
assert (d['liver'] == {'i': 1, 'believe': 1, 'my': 1, 'is': 1, 'diseased': 1})


# test for part d
most_similar_word("cat", ["dog", "cat", "horse"], d)
