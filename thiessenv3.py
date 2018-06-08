# -*- coding: utf-8 -*-
"""
Created on DATE

@author: NAME
"""

import csv
'''

def opensmallcsv2(file):
    with open(file,'rb') as f:
        reader = csv.reader(f)
        data =list(reader)
    return data
'''
#get csv data for further operation
def opensmallcsv3(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

#get the thiessen polygon ID
def getlist(data,number):

    tempset=set()
    storeitem=[]

    for row in data:
        tempset.add(row[number])
    for item in tempset:
        storeitem.append(item)
    storeitem.sort()
    return storeitem

#calculate results
def thiessen_cal(dataset,data,RowOfDataset,RowOfData):
    lista=[]
    for element in dataset:
        sum1=0
        for row in data:
            try:
                if str(row[RowOfDataset]) == str(element):
                    sum1 = int(row[RowOfData]) + sum1
            except ValueError:
                pass
        lista.append([element, sum1])
    return lista
#output data
def exportcsv(Datalist,output):
    with open(output, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(Datalist)

Input = 'thissen1.csv'
Output = 'test1_su.csv'
NumberOfTheFirstRow=1
NumberOfTheSecondRow=4



adata=opensmallcsv3(Input)
alist=getlist(adata,NumberOfTheFirstRow)
result=thiessen_cal(alist,adata,NumberOfTheFirstRow,NumberOfTheSecondRow)
exportcsv(result,Output)

