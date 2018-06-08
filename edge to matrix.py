import pandas as pd
import xlsxwriter
from scipy.sparse import coo_matrix


data=pd.read_csv('street_edge_table.csv',header=None)

nodes=data.iloc[:,0].tolist()+ data.iloc[:,1].tolist()
n_nodes=sorted(list(set(nodes)))

s_nodes=[(i,n_nodes[i]) for i in range(len(n_nodes))]

for i in range(len(s_nodes)):
    data=data.replace(s_nodes[i][1],s_nodes[i][0])
'''
since the replace did not recognize which part of data has beeen replaced, if the weight
table have some integer value, the value will be also replaced as value, so it need to
improved, and caution of use weight=1, the most common cases
'''



M = coo_matrix((data.iloc[:,2], (data.iloc[:,0],data.iloc[:,1])), shape=(len(n_nodes), len(n_nodes)))
M1=M.todense()



df=pd.DataFrame(M1)

df.to_excel('current_street_matrix.xlsx')


