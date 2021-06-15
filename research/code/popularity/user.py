with open ("song_unsort.txt", "w") as f2:
	with open('year1_valid_triplets_visible.txt', 'r') as f:
	    song_to_count = dict()
	    for line in f:
        	_, song, _ = line.strip().split('\t')
        	if song in song_to_count:
        	    song_to_count[song] += 1
        	else:
        	    song_to_count[song] = 1
    		    f2.write(song+'\n')        
        	    pass
        	pass
	    pass
