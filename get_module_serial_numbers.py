#!/usr/bin/env python

#python get_module_serial_numbers.py

'''
Script to retrieve serial numbers of production ITk modules from different assembly institutes 

Adapted by Jesse Liu
Based on 
- https://itkdb.docs.cern.ch/latest/examples/
- https://gitlab.cern.ch/atlas-itk-production-software/strips/itk-strip-production-module_hybrid-tracker/-/blob/master/src/fetch_serials.py?ref_type=heads

Athenticate following these instructions by copying token to environment variable: 
  export ITK_DB_AUTH=TOKEN 
https://gitlab.cern.ch/atlas-itk/sw/db/production_database_scripts/-/tree/master?ref_type=heads#authentication
'''

import argparse
import os
from pprint import pprint
# https://itkdb.docs.cern.ch/latest/
import itkdb
import numpy
import pandas as pd

def fetch_serials_from_batch(batchNames, institute, componentType, client):
    print(f'fetching serial numbers for component type {componentType} at institute {institute}')

    data = {"filterMap": {"componentType": componentType, "institute": institute}}
    component_jsons = client.get("listComponents", json=data)
    components = pd.json_normalize(data=component_jsons, record_path=["batches"], meta=['serialNumber', 'state', 'trashed'], record_prefix='_')
    pprint(components)
    list_of_components_in_batch = components.loc[(components['_number'].isin(batchNames)) & (components['_state'] == 'ready') & (components['state'] == 'ready')]
    serialNumbers = (list_of_components_in_batch['serialNumber']).to_numpy().tolist()
    print(f'\nfetched {len(serialNumbers)} serial numbers for component type {componentType} at institute {institute}')
    return serialNumbers

def get_hybrid_serial_from_module(module_serial, client):
    
    component = client.get("getComponent", json={"component": module_serial})  
    for item in component['children']:
       if 'HYBRID' in item['componentType']['code']:
         try:
           hybrid_serial = item['component']['serialNumber']
         except TypeError:
           hybrid_serial = ''
    print('{0}, {1}'.format(module_serial, hybrid_serial))
    return hybrid_serial

def hybrid_serial_dictionary_from_module_list(module_serial_numbers, client):
   
  d_hybrid_serials = {}
  print('Module serial number, hybrid serial number')
  for module_serial in module_serial_numbers:
    hybrid_serial =  get_hybrid_serial_from_module(module_serial, client)
    d_hybrid_serials[module_serial] = hybrid_serial
    
  return d_hybrid_serials

if __name__ == "__main__":

  token = os.getenv("ITK_DB_AUTH")
  user = itkdb.core.UserBearer(bearer=token)
  if token:
    client = itkdb.Client(user=user)  
  else: 
    client = itkdb.Client()

  # Lawrence Berkeley National Laboratory
  print('Fetching LBNL module/hybrid serial numbers')
  serials_LBNL = fetch_serials_from_batch(['PRODUCTION_LBNL'], 'LBNL_STRIP_MODULES', 'MODULE', client)
  d_hybrids_LBNL = hybrid_serial_dictionary_from_module_list(serials_LBNL, client)
  
  # Brookhaven National Laboratory
  print('Fetching BNL module/hybrid serial numbers')
  serials_BNL  = fetch_serials_from_batch(['PRODUCTION_BNL'],  'BNL',                'MODULE', client)
  d_hybrids_BNL = hybrid_serial_dictionary_from_module_list(serials_BNL, client)
  
  # University of California at Santa Cruz (SCIPP = Santa Cruz Institute for Particle Physics)
  print('Fetching BNL module/hybrid serial numbers')
  serials_UCSC = fetch_serials_from_batch(['PRODUCTION_UCSC'], 'UCSC',               'MODULE', client)
  d_hybrids_UCSC = hybrid_serial_dictionary_from_module_list(serials_UCSC, client)

  print('\nSerial numbers for Brookhaven (BNL) ITk production modules and hybrids:')
  pprint(d_hybrids_BNL)
  print('\nSerial numbers for Berkeley (LBNL) ITk production modules and hybrids:')
  pprint(d_hybrids_LBNL)
  print('\nSerial numbers for Santa Cruz (UCSC) ITk production modules and hybrids:')
  pprint(d_hybrids_UCSC)