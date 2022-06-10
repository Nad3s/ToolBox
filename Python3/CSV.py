#!/usr/bin/python
"""
This script regroup all the function who can be usefull for CSV file (reading (R), writting (W), extract (E)...) 
Modules used:
- pandas
"""
import pandas

#RE. Result -> Table datas with 1 table by line + X tables by peer of Header/Value
def read_csv(file):
  datas,header= [],[]
  table = pandas.read_csv(file)
  for column in table:
     header.append(column)
      
  for index, row in table.iterrows():
    line=[]
    for i in range(len(header)):
      couple=[]
      couple.append(header[i])
      couple.append(table[header[i]].values[index])
      line.append(couple)
      
    datas.append(line)
    #print(datas)
  return datas
