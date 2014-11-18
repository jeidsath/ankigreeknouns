#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import shelve

import ankigreekutil as anki


WIKTIONARY = 'http://en.wiktionary.org/wiki/'
REPRESENTATIONS = {'imperfect': '----    |',
                   'present': '--|--',
                   'future': '|    -\n|    -----',
                   'perfect': '----|',
                   'pluperfect': '----X    |',
                   'aorist': '-   |',
                   'future perfect': '|    ----    X',
                   'indicative': '👉 ',
                   'imperative': '✋ ',
                   'subjunctive': '👇 ',
                   'optative': '👻 ',
                   'first singular': '(👤 )',
                   'second singular': '→ 👤 ',
                   'third singular': '👤 ',
                   'first dual': '(👬 )',
                   'second dual': '→ 👬 ',
                   'third dual': '👬 ',
                   'first plural': '(👪 )',
                   'second plural': '→ 👪 ',
                   'third plural': '👪 ',
                   'infinitive': '∞',
                   'active': '🏃 ',
                   'middle': '🔁 ',
                   'passive': '☔️ '
                   }


class VerbList(object):
    pass


def parse_args():
    parser = argparse.ArgumentParser('Verbs')
    parser.add_argument('--get')
    parser.add_argument('--show')
    parser.add_argument('--anki', action='store_true')
    return parser.parse_args()


def download_and_save(word):
    html = anki.get_html_from_wiktionary(word)


def main():
    args = parse_args()
    if args.get:
        download_and_save(args.get)
    if args.show:
        anki.show_forms(args.show, SHELF)

if __name__ == '__main__':
    global SHELF
    SHELF = shelve.open('verbs.shelf')
    main()
    SHELF.close()
