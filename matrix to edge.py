import pandas as pd
import numpy as np
import networkx as nx
import csv


'''
def adj_to_list(input_filename,output_filename,delimiter):
'
    A=pd.read_csv(input_filename,delimiter=delimiter,index_col=0)
    List=[('Source','Target','Weight')]
    for source in A.index.values:
        for target in A.index.values:
            List.append((target,source,A[source][target]))
    with open(output_filename, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(List)
    return List

List=adj_to_list('matrix.csv','edge_list.csv',',')
'''
def opensmallcsv3(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data
def exportcsv(Datalist,output):
    with open(output, 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(Datalist)

#get all edge
LISTA=[('Source', 'Target','Weight')]
data=opensmallcsv3('weibo_matrix.csv')
for source in data[1:]:
    index_s=data.index(source)
    for target in source[1:]:
        index_t=source.index(target)
        LISTA.append((data[index_s][0],data[0][index_t],target))

#remove edge with 0 weight
LISTB=[]
for edge in LISTA:
    edgelist=list(edge)
    #print(edgelist,edgelist[2],type(edgelist[2]))

    if (edgelist[2]!=str('0')):
        LISTB.append(edge)

exportcsv(LISTB, 'edgelist.csv')