#!/usr/bin/env python

import json
import pickle
import csv
import yaml # pip install pyyaml

# The data is based on the top 5 countries by population
data = {
    'china': {
        'population': 135404000,
        'data_age': '2012-12-31',
        'languages': ['chinise', 'mongolian', 'tibetan', 'uyghur', 'zhuang'],
    },
    'india': {
        'population': 1210569573,
        'data_age': '2011-03-01',
        'languages': ['hindi', 'english'],
    },
    'usa': {
        'population': 316116000,
        'data_age': '2013-06-25',
        'languages': ['english',],
    },
    'indonesia': {
        'population': 237641326,
        'data_age': '2010-05-01',
        'languages': ['indonesian',],
    },
    'brazil': {
        'population': 193946886,
        'data_age': '2012-07-01',
        'languages': ['portoguese',],
    },
}

with open('countryinfo.json', 'w') as fp:
    json.dump(data, fp)

with open('countryinfo.yaml', 'w') as fp:
    yaml.dump(data, fp)

with open('countryinfo.python_pickle', 'w') as fp:
    pickle.dump(data, fp)
