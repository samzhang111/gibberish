import cPickle as pickle
from wordlist import make_wordlist, make_cmu_wordlist
from gibberish import CharBasedMarkovChain
import pprint
import sys

def usage():
    print """Usage:
English dictionary: test.py 0
Pronunciation dictionary: test.py 1
"""

def main():
    tests = {
            0: "words_edited.p",
            1: "cmu.p"
            }

    test = -1

    if len(sys.argv) != 2:
        usage()
        return
    if sys.argv[1] == "0":
        test = 0
    elif sys.argv[1] == "1":
        test = 1
    else:
        usage()
        return
#     try:
#         with open("tmp/" + tests[test], "r") as f:
#             wordlist = pickle.load(f)
#         print "Reading wordlist from pickle file..."
#     except IOError:
#         print "No wordlist, generating new one..."

    if test == 0:
        wordlist = make_wordlist()
    else:
        wordlist = make_cmu_wordlist()

    markov = CharBasedMarkovChain()
    counts = markov.train(iter(wordlist))
    text = markov.gen(100)

    pprint.pprint(text)

if __name__ == "__main__":
    main()
