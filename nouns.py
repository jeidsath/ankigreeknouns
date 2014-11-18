#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve
import argparse
import re
import os

import ankigreekutil as anki


def main():
    args = parse_args()
    if args.get:
        download_and_save(args.get)
    if args.show:
        show_forms(args.show)
    if args.anki:
        prepare_shelf()
        create_noun_files(anki.WORDS)


def prepare_shelf():
    SHELF['ἡ μνᾶ'] = {
        'Singular': {'Nominative': u'μνᾶ',
                     'Genitive': u'μνᾶς',
                     'Dative': u'μνᾷ',
                     'Accusative': u'μνᾶν',
                     'Vocative': u'μνᾶ',
                     },
        'Dual':     {'Nominative': u'μνᾶ',
                     'Genitive': u'μναῖν',
                     'Dative': u'μναῖν',
                     'Accusative': u'μνᾶ',
                     'Vocative': u'μνᾶ',
                     },
        'Plural':   {'Nominative': u'μναῖ',
                     'Genitive': u'μνῶν',
                     'Dative': u'μναῖς',
                     'Accusative': u'μνᾶς',
                     'Vocative': u'μναῖ',
                     }
        }
    SHELF['ἡ συκῆ'] = {
        'Singular': {'Nominative': u'σῡκῆ',
                     'Genitive': u'σῡκῆς',
                     'Dative': u'σῡκῇ',
                     'Accusative': u'σῡκῆν',
                     'Vocative': u'σῡκῆ',
                     },
        'Dual':     {'Nominative': u'σῡκᾶ',
                     'Genitive': u'σῡκαῖν',
                     'Dative': u'σῡκαῖν',
                     'Accusative': u'σῡκᾶ',
                     'Vocative': u'σῡκᾶ',
                     },
        'Plural':   {'Nominative': u'σῡκαῖ',
                     'Genitive': u'σῡκῶν',
                     'Dative': u'σῡκαῖς',
                     'Accusative': u'σῡκᾶς',
                     'Vocative': u'σῡκαῖ',
                     }
        }
    SHELF['ὁ νοῦς'] = {
        'Singular': {'Nominative': u'(νόος) νοῦς',
                     'Genitive': u'(νόου) νοῦ',
                     'Dative': u'(νόῳ) νῷ',
                     'Accusative': u'(νόον) νοῦν',
                     'Vocative': u'(νόε) νοῦ',
                     },
        'Dual':     {'Nominative': u'(νόω) νώ',
                     'Genitive': u'(νόοιν) νοῖν',
                     'Dative': u'(νόοιν) νοῖν',
                     'Accusative': u'(νόω) νώ',
                     'Vocative': u'(νόω) νώ',
                     },
        'Plural':   {'Nominative': u'(νόοι) νοῖ',
                     'Genitive': u'(νόων) νῶν',
                     'Dative': u'(νόοις) νοῖς',
                     'Accusative': u'(νόους) νοῦς',
                     'Vocative': u'(νόοι) νοῖ',
                     }
        }
    SHELF['ὁ περίπλους'] = {
        'Singular': {'Nominative': u'(περίπλοος) περίπλους',
                     'Genitive': u'(περιπλόου) περίπλου',
                     'Dative': u'(περιπλόῳ) περίπλῳ',
                     'Accusative': u'(περίπλοον) περίπλουν',
                     'Vocative': u'(περίπλοε) περίπλου',
                     },
        'Dual':     {'Nominative': u'(περιπλόω) περίπλω',
                     'Genitive': u'(περιπλόοιν) περίπλοιν',
                     'Dative': u'(περιπλόοιν) περίπλοιν',
                     'Accusative': u'(περιπλόω) περίπλω',
                     'Vocative': u'(περιπλόω) περίπλω',
                     },
        'Plural':   {'Nominative': u'(περίπλοοι) περίπλοι',
                     'Genitive': u'(περιπλόων) περίπλων',
                     'Dative': u'(περιπλόοις) περίπλοις',
                     'Accusative': u'(περιπλόους) περίπλοις',
                     'Vocative': u'(περίπλοοι) περίπλοι',
                     }
        }
    SHELF['ἡ μήτηρ'] = {
        'Singular': {'Nominative': u'μήτηρ',
                     'Genitive': u'μήτρός',
                     'Dative': u'μητρί',
                     'Accusative': u'μητέρα',
                     'Vocative': u'μῆτερ',
                     },
        'Dual':     {'Nominative': u'μητέρε',
                     'Genitive': u'μητέροιν',
                     'Dative': u'μητέροιν',
                     'Accusative': u'μητέρε',
                     'Vocative': u'μητέρε',
                     },
        'Plural':   {'Nominative': u'μητέρες',
                     'Genitive': u'μητέραν',
                     'Dative': u'μητράσι(ν)',
                     'Accusative': u'μητέρας',
                     'Vocative': u'μητέρες',
                     }
        }
    SHELF['ὁ Σωκράτης'] = {
        'Singular': {'Nominative': u'Σωκράτης',
                     'Genitive': u'(Σωκράτεος) Σωκράτους',
                     'Dative': u'(Σωκράτει) Σωκράτει',
                     'Accusative': u'(Σωκράτεα) Σωκράτη',
                     'Vocative': u'Σώκρατες',
                     }
        }
    SHELF['ἡ τριήρης'] = {
        'Singular': {'Nominative': u'τριήρης',
                     'Genitive': u'(τριήρεος) τριήρους',
                     'Dative': u'(τριήρει) τριήρει',
                     'Accusative': u'(τριήρεα) τριήρη',
                     'Vocative': u'τριῆρες',
                     },
        'Dual':     {'Nominative': u'(τριήρεε) τριήρει',
                     'Genitive': u'(τριηρέοιν) τριήροιν',
                     'Dative': u'(τριηρέοιν) τριήροιν',
                     'Accusative': u'(τριήρεε) τριήρει',
                     'Vocative': u'(τριήρεε) τριήρει',
                     },
        'Plural':   {'Nominative': u'(τριήρεες) τριήρεις',
                     'Genitive': u'(τριηρέων) τριήρων',
                     'Dative': u'(τριήρεσσι) τριήρεσι(ν)',
                     'Accusative': u'τριήρεις',
                     'Vocative': u'(τριήρεες) τριήρεις',
                     }
        }
    SHELF['τὸ γέρας'] = {
        'Singular': {'Nominative': u'γέρας',
                     'Genitive': u'(γέραος) γέρως',
                     'Dative': u'(γέραι) γέραι',
                     'Accusative': u'γέρας',
                     'Vocative': u'γέρας',
                     },
        'Dual':     {'Nominative': u'(γέραε) γέρᾱ',
                     'Genitive': u'(γεράοιν) γερῷν',
                     'Dative': u'(γεράοιν) γερῷν',
                     'Accusative': u'(γέραε) γέρᾱ',
                     'Vocative': u'(γέραε) γέρᾱ',
                     },
        'Plural':   {'Nominative': u'(γέραα) γέρᾱ',
                     'Genitive': u'(γεράων) γερῶν',
                     'Dative': u'(γέρασσι) γέρασι(ν)',
                     'Accusative': u'(γέραα) γέρᾱ',
                     'Vocative': u'(γέραα) γέρᾱ',
                     }
        }
    SHELF['τὸ δέος'] = {
        'Singular': {'Nominative': u'δέος',
                     'Genitive': u'(δέεος) δέους',
                     'Dative': u'(δέει) δέει',
                     'Accusative': u'δέος',
                     'Vocative': u'δέος',
                     }
        }
    SHELF['ἡ αἰδώς'] = {
        'Singular': {'Nominative': u'αἰδώς',
                     'Genitive': u'(αἰδόος) αἰδοῦς',
                     'Dative': u'(αἰδόι) αἰδοῖ',
                     'Accusative': u'(αἰδόα) αἰδῶ',
                     'Vocative': u'αἰδώς',
                     }
        }
    SHELF['τὸ ἄστυ'] = {
        'Singular': {'Nominative': u'ἄστυ',
                     'Genitive': u'ἄστεως',
                     'Dative': u'ἄστει',
                     'Accusative': u'ἄστυ',
                     'Vocative': u'ἄστυ',
                     },
        'Dual':     {'Nominative': u'ἄστει',
                     'Genitive': u'ἀστέοιν',
                     'Dative': u'ἀστέοιν',
                     'Accusative': u'ἄστει',
                     'Vocative': u'ἄστει',
                     },
        'Plural':   {'Nominative': u'ἄστη',
                     'Genitive': u'ἄστεων',
                     'Dative': u'ἄστεσι(ν)',
                     'Accusative': u'ἄστη',
                     'Vocative': u'ἄστη',
                     }
        }
    SHELF['ἡ γραῦς'] = {
        'Singular': {'Nominative': u'γραῦς',
                     'Genitive': u'γρᾱός',
                     'Dative': u'γρᾱῑ́',
                     'Accusative': u'γραῦν',
                     'Vocative': u'γραῦ',
                     },
        'Dual':     {'Nominative': u'γρᾶε',
                     'Genitive': u'γρᾱοῖν',
                     'Dative': u'γρᾱοῖν',
                     'Accusative': u'γρᾶε',
                     'Vocative': u'γρᾶε',
                     },
        'Plural':   {'Nominative': u'γρᾶες',
                     'Genitive': u'γρᾱῶν',
                     'Dative': u'γραυσί(ν)',
                     'Accusative': u'γραῦς',
                     'Vocative': u'γρᾶες',
                     }
        }


