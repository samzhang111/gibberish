from nltk.corpus import cmudict
import cPickle as pickle

def make_wordlist():
    """
    Add '#' to the start of strings
    Add '$' to the end of strings (for markov chain use).

    Pickle and dump to 'dict.p'.
    """
    with open('wordlists/words.txt', 'r') as wordfile:
        words = wordfile.readlines()
    for i in xrange(len(words)):
        words[i] = '#' + words[i].lower().strip() + '$'
        #Use '$' to mark the end of words

#    with open('wordlists/words_edited.p', 'w') as outfile:
#        pickle.dump(words, outfile)
    
    return words


def make_cmu_wordlist():
    """
    Strip the CMU Pronunciation Dictionary of accent marks.

    Add '$' to the end of strings (for markov chain use).

    Pickle and dump to 'cmu.p'.
    """
    d = cmudict.dict()
    pronunciation_list = d.values()

    edited_list = []
    for entry in pronunciation_list:
        for word in entry:
            edited_word = ["#"]
            for i in xrange(len(word)):
                #remove accent marks
                edited_word.append(word[i].rstrip('0123456789'))
                
            #Use '$' to mark the end of words
            edited_word.append('$')
            edited_list.append(edited_word)

#    with open('wordlists/cmu.p', 'w') as outfile:
#        pickle.dump(edited_list, outfile)
    
    return edited_list

def main():
    make_wordlist()

if __name__ == '__main__':
    main()
