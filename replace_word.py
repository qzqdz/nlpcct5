from nltk.corpus import wordnet as wn
# import nltk
# nltk.download()
wordnet_vocab = list(wn.all_lemma_names())

similar_string = 'alzheimer'
[word for word in wordnet_vocab if similar_string in word]
#op if exact word is not present,  you can get similar word which are present in wordnet vocab
["alzheimer's", "alzheimer's_disease", 'alzheimers']