def download_and_save(word):
    html = anki.get_html_from_wiktionary(word)
    forms = get_noun_forms(html)
    save_forms(word, forms)


def create_noun_files(words):
    try:
        os.unlink(anki.NOUNS_FILE)
    except OSError:
        pass
    try:
        os.unlink(anki.NOUNS_REVERSE)
    except OSError:
        pass
    for word in words:
        output_word_defs(word)


def output_word_defs(word):
    try:
        if not SHELF.get(word):
            download_and_save(word)
    except:
        print (u"Bad defintion for " + unicode(word, 'utf-8')).encode('utf-8')
        return

    # article = article_from_gender(SHELF[word]['gender'])
    # nom_sing = SHELF[word]['Singular']['Nominative']
    # dict_form = article + ' ' + nom_sing
    # unfortunately the dictionary is not regular
    dict_form = unicode(word, 'utf-8')

    cases = ['Singular', 'Plural', 'Dual']
    defs = {}
    if not SHELF[word].get('Singular'):
        print (u"Bad defintion for " + unicode(word, 'utf-8')).encode('utf-8')
    for case in cases:
        if not SHELF[word].get(case):
            continue
        for decl, form in SHELF[word][case].iteritems():
            article = article_for_word(word, case, decl)
            for ff in min_form(clean_form(form)):
                if not defs.get(ff):
                    defs[ff] = []
                defs[ff].append([case, decl])
            ss = dict_form + "<br>" + article + " ________; "
            answers = min_form(clean_form(form))
            answers = map(lambda xx: article + ' ' + xx, answers)
            ss += "<br>".join(answers)

            if not ignore_cases(article, case, decl):
                with open(anki.NOUNS_REVERSE, 'a') as ff:
                    ff.write(ss.encode('utf-8') + "\n")

    # forward
    for form in defs.keys():
        articles = set()
        for case, decl in defs[form]:
            articles.add(article_for_word(word, case, decl))
        ss = form + '; '
        for article in articles:
            ss += article + ' ' + form + '<br>'
        ss += '<br>' + dict_form
        with open(anki.NOUNS_FILE, 'a') as ff:
            ff.write(ss.encode('utf-8') + "\n")


