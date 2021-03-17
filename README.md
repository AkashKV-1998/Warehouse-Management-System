# Warehouse-Management-System

The successful and effective management of a busy and complex warehouse relies upon the control and location of stock within the warehouse. It is essential that stock is located in the most suitable locations, to optimise storage capability and increase resource efficiency. It is critical that the warehouse team has control and visibility at all times. A warehouse needs to be defined in multiple ways to reflect your individual characteristics, with your own location descriptions. 


The warehouse management system is a combinatorial optimization problem, where given a map (a set of racks and their positions in a warehouse), one wants to find an order for visiting the corresponding racks in such a way that the distance is minimal. Warehouse operational costs are heavily influenced by the efficiency in which workers are able to traverse the warehouse and gather items on orders around the warehouse that must be shipped to customers. The act of traversing the warehouse is greatly optimized by finding a shortest path possible to collect the order from the specified rack position .The main goal of Warehouse Management System is to ensure consistent availability of supplies for consumers. In general, there are two issues in optimizing a system: where in the warehouse each rack should be located and also to find an optimized possible path to retrieve the order. Therefore, we propose an implementation of a warehouse management system based on Dijkstra’s Algorithm to find the best shortest path.


## CONTENTS

1. Introduction 
2. Problem and Solution 
3. Implementation 
4. Conclusion 
5. References 

#### 1. Introduction

A common goal of nearly all businesses is to reduce man-hour and increase the
overall profit margin of the business. In warehouse related businesses,
optimizing the efficiency of order picking can lend itself to great reductions in
the time it takes orders to ship out, as well as, improving the overall
effectiveness of its workers. Of all costs associated with warehouse operations,
55-65% of the operational funds are allocated towards order picking showing
the importance of optimizing this phase of the warehouse process.
The warehouse management system is an application that helps to control and
manage the day-to-day operations in a warehouse. It is used to find an order
for visiting the corresponding racks in such a way that the distance travelled is
minimal. Thus it is very useful in reducing the time for picking processes. A
suggestion system which advises on the products to be placed on the initial
racks, so has to decrease the time required to collect the product. Suggestion
system works based on the ranking of the highest selling products.
Warehouse management is the act of organising and controlling everything
within the warehouse and making sure it all runs in the most optimal way
possible. Nearly all activities at a warehouse are centred on receiving orders
from customers. As an order comes into the warehouse, an individual in the
warehouse becomes responsible for the order; this is the order picker. The
order picker is responsible for gathering all items on the order from around
the warehouse, also known as picking, and then placing them in the shipping
area. Once in shipping, the order will be packaged in a box or pallet and
shipped to the customer. The picking process can be time consuming and by
far is the biggest operational expense of any warehouse.

#### 2. Problem and Solution


The main objective of this project is, when an order for a product is placed by
a customer, compare the cost for exploring each path to the rack containing
the product and find the shortest and optimized path possible.
Algorithm used - Dijkstra algorithm
Dijkstra's algorithm solves the problem of finding the shortest path from a
point in a graph (the source ) to a destination. It turns out that one can find
the shortest paths from a given source to all points in a graph at the same
time, hence this problem is sometimes called the single-source shortest paths
problem. .
The algorithm is also easy to alter so that Dijkstra’s will not only return the
distance of the shortest path to each vertex, but also the path to traverse. In
pick path optimization, Dijkstra’s is quite useful as it can be used at each
location to find the shortest distance between this location and all remaining
locations on the order. This is quite practical and is often exactly what we
need to solve in the process of generating an optimal pick path. The reliability,
popularity, and speed of Dijkstra’s makes it a heavily implemented and
researched algorithm, especially in the realm of map routing and GPS
programming.
Dijkstra’s algorithm is quite popular for its performance, with a worst case
performance of O(|E| + |V| Log |V|),where E = number of edges and V =
number of vertices.
Here we are using a graph G with a set of vertices (nodes) V connected by
edges (links) E. Thus G=(V, E).
Therefore ,Here we are using a graph G= (11,18)
The graph G is connected and cyclic.

#### 3.Implementation


