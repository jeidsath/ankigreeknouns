# -*- coding: utf-8 -*-

import requests

WIKTIONARY = 'http://en.wiktionary.org/wiki/'

NOUNS_FILE = 'nouns.txt'
NOUNS_REVERSE = 'reverse_nouns.txt'
FIRST_DECL = (['ἡ χώρα', 'ἡ νίκη', 'ἡ φυγή', 'ἡ μοῖρα', 'ἡ γλῶττα',
               'ἡ θάλαττα'] +
              ['ὁ νεανίας', 'ὁ πολίτης', 'ὁ κριτής', 'ὁ Ἀτρείδης'] +
              ['ἡ μνᾶ', 'ἡ συκῆ', 'ὁ Βορρᾶς', 'ὁ Ἑρμῆς'])
SECOND_DECL = (['ὁ ἵππος', 'ὁ ἄνθρωπος', 'ἡ ὁδός', 'τὸ δῶρον'] +
               ['ὁ νοῦς', 'ὁ περίπλους', 'τὸ ὀστοῦν'] +
               ['ὁ νεώς'])
THIRD_DECL = (['ὁ Αἰθίοψ', 'ἡ φλέψ', 'ὁ φύλαξ', 'ἡ φάλαγξ', 'ὁ/ἡ αἴξ',
               'ἡ θρίξ'] +
              ['ὁ θής', 'ἡ ἐλπίς', 'ἡ χάρις', 'ὁ/ἡ ὄρνις', 'ὁ Γίγας',
               'ὁ γέρων'] +
              ['τὸ σῶμα', 'τὸ ἧπαρ', 'τὸ τέρας', 'τὸ κέρας'] +
              ['ὁ θήρ', 'ὁ ῥήτωρ', 'ἡ ῥίς', 'ὁ ἡγεμών', 'ὁ ἀγών', 'ὁ ποιμήν'] +
              ['ὁ πατήρ', 'ἡ μήτηρ', 'ἡ θυγάτηρ', 'ὁ ἀνήρ'] +
              ['ὁ Σωκράτης', 'ὁ Δημοσθένης', 'ἡ τριήρης', 'τὸ γένος',
               'τὸ γέρας'] +
              ['τὸ δέος', 'ὁ Περικλῆς'] +
              ['ἡ αἰδώς'] +
              ['ὁ ἥρως'] +
              ['ἡ πόλις', 'ὁ πῆχυς', 'τὸ ἄστυ', 'ὁ/ἡ σῦς', 'ὁ ἰχθύς'] +
              ['ὁ/ἡ οἶς'] +
              ['ὁ βασιλεύς', 'ἡ γραῦς', 'ἡ ναῦς', 'ὁ/ἡ βοῦς'] +
              ['ἡ πειθώ'])
NOUNS = FIRST_DECL + SECOND_DECL + THIRD_DECL
ARTICLE_MAP = {'m': {'Singular': {'Nominative': u'ὁ',
                                  'Genitive': u'τοῦ',
                                  'Dative': u'τῷ',
                                  'Accusative': u'τὸν',
                                  'Vocative': u'ῶ'},
                     'Dual':     {'Nominative': u'τὼ',
                                  'Genitive': u'τοῖν',
                                  'Dative': u'τοῖν',
                                  'Accusative': u'τὼ',
                                  'Vocative': u'τὼ'},
                     'Plural':   {'Nominative': u'οἱ',
                                  'Genitive': u'τῶν',
                                  'Dative': u'τοῖς',
                                  'Accusative': u'τοὺς',
                                  'Vocative': u'οἱ'}, },
               'f': {'Singular': {'Nominative': u'ἡ',
                                  'Genitive': u'τῆς',
                                  'Dative': u'τῇ',
                                  'Accusative': u'τὴν',
                                  'Vocative': u'ῶ'},
                     'Dual':     {'Nominative': u'τὼ',
                                  'Genitive': u'τοῖν',
                                  'Dative': u'τοῖν',
                                  'Accusative': u'τὼ',
                                  'Vocative': u'τὼ'},
                     'Plural':   {'Nominative': u'αἱ',
                                  'Genitive': u'τῶν',
                                  'Dative': u'ταῖς',
                                  'Accusative': u'τὰς',
                                  'Vocative': u'αἱ'}, },
               'n': {'Singular': {'Nominative': u'τὸ',
                                  'Genitive': u'τοῦ',
                                  'Dative': u'τῷ',
                                  'Accusative': u'τὸ',
                                  'Vocative': u'ῶ'},
                     'Dual':     {'Nominative': u'τὼ',
                                  'Genitive': u'τοῖν',
                                  'Dative': u'τοῖν',
                                  'Accusative': u'τὼ',
                                  'Vocative': u'τὼ'},
                     'Plural':   {'Nominative': u'τὰ',
                                  'Genitive': u'τῶν',
                                  'Dative': u'τοῖς',
                                  'Accusative': u'τὰ',
                                  'Vocative': u'τὰ'}, }}


def get_html_from_wiktionary(word):
    print "Called for " + unicode(word, 'utf-8')
    return requests.get(WIKTIONARY + word.split(' ')[-1]).content


def article_from_gender(gender):
    if gender == 'feminine':
        return u'ἡ'
    if gender == 'masculine':
        return u'ὁ'
    if gender == 'neuter':
        return u'τὸ'


def show_forms(noun, shelf):
    forms = shelf[noun]
    print unicode(repr(forms), 'utf-8')
    for kk in forms.keys():
        print kk
        if kk != 'gender':
            for key, value in forms[kk].iteritems():
                print key, value
        else:
            print forms[kk]