def ignore_cases(article, case, decl):
    article = article.split('/')[0]
    noms = [u'τὼ', u'τὸ', u'τὰ', u'οἱ', u'αἱ']
    if article in noms:
        if decl != 'Nominative':
            return True
    if article == u'τοῖν':
        if decl != 'Genitive':
            return True
    return False


def min_form(form):
    forms = form.split(' ')
    forms = filter(lambda xx: xx != '/', forms)
    forms = filter(lambda xx: xx != '(late)', forms)
    forms = map(remove_parens, forms)

    output = []
    for form in forms:
        output += replace_movable_n(form)

    return output


def replace_movable_n(form):
    if len(form) > 3 and form[-3] == u'(' and form[-2] == u'ν' and form[-1] == u')':
        return [form[0:-3], form[0:-3] + u'ν']
    return [form]


def remove_parens(word):
    if word[0] == '(' and word[-1] == ')':
        return word[1:-1]
    return word


def article_for_word(word, case, decl):
    word_article = unicode(word.split(' ')[0], 'utf-8')
    if word_article == u'ὁ':
        gender = 'm'
    elif word_article == u'ἡ':
        gender = 'f'
    elif word_article == u'τὸ':
        gender = 'n'
    elif word_article == u'ὁ/ἡ':
        gender = 'm/f'
    else:
        print word
        raise Exception('Could not find article')

    if gender == 'm/f':
        first = anki.ARTICLE_MAP['m'][case][decl]
        second = anki.ARTICLE_MAP['f'][case][decl]
        return first + '/' + second

    return anki.ARTICLE_MAP[gender][case][decl]


