import sys
from random import choice

class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        #methods reads input file and returns contents a string
        word_bucket = ''

        for filename in filenames:
              input_text = open(filename).read()  
              word_bucket = word_bucket + input_text    

        return word_bucket


    def make_chains(self, corpus):
        """Takes input text as string; returns dictionary of markov chains."""

        chains = {}

        words = corpus.split()

        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

            # or we could say "chains.setdefault(key, []).append(value)"
        return chains


    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)
         
        return " ".join(words)

start_markov = SimpleMarkovGenerator()
input_path = sys.argv[1:]
word_bucket = start_markov.read_files(input_path)
chains = start_markov.make_chains(word_bucket)
complete_markov = start_markov.make_text(chains)
print complete_markov
    # Get a Markov chain
#chains = make_chains(self.input_text)

    # Produce random text
    # random_text = make_text(chains)

#print random_text
