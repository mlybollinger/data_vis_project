# data_vis_project

I wrote this script as part of a project to create a music recommendation engine using a graph-based algorithm. Our group took the Spotify million playlist
dataset and converted it into a graph: each node was a song, and the weight of the edges between two nodes was the # of playlists on which they both appeared.

Our group's initial method was to rank song similarity based purely on the weight of the edges between two songs. I decided to refine this method by factoring in
shared neighbors as well. To accomplish this, I decided to represent each song's neighbors by a vector consisting of the weights of the edges to each neighbor. 
I then used cosine similarity to quantify the proximity between pairs of nodes.

Since our graph consisted of about 100,000 songs, calculating the similarities between every pair of nodes would have been impossible. Instead, I looked at smaller subgraphs until every node in the graph had been examined. My procedure was to start by taking a node and construct a subgraph consisting of every node within two edges of the initial one. Within that subgraph, I would calculate the similarity scores for every node that had not been examined, and then remove those newly-examined nodes from a running set. I found that it sped up the process enormously to use a Python set rather than a list to keep track of examined/unexamined nodes.

As a visual aid, I also generated a force-directed graph from the 1000 most central nodes. I then used a hierarchical clustering algorithm + a color-coded visualization to identify different groupings of the songs in our graph. These spatial groupings tended to correlate with factors like genre, time period, etc. 
