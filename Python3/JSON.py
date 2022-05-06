#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def read_response(response):
  dump=json.dumps(response, indent=4) # Contain "good presentation" of response
  datas=json.loads(dump) #Store information in dictionnary
  
  #Reading each value on dictionnary
  for key in datas:
    	print("key : %s, value: %s" % (key,datas[key]))
  #print(datas['toto']) => Show values of the key 'toto'
  #print(datas['toto'][0]) => Show 1rst table on the key 'toto'
  #print(datas['toto'][0]['titre'] => Show the value of the 1rst table on the key 'toto'
  
  return datas
