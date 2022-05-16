#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
This script regroup all the function usefull for "play" with TheHive in CLI.
Modules used:
- thehive4py
- json
- requests
- __future__
"""
from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTemplate
from thehive4py.exceptions import CaseTemplateException

#Search if the template's name entered by the user exists in the instance
def check_template(url,key):
	api= TheHiveApi(url,key)
	name=input("What is the name of the template ?: ")
	print("Research of existing case template")

  try:
	response=api.get_case_template(name)
	print(json.dumps(template, indent=4))
  except CaseTemplateException as e:
	print(str(e))

def del_case(url,key,query,range): #query= (Eq('tlp', 2)) number=50
	api=TheHiveApi(url,key)

	print("Delete all cases")
	response=api.find_cases(query=query,range=number)
	if response.status_code == 200:
		for i in range(number):
			id = response.json()[i]['id']
			api.delete_case(id, force=True)
			print(i+1,"/",number)
	else:
		print('ko: {}/{}'.format(response.status_code, response.text))	
