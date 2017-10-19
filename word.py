#import nltk
#nltk.download('wordnet')
from nltk.corpus import wordnet as wn
strn = raw_input("String : ")
wrd = wn.synset(strn+'.n.01')
hyper = lambda s: s.hypernyms()
x = list(wrd.closure(hyper))

for i in x:
  print(i)

#----------------------------------------------------------
#  This Program helps in categories the word inside synset('word1.n.01') 
#
#----------------------------------------------------------