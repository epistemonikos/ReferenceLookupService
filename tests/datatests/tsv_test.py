#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import pprint
import os

"""
This Testing file, make a tsv with four columns, which are:
rating (calculate from crsearch result), crossref's doi, epistemonikos's doi and the original reference.
It was use, for make a graphic, in order to show the correctness of Crossref API.
"""
rrsr = open('./src/random_results_systematic_review')

line = rrsr.readline()
while line:
    sline = line.split('\t')
    try:
        if len(sline) > 1:
            episte_doi = sline[0] or '-'
            reference = ''.join(sline[1:]) or '-'
            x = requests.get('http://0.0.0.0:5001/api/v1/crsearch', params={
                'ref' : reference
            })
            rating = x.json().get('rating', {}).get('total', 0)
            crossRef_doi = x.json().get('ids', {}).get('doi', '-')
            print("%.2f\t%s\t%s\t%s" % (rating, crossRef_doi, episte_doi, reference))
    except:
        pass
    line = rrsr.readline()
