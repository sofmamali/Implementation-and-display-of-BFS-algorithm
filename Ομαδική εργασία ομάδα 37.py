# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:12:15 2018

@author: pavilion
"""
import networkx as nkx
import matplotlib.pyplot as pbt
from matplotlib.pyplot import pause

def bfs(graph, start):
    visited = []
    tail = [start]
    not_visited=[]
    while tail:
        now = tail.pop(0)
        print("Αναζήτηση του κόμβου:", now)
        if now not in visited:
           visited.append(now)
           not_visited = list(set(nodes).difference(visited))
           nkx.draw_networkx_nodes(G, place, nodelist=visited, node_color='blue', node_size=1400)
           nkx.draw_networkx_nodes(G, place, nodelist=not_visited,  node_color="lightblue", node_size=1000)
           nkx.draw_networkx_edges(G, place, edge_color='black', edgelist=G.edges(), width=3)
           nkx.draw_networkx_labels(G, place, font_size=20, font_family='Arial')
           print("Κόμβοι τους οποίους έχουμε επισκεπτεί:",visited)
           print("Γείτονες του κόμβου",now,":",list(G.neighbors(now)))
           neighbours = graph[now]
           for neighbour in neighbours:
               if (neighbour not in tail) and (neighbour not in visited):
                   tail.append(neighbour)
           pause(2.5)
        print("Ουρά:",tail)
        
    print("Η ουρά είναι άδεια. Έχουμε επισκεπτεί όλους τους κόμβους!")
    return visited

graph = {0: [1, 2],
         1: [0],
         2: [0, 4],
         3: [7,9],
         4: [2, 5],
         5: [4, 6, 7],
         6: [5, 8],
         7: [3, 8, 5],
         8: [6, 7],
         9: [3]
         }

nodes=[]
edges=[]
for node in graph:
    nodes.append(node)
    ##---------------------------------------------------------------
    edges.append(graph[node])

labels = {}

G=nkx.Graph()
for node in nodes:
    G.add_node(node)
    labels[node] = node # oxi lejiko alla lista
    for n in edges[node]:
        G.add_edge(node,n,  edge_color='black')

print(G.nodes())
print(G.edges())

place= nkx.shell_layout(G)
nkx.draw_networkx_nodes(G, place, node_color='lightblue', node_size=1000)
nkx.draw_networkx_edges(G, place, edge_color='black', edgelist=G.edges(), width=3)
nkx.draw_networkx_labels(G, place, font_size=20, font_family='Arial')

pbt.ioff()
pbt.axis('off')
pbt.title("Ομαδική Εργασία - Ομάδα 37")
pbt.draw()
pause(2.5)
print(bfs(graph,0))
