import ml_metrics as metrics
from sklearn.neighbors import NearestNeighbors
import numpy as np
f=open('final_features_int.txt','r').readlines()
##indicesFile=open('30NearestNeighbors.txt','w')
##distancesFile=open('30NearestNeighbors.txt','w')

N=len(f)
data =[]
for i in range(N):
    w=f[i].split()
    line=[float(x) for x in w]
    data +=[line]

song_to_index = {}
for n, line in enumerate(open('songs_features.txt','r'), start=0):
  song_to_index[line.strip()] = n
  

def saveFile(fileName,inputs):
    a = open(fileName,'w')
    lineNb = len(inputs)
    a.writelines('\t'.join(str(j) for j in i) + '\n' for i in inputs)
    a.closed

with open('year1_valid_triplets_visible.txt','r') as f:
    uts=dict()
    for line in f:
        user,song,_=line.strip().split('\t')
        if song in song_to_index:
            if user in uts:
                uts[user].add(song_to_index[song])
            else:
                uts[user]=set([song_to_index[song]])
                pass
	pass
    pass

with open('year1_valid_triplets_hidden.txt','r') as f:
    utsh=dict()
    for line in f:
        user,song,_=line.strip().split('\t')
        if song in song_to_index:
            if user in utsh:
                utsh[user].add(song_to_index[song])
            else:
                utsh[user]=set([song_to_index[song]])
                pass
	pass
    pass

nbrs = NearestNeighbors(n_neighbors=50, algorithm='ball_tree').fit(data)
distances, indices = nbrs.kneighbors(data)
#print indices[0]
#print distances[1]
#print nbrs.kneighbors_graph(data).toarray()
#saveFile('30NearestNeighborsIndices.txt',indices)
#saveFile('30NearestNeighborsDistances.txt',distances)

c = 0
count = 0
for j, user in enumerate(uts):
    #print j
    if user in utsh:
        flag = 0
#       print user
        rec = []
        l1 = uts[user]
        l2 = map(int, l1)

    #print l2[1]
        for i in l2:
            if i<10000:
                flag = 1
                #print indices[i]
                rec.extend(indices[i])
            #rec.extend(indices[1])
#        print rec
#    print utsh[user]
        hid = map(int, utsh[user])
        if flag>0:
            count = count+1
        #print hid
        #print j    
        c = c+metrics.apk(utsh[user],rec, 10000)
#print j
#print count
#print c
relevant = c/(count)
print relevant
allu = c/j
#print allu


