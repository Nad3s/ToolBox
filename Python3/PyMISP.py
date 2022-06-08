# Connect to MISP Instance
from pymisp import PyMISP
from keys import misp_url, misp_key #Can remove to use argparse

#Function to start PyMISP
def init(url,key):
  return PyMISP(url, key, True)

#Connection to MISP Instance
misp = init(misp_url, misp_key)

# Get events
event = misp.get_event(ID_EVENT)
print(event)
