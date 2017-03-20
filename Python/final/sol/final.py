from pprint import pprint
# from optparse import OptionParser
from enum import Enum
import random
import urllib
import urllib.request
import pickle
import logging
import graph
import collections
import types
import sys
import argparse


class RandomWriter(object):
    """A Markov chain based random data generator."""
    def __init__(self, level=1, tokenization=None):
        self.model = graph.MarkovChainGraph()
        self.level = level
        self.token = tokenization

    def generate(self):
        """Generate tokens using the model."""
        node = self.generate_random()

        while True:
            yield node.state[-1]
            if len(node.next_states) != 0:
                node = node.get_next_state()
                if node == None:
                    node = self.generate_random()
                    while len(node.next_states) == 0:
                        node = self.generate_random()
            else:
                node = self.generate_random()
                while len(node.next_states) == 0:
                    node = self.generate_random()

    def generate_random(self):
        ls =[]
        for key in self.model.state_dict.keys():
            ls.append(key)
        return self.model.state_dict[random.choice(ls)]


    def generate_file(self, filename, amount):
        """Write a file using the model.

        Make sure to open the file in the appropriate mode.
        """
        with open(filename, "w", encoding="utf-8") as fi:
            count = 0

            if self.token is Tokenization.byte or self.token is Tokenization.character:
                space = ""
            else:
                space = " "
            for generate_token in self.generate():
                count += 1
                outputStr = str(generate_token)
                outputStr += space
                fi.write(outputStr)
                if count >= amount:
                    break


    def save_pickle(self, filename_or_file_object):

        if hasattr(filename_or_file_object, 'read'):
            fi = filename_or_file_object
        else:
            fi = open(filename_or_file_object, 'wb')
        pickle.dump(self.model.state_dict, fi)
        fi.close()

    @classmethod
    def load_pickle(cls, filename_or_file_object):
        """Load a Python pickle and make sure it is in fact a model."""

        if hasattr(filename_or_file_object, 'read'):
            fi = filename_or_file_object
        else:
            fi = open(filename_or_file_object, 'r+b')
        rw_instance = RandomWriter()
        rw_instance.model.state_dict = pickle.load(fi)
        fi.close()
        return rw_instance

    def train_url(self, url):
        """Compute the probabilities based on the data downloaded from url.
        This method is only supported if the tokenization mode is not
        none.
        Training is not supported on models loaded form text files.
        """

        if self.token != Tokenization.none:
            data = urllib.request.urlopen(url)
            if self.token == Tokenization.byte:
                data_input = data.read() 
            else:
                data_input = data.read().decode("utf-8")
            self.train_iterable(data_input)

    def train_iterable(self, data):
        """Compute the probabilities based on the data given.
        Training is not supported on models loaded form text files.
        """

        if not isinstance(data, types.GeneratorType):
            if self.token == Tokenization.character:
                if type(data) != str:
                    raise TypeError
            elif self.token == Tokenization.word:
                if type(data) != str:
                    raise TypeError
                else:
                    data = tuple(data.split())
            elif self.token == Tokenization.byte:
                if type(data) != bytes:
                    raise TypeError
            else:
                if not isinstance(data, collections.Iterable):
                    raise TypeError
        # try:
        #     tokens = {}
        #     for i,j in self.windowed(data, self.level):
        #         token = tuple(i)
        #         if not token in tokens:
        #             tokens[token] = {}
        #         follower = (j,)
        #         if follower[0] != None:
        #             tokens[token][follower] = tokens[token][follower] + 1 if follower in tokens[token] else 1
        #     if len(tokens) == 1:
        #         raise Exception("The data is too short, should have provided more than {} elements".format(self.level))
        # except Exception:
        #     raise Exception("There is an error occurs while loading trainingdata")

        # autoCounter = 1
        # for token in tokens:
        #     self.model.add_node(autoCounter, token)
        #     autoCounter += 1
        # for token, followers in tokens.items():
        #     if len(followers)>0:
        #         weight = float(sum((count for follower, count in followers.items())))
        #         for follower, count in followers.items():
        #             next_state_token = token[1:] + follower

        #             for item in self.model.state_dict.values():
        #                 if item.state == next_state_token:
        #                     next_state_token_ID = item.value
        #                     break
        #             for item in self.model.state_dict.values():
        #                 if item.state == token:
        #                     current_token_ID = item.value
        #                     break

        #             if next_state_token_ID in self.model.state_dict:
        #                 next_state_node = self.model[next_state_token_ID]
        #                 self.model[current_token_ID].set_next_state(next_state_node, count/weight)


    # def windowed(self, iterable, size):
    #     window = list()
    #     for v in iterable:
    #         if len(window) < size+1:
    #             window.append(v)
    #         else:
    #             window.pop(0)
    #             window.append(v)
    #         if len(window) == size+1:
    #             yield window[:-1], window[-1]
    #     yield (window[1:], None)


class Tokenization(Enum):
    word = 1
    character = 2
    byte = 3
    none = 4




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--train", help = "train the iterator", action="store_true")
    parser.add_argument("--input", help = "The input file to train on", action="store_true", default=sys.stdin)
    parser.add_argument("--output", help = "The input file to train on", action="store_true", default=sys.stdout)
    parser.add_argument("--word", help = "Use word tokenization", action="store_true")
    parser.add_argument("--character", help = "Use character tokenization", action="store_true")
    parser.add_argument("--byte", help = "Use byte tokenization", action="store_true")
    parser.add_argument("--level", help = "Train or level n", default=1, action="store_true")
    parser.add_argument("--generate", help = "generate an output", action="store_true")
    parser.add_argument("--amount", help = "Generate n tokens", action="store_true")
    args = vars(parser.parse_args())

    for x,y in args.items():
        print(x,y)

    rw = RandomWriter(1, Tokenization.word)

    if args['train']:
        if parser['input']:
            if parser['character']:
                token = parser.character
            elif parser['byte']:
                token = parser.byte
            else:
                token = parser.word
            if not parser['level']:
                raise parser.error("Need a level")
            parser.train_url(parser.input)
        if parser['output']:
            parser.save_pickle(parser.output)
    if parser['generate']:
        if not parser['amount']:
            raise parser.error("Need an amount")
        if parser['input']:
            print("I Tried my best :/")
