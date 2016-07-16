import random
import re
import string
import sys
import argparse

import training

def main():
    parser = argparse.ArgumentParser(description='Generate some fanfic.')

    parser.add_argument("-f", "--file", type=str,
                        help="Pass an existing pickle file with suffix_table")
    parser.add_argument("-s", "--split", type=int, default=2,
                        help="Pass number of splits into suffix table")
    parser.add_argument("-m", "--minlen", type=int, default=40,
                        help="Minimum number of words to print")
    parser.add_argument("-p", "--permatable", dest='savetable', action='store_const',
                        const=True, default=False,
                        help="Save the suffix table generated")
    parser.add_argument("-o", "--output", type=str,
                        help="Output filename")
    parser.add_argument("--retrain", type=str,
                        help="Provide another text to train. If no -f then will simply start new")
    args = parser.parse_args()

    if args.file == None:
        suff_table = training.run('training/The Ultimate Betrayal - MCRasengan.txt', args.split)
    else:
        suff_table = training.load_suffix_table(args.file)

    if args.retrain != None:
        suff_table = training.build_suffix_table(training.openAndClean(args.retrain), args.split, suff_table)

    if args.savetable:
        training.save_suffix_table(suff_table)

    t = textgen(suff_table, args.split, args.minlen)

    if args.output != None:
        out = open(args.output, "w")
        out.write(t)

    print t

    return

def textgen(suffix_table, split, minlen):
    capitals = [suff for suff in suffix_table.keys() if suff[0] != None and suff[0].isupper()]
    prefix = random.choice(capitals)
    prefixprelim = prefix

    buffer = list(prefix)
    start_word = random.choice(suffix_table[prefix])

    # print "Starting with: " + start_word
    # print suffix_table

    len = 0
    while len < minlen or buffer[-1] != ".":
        len = len + 1
        buffer += [start_word]
        # print start_word

        prefixprelim = prefix[1:split] + tuple([start_word])

        while not suffix_table.has_key(prefixprelim):
            start_word = random.choice(suffix_table[prefix])
            prefixprelim = prefix[1:split] + tuple([start_word])

        prefix = prefixprelim
        start_word = random.choice(suffix_table[prefix])

    return ''.join([('' if c in string.punctuation else ' ')+c for c in buffer])

if __name__ == '__main__':
    main()
