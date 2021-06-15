import recsys.algorithm
recsys.algorithm.VERBOSE = True
import ml_metrics as metrics
import numpy as np
from pprint import pprint
from recsys.algorithm.factorize import SVDNeighbourhood
import scipy.sparse
from sparsesvd import sparsesvd
from scipy import linalg, mat, dot;
from numpy import loads, mean, sum, nan

from recsys.algorithm.factorize import SVD
svd = SVD()

svd.load_data(filename='number_valid.txt', sep=',', format={'col':1, 'row':0, 'value':2, 'ids': int})
mat = svd.get_matrix()


#print m
print scipy.sparse.issparse(mat)

k = 1000
svd.compute(k=k, min_values=1, pre_normalize=None, mean_center=False, post_normalize=False, savefile='movielens2')

with open('user_valid.txt', 'r') as f:
    canonical_users = map(lambda line: line.strip(), f.readlines()) 
    pass

with open('kaggle_songs.txt', 'r') as f:
    song_to_index = dict(map(lambda line: line.strip().split(' '), f.readlines())) 
    pass

with open('number_valid_hid.txt','r') as f:
    uts=dict()
    for line in f:
        user,song,_=line.strip().split(',')
        if user in uts:
            uts[user].append(song)
        else:
            uts[user]=[song]
            pass
	pass
    pass

hidden = uts.values()

    

c = 0
j = 1
with open('number_valid_hid.txt','r') as f2:
    check=dict()
    for line in f2:
        if j>=40:
            break
        user, song,_=line.strip().split(',')
        if user not in check:
             check[user]=[song]
             hidlist = uts[user]
	     
	     rating = svd.recommend(int(user), n=10, only_unknowns=False, is_row=True)
	     predict = []
             for i1 in rating:
                 predict.append(i1[0])
             j = j+1
             predict = map(int, predict)
             hidlist = map(int, hidlist)
             c = c+metrics.apk(hidlist,predict,100)
             print c
              

             pass
	pass
    pass

print c
t = c/j
print t


