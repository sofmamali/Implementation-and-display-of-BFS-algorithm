# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:04:23 2018

@author: pavilion
"""
# εισαγωγή των βιβλιοθηκών 
import networkx as nkx
import matplotlib.pyplot as pbt
from matplotlib.pyplot import pause
# αλγόριθμος bfs
def bfs(graph, start):
    # λίστα των κόμβων που έχουμε επισκεπτεί 
    visited = []
    # ουρά προτεραιότητας
    tail = [start]
    # λίστα των κόμβων που δεν έχουμε επισκεπτεί 
    not_visited=[]
    # βοηθητική ματαβλητή
    y=0
    while tail:
        # παύση
        pause(2.5)
        # τωρινός κόμβος 
        now = tail.pop(0)
        y+=0.11
        print("Αναζήτηση του κόμβου:", now)
        # εμφάνιση του τωρινού κόμβου
        pbt.text(-1.145+y/3,1,(now),fontsize=12)
        if len(visited)!=len(graph)-1:
            pbt.text(-1.12+y/3,1,',',fontsize=12)
        # παύση
        pause(1)
        if now not in visited:
           # προσθήκη του τωρινού κόμβου στην λίστα 
           visited.append(now)
           # διαγραφή των ετικετών
           del labels[now]
           # ετικέτες που αντιστοιχούν σε κόμβους που έχουμε επισκεπτεί
           labels_visited.update({now:now})
           # ορισμός της λίστας με τους κόμβους που δεν έχουμε επισκεπτεί
           not_visited = list(set(nodes).difference(visited))
           # αποτύπωση των κόμβων που έχουμε επισκεπτεί
           nkx.draw_networkx_nodes(G, place, nodelist=visited, node_color='blue', node_size=1400)
           # αποτύπωση των κόμβων που δεν έχουμε επισκεπτει 
           nkx.draw_networkx_nodes(G, place, nodelist=not_visited,  node_color="lightblue", node_size=1000)
           # αποτύπωση των ακμών
           nkx.draw_networkx_edges(G, place, edge_color='black', edgelist=G.edges(), width=3)
           # αποτύπωση των ετικετών των κόμβων που δεν έχουμε επισκεπτεί 
           nkx.draw_networkx_labels(G, place, labels=labels, font_size=20, font_family='Arial')
           # αποτύπωση των ετικετών των κόμβων που έχουμε επισκεπτεί
           nkx.draw_networkx_labels(G, place, labels=labels_visited, font_size=20, font_family='Arial', font_color='white')
           print("Κόμβοι τους οποίους έχουμε επισκεπτεί:",visited)
           # εμφάνιση των κόμβων που έχουμε επισκεπτεί
           pbt.text(-1.575,0.35-y,(visited),fontsize=12)
           # παύση
           pause(1)
           print("Γείτονες του κόμβου",now,":",list(G.neighbors(now)))
           # εμφάνιση των γείτονων κόμβων
           pbt.text(1.1,1-y,(now,list(G.neighbors(now))),fontsize=12)
           # παύση
           pause(1)
           # ορισμός των γειτόνων του τωρινού κόμβου
           neighbours = graph[now]
           for neighbour in neighbours:
               if (neighbour not in tail) and (neighbour not in visited):
                   # προσθήκη του γειτονικού κόμβου στην ουρά
                   tail.append(neighbour)
        print("Ουρά:",tail)
        # εμφάνιση της ουράς
        pbt.text(1.1,-0.25-y,(tail),fontsize=12)
        # παύση
        pause(0.5)
    print("Η ουρά είναι άδεια. Έχουμε επισκεπτεί όλους τους κόμβους!")
    # εμφάνιση οταν έχουμε επισκεπτεί όλους τους κόμβους
    pbt.text(-0.72,-1.3,"Η ουρά είναι άδεια. Έχουμε επισκεπτεί όλους τους κόμβους!",fontsize=16,color='red')
    return visited
# γράφημα
graph = {0: [1, 2],
         1: [0, 5, 8],
         2: [0, 4, 9],
         3: [6, 7 ,9],
         4: [2, 5],
         5: [1, 4, 7],
         6: [3, 8],
         7: [3, 8, 5],
         8: [6, 7],
         9: [3, 2]
         }
# λίστα των κόμβων
nodes=[]
# λίστα των ακμών
edges=[]
for node in graph:
    # ορισμός των κόμβων
    nodes.append(node)
    # ορισμός των ακμών
    edges.append(graph[node])
# ετικέτες των κόμβων που δεν έχουμε επισκεπτεί
labels = {}
# ετικέτες των κόμβων που έχουμε επισκεπτεί
labels_visited = {}
# δημιουργία γραφήματος
G=nkx.Graph()
for node in nodes:
    # προσθήκη κόμβων
    G.add_node(node)
    # ορισμός των ετικετών
    labels[node] = node 
    for n in edges[node]:
        # προσθήκη ακμών
        G.add_edge(node,n,  edge_color='black')
# εμφάνισε τους κόμβους
print(G.nodes())
# εμφάνισε τις ακμές
print(G.edges())
# δημιουργία παραθύρου
place= nkx.shell_layout(G)
# αποτύπωση των κόμβων
nkx.draw_networkx_nodes(G, place, node_color='lightblue', node_size=1000)
# αποτύπωση των ακμών
nkx.draw_networkx_edges(G, place, edge_color='black', edgelist=G.edges(), width=3)
# αποτύπωση των ετικετών
nkx.draw_networkx_labels(G, place, font_size=20, font_family='Arial')
# αποτύπωση του γραφήματος
pbt.ioff()
# απόκρυψη των αξόνων
pbt.axis('off')
# ορισμός τίτλου του παραθύρου
pbt.title("Ομαδική Εργασία - Ομάδα 37",fontsize=15)
pbt.draw()
# εμφάνιση του τωρινού κόμβου
pbt.text(-1.575,1,'Αναζήτηση του κόμβου:',fontsize=12)
# εμφάνιση των κόμβων που έχουμε επισκεπτεί
pbt.text(-1.575,0.35,"Κόμβοι τους οποίους έχουμε επισκεπτεί:",fontsize=12)
# εμφάνιση των γειτόνων του τωρινού κόμβου
pbt.text(1.05,1,"Γείτονες του κόμβου:",fontsize=12)
# εμφάνιση της ουράς
pbt.text(1.05,-0.25,"Ουρά:",fontsize=12)
# παύση
pause(2.5)
# κλήση του αλγόριθμου
print(bfs(graph,0))
# τελική παύση
pause(50)
