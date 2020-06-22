import synonyms as syn

# Use the two novels to build semantic descriptors dictionary,
# and to predict answers of test.txt. Show the accuracy finally.
novels = ["wp.txt", "swan_final.txt"]
novel_sent_lists = syn.get_sentence_lists_from_files(novels)
descriptors = syn.build_semantic_descriptors(novel_sent_lists)
print(syn.run_similarity_test("test.txt", descriptors))
