#!/usr/bin/env python

import argparse
import csv
import random


def make_pw(add_number=True, add_symbol=True):
    rnd = random.SystemRandom()
    with open('verbs.txt') as verbfile:
        reader = csv.reader(verbfile, delimiter=',')
        verblist = [i for row in reader for i in row]
    with open('nouns.txt') as nounfile:
        reader = csv.reader(nounfile, delimiter=',')
        nounlist = [i for row in reader for i in row]
    final_pw = []
    odd = True  # alternate verbs + nouns
    nouns = rnd.sample(nounlist, 100)
    verbs = rnd.sample(verblist, 100)
    while len(final_pw) < 3:
        if odd:
            # noun
            try:
                noun = nouns.pop()
                while len(noun) < 4 or len(noun) > 8:
                    noun = nouns.pop()
                final_pw.append(noun.title())
            except IndexError:
                nouns = rnd.sample(nounlist, 100)
                continue
            odd = False
        else:
            # verb
            try:
                verb = verbs.pop()
                while len(verb) < 4 or len(verb) > 8:
                    verb = verbs.pop()
                final_pw.append(verb.lower())
            except IndexError:
                verbs = rnd.sample(verblist, 100)
                continue
            odd = True
    if add_number:
        final_pw.insert(2, str(rnd.choice(range(13, 99))))
    final_pw = ' '.join(final_pw)
    if add_symbol:
        final_pw += str(rnd.choice('#!+.-=%$'))
    return final_pw


parser = argparse.ArgumentParser("passgen")
parser.add_argument("passwords", nargs="?", help="Number of passwords to generate.", type=int, default=1)
parser.add_argument("number", nargs="?", help="Add number to password.", type=bool, default=1)
parser.add_argument("symbol", nargs="?", help="Add symbol to password.", type=bool, default=1)
args = parser.parse_args()

for _ in range(args.passwords):
    print(make_pw(args.number, args.symbol))
