import random
import re
import string
import sys
import cPickle as pickle

def run(filename, split):
    cleanText = openAndClean(filename)

    suff_table = build_suffix_table(cleanText, split, {})
    return suff_table

def openAndClean(filename):
    f = open(filename)
    cleantext = text_clean(f)
    return cleantext

def build_suffix_table(full_text, split, suffix_table):
    prefix = tuple([None] * split)

    sp = re.findall(r"\w+|\S+", full_text)

    for word in sp:
        if prefix in suffix_table:
            suffix_table[prefix] += [word]
        else:
            suffix_table[prefix] = [word]
        prefix = prefix[1:split] + tuple([word])

    save_suffix_table(suffix_table)

    return suffix_table

def load_suffix_table(filename):
    f = open(filename)
    suff_table = pickle.load(f)
    return suff_table

def save_suffix_table(suffix_table):
    pickle.dump(suffix_table, open("training.p", "wb"))
    return

def text_clean(text_file):
    return re.sub(r"<\S+>|\n", "", text_file.read())