def clean_form(form):
    articles = [u'οἱ', u'τοὺς', u'τοῖς', u'τοῦ', u'τὸν', u'τῷ', u'τοῖν',
                u'τῶν', u'τὼ', u'ὁ', u'ὁ/ἡ', u'οἱ/αἱ', u'τῷ/τῇ', u'τὸν/τὴν',
                u'τοῦ/τῆς', u'τοὺς/τὰς', u'τοῖς/ταῖς']
    split = form.split(' ')
    if len(split) == 2 and split[0] in articles:
        return split[1]
    return form


def parse_args():
    parser = argparse.ArgumentParser('Nouns')
    parser.add_argument('--get')
    parser.add_argument('--show')
    parser.add_argument('--anki', action='store_true')
    return parser.parse_args()


def get_noun_forms(html):
    # Go through lines until table.*inflection-table
    # Grab the headers for the first tr (Sing, Dual, Plur)
    # Grab the header of the next tr (Nom, or Gen, etc.)
    # Grab the td values, setting map['singular']['nominative'] etc.

    headers = []

    gender = None

    inflection_table = False
    first_tr = False
    data_trs = False

    data_header = None
    data_group = 0

    table_done = False

    forms = {}

    for line in html.split('\n'):

        if not gender:
            gen_re = r'^.*<abbr title="(.*) gender">.</abbr>.*$'
            gender_match = re.match(gen_re, line)
            if gender_match:
                gender = gender_match.group(1)
                forms['gender'] = gender

        if table_done:
            continue

        if not inflection_table:
            if re.match(r'^.*table.*inflection-table.*$', line):
                inflection_table = True
                first_tr = True
            continue
        if re.match(r'^.*</table>.*', line):
            table_done = True

        if first_tr:
            if re.match(r'^.*</tr>.*', line):
                first_tr = False
                data_trs = True
            header_match = re.match(r'^.*<th.*?>(.*)</th>.*$', line)
            if header_match:
                header = header_match.group(1)
                header = re.sub(r'<.*?>', '', header)
                headers.append(header)

        if data_trs:
            header_match = re.match(r'^.*<th.*?>(.*)</th>.*$', line)
            if header_match:
                header = header_match.group(1)
                header = re.sub(r'<.*?>', '', header)
                data_header = header
                data_group = 0
            data_match = re.match(r'^.*<td.*<a.*>(.*)</a>.*</td>.*$', line)
            if data_match:
                word = data_match.group(1)
                data_group += 1
                header = headers[data_group]
                if not forms.get(header):
                    forms[header] = {}
                forms[header][data_header] = unicode(word, 'utf-8')
            data_match2 = re.match(r'^.*<td.*<spa.*>(.*)</span></td>.*$', line)
            if not data_match and data_match2:
                word = data_match2.group(1)
                data_group += 1
                header = headers[data_group]
                if not forms.get(header):
                    forms[header] = {}
                forms[header][data_header] = unicode(word, 'utf-8')

    return forms


def save_forms(noun, forms):
    SHELF[noun] = forms


def show_forms(noun):
    forms = SHELF[noun]
    print unicode(repr(forms), 'utf-8')
    for kk in forms.keys():
        print kk
        if kk != 'gender':
            for key, value in forms[kk].iteritems():
                print key, value
        else:
            print forms[kk]


if __name__ == '__main__':
    global SHELF
    SHELF = shelve.open('nouns.shelf')
    main()
    SHELF.close()
