import cPickle as pickle
from wordlist import make_cmu_wordlist
from gibberish import CharBasedMarkovChain
import pprint
import sys

def main():
    wordlist = make_cmu_wordlist()
    markov = CharBasedMarkovChain()
    counts = markov.train(iter(wordlist))
    text = markov.gen(100)

    pprint.pprint(text)

if __name__ == "__main__":
    main()
