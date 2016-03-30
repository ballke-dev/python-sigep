# -*- encoding: utf-8 -*-
import re


def clean_postcode(postcode, size=8):
    assert isinstance(postcode, (str, unicode, int)), 'postcode must been an unicode, string or int'

    cleaned_postcode = re.sub("[^0-9]", "", str(postcode))
    cleaned_postcode = cleaned_postcode.rjust(size, '0')

    return cleaned_postcode


def iso_2_utf(text):
    assert isinstance(text, (str, unicode)), 'text must been a string or unicode'

    return text.decode('iso-8859-1').encode('utf8')


def utf_2_iso(text):
    assert isinstance(text, (str, unicode)), 'text must been a string or unicode'

    return text.decode('utf-8').encode('iso-8859-1')
