#only works when the edge start with 1,and no break values
import pandas as pd
import xlsxwriter
from scipy.sparse import coo_matrix


data=pd.read_csv('block_network_T.csv',header=None)

nodes=data.iloc[:,0].tolist()+ data.iloc[:,1].tolist()
n_nodes=sorted(list(set(nodes)))

s_nodes=[(i,n_nodes[i]) for i in range(len(n_nodes))]

#for i in range(len(s_nodes)):
#    data=data.replace(s_nodes[i][1],s_nodes[i][0])

print(len(n_nodes))
matrix=[[0 for x in range(len(n_nodes))] for y in range(len(n_nodes))]
print(matrix[0][0])

for i in range(len(n_nodes)):
    a=int(data.iloc[i,0])
    b=int(data.iloc[i,1])
    c=data.iloc[i,2]
    print(a,type(a),)
    matrix[a-1][b-1]=c
print(matrix)



#print(matrix)

'''

#M = coo_matrix(('1', (data.iloc[:,0],data.iloc[:,1])), shape=(len(n_nodes), len(n_nodes)))
#M1=M.todense()



df=pd.DataFrame(M1)

df.to_excel('current_block_matrix.xlsx')
'''