Now, warehouses stay competitive by optimizing every possible area of work
from picking to packing to shipping. With new warehouses cropping up every
day, and customer demand for speedy deliveries rising, distribution centres
don’t have the option of phoning it in. They must analyze their warehouses
from top to bottom to look for inefficiencies and nip them in the bud.
One warehouse process that’s ripe for warehouse optimization is the pick
path. According to some estimates, picking takes up over 50% of a
warehouse’s labour efforts. This isn’t surprising considering that, despite
warehouse technological advancements in areas like automated storage and
retrieval systems, picking is still a largely human-led process. It is possible to
further optimize picking and, more specifically, the pick path. Oftentimes, the
biggest cause of inefficiency during the picking process is motion waste - the
unnecessary movement that makes a given task take longer than it should.
Walking path optimization or picking path optimization, depending on who
you talk to, the process of finding the fastest way to navigate the warehouse
in order to pick products quickly, accurately, and efficiently by using various
picking methods such as wave picking, zone picking.
The problem is a shortest path problem, where one would need to find the
shortest point between all the nodes before you’re able to find the shortest
path through all the nodes. This is because there’s no guarantee that every
node is connected with one edge, As a result, you must find the shortest
distance between each node first. The algorithm that is considered for study
is Dijkstra's Algorithm.
With Dijkstra's Algorithm, you can find the shortest path between nodes in a
graph. It can find the shortest path from a node to all other nodes in the
graph , producing a shortest-path tree.

##### Basics of Dijkstra's Algorithm

● Dijkstra's Algorithm starts at the source node and it analyzes the graph to
find the shortest path between that node and all the other nodes in the
graph.

● The algorithm keeps track of the currently known shortest distance from
each node to the source node and it updates these values if it finds a
shorter path.

● Once the algorithm has found the shortest path between the source node
and another node, that node is marked as "visited" and added to the path.

● The process continues until all the nodes in the graph have been added to
the path. This way, we have a path that connects the source node to all
other nodes following the shortest path possible to reach each node.
Implementation of Dijkstra's Algorithm in warehouse management system
The shortest distance between the root node or the source node as the
starting point and the relative position of the object in the rack (node) is
calculated and all the possible distance of the path is taken into note. It is
constantly updated if a better path is found and if a path is visited it is marked
as visited in order to prevent repetitions. Thus once all the nodes are visited
we have a clear list of all the nodes with their shortest possible route.
Thus the application in warehouse problem is more valid and time saving as
once the algorithm goes through all the node possibilities it automatically
provides with a shortest possible distance the object can be accessed thus
improves the efficiency of the warehouse.

Steps in finding the shortest path of warehouse management problem:

● Set a root node

● Iterating through all the unvisited route

● Setting all the nodes shortest distance is infinity to be updated in further
iterations

· Running the iteration to all the unvisited nodes and update the path for the
shortest distance

o Where the current node is kept in memory and the weight of the
subsequent node is added

o If the value of the added combination of the path is lesser than
the previous distance in any iteration then the distance is
updated

· Same way all the connected nodes of the network are compared and the least
possible path is updated and printed for both the employee for accessing the
rack and the customer it provides an interface and transparency.
The whole customer interface is provided by a django model where the user
enters all the information about the object and the shortest path is displayed
after all the process is carried out in the back end.

#### 5. Conclusion

It is necessary to have a proper management system for busy and complex
warehouses. It is difficult to stock the items in the most suitable locations
and to optimise the storage capacity used and most of the time it is
difficult to have control and visibility on the storage location all the time.
So here we have developed an application which can find the shortest path
to the rack. when an order for a product is placed by a customer, compare
the cost for exploring each path to the rack containing the product and
find the shortest and optimized path possible. This way workers can
traverse the warehouse and gather needed items within a shorter period
of time.
In the developed system, we have used Dijkstra algorithm to find out the
shorted path to the rack, which at worst case perform O(|E| + |V|log|V|).
The algorithm not only gives the shortest distance, it also gives which
direction we should take to reach the goal with a shorter distance.
We know that in many warehouses, they use the help of technologies such
as drones and robots to collect the items from the rack which uses a
specific algorithm to function. In our project we have developed a
suggestion system, which can sort the items present in all the racks using
its number of frequencies of the order that item is placed in the past.
By using this workers can identify which product is sold frequently and
reassign the rack according to that and efficiently manage the
Warehouses.

#### 6. References

1. Theys, C., Braysy, O., Dullaert, W., Raa, B., 2010. Using a TSP heuristic for
routing order pickers in warehouses. European Journal of Operational
Research 200 (3), 755–763.

2. Ryan Key, Anurag Dasgupta,Edinboro University of Pennsylvania ,
Warehouse Pick Path Optimization Algorithm Analysis Int'l Conf.
Foundations of Computer Science| FCS'15 |, 63-69.

3. John J Bartholdi and Steven T Hackman. Warehouse & distribution science:
release 0.92. The Supply Chain and Logistics Institute, School of Industrial
and Systems Engineering, Georgia Institute of Technology, Atlanta, GA,
30332, 2010.

4. Parvaneh Jahani. Dynamic warehouse optimization using predictive
analytics. 12-2016 . 1-188.
5. Lee, C. K. M., Lv, Y., Ng, K. K. H., Ho, W., & Choy, K. L. (2017). Design and
application of Internet of things-based warehouse management system for
smart logistics. International Journal of Production Research, 56(8),
2753–2768.
