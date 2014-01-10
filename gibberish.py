#from nltk.corpus import cmudict
#d = cmudict.dict()
from collections import defaultdict
import random

class CharBasedMarkovChain:

    def __init__(self):
        self.chain = {}
   

    def gen(self, n=50):
        """Using the trained markov chain, generates n number of words
        """
        if not self.chain:
            # raise error?
            return
       
        wordlist = []
        for i in xrange(n):
            key = '#'
            word = '' # string to append to
            while key != '$':
                roll = random.random()
                for c, prob in self.chain[key].items():
                    roll -= prob
                    if roll <= 0:
                        if key == '#':
                            # first one, so add pair
                            word += "".join(c)
                            key = c
                        elif c == '$':
                            key = '$'
                        else:
                            word += c
                            key = (key[1], c)
                        break
            wordlist.append(word)
            word = ''
        
        return wordlist
             
       

    def _flatten_counts(self, counts):
        """Transforms counts into probabilities. Internally used by train.
        """
        probs = defaultdict(lambda : defaultdict(int))
        for key in counts.keys():
            total = float(sum(counts[key].values()))
            for subkey, count in counts[key].items():
                probs[key][subkey] = count/total
        
        return probs

    def train(self, wordlist, order=2):
        """Input: a list of CMU Dictionary phonetic pronunciations
           
           1) creates a dictionary containing all the counts of each syllable following another

           2) transforms those counts into probabilities

        """

        # a dictionary that defaults to containing a dictionary that defaults to 1
        counts = defaultdict(lambda : defaultdict(lambda: 1))
        for entry in wordlist:
            counts['#'][tuple(entry[1:1+order])] += 1
            for i in xrange(1, len(entry)-order):
                counts[tuple(entry[i:i+order])][entry[i+order]] += 1
        self.chain = self._flatten_counts(counts)
        return self.chain

