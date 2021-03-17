# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import productForm, pathForm, OrderForm, ManufacturerForm, CategoryForm
from .models import productDetails, productSuggestions, Category, Manufacturer
from django.shortcuts import render,redirect
from django.db.models import Max
import math
import json


# Create your views here.
def index(request):
    return render(request,"productDetails/index.html")
def product_list(request):
    return render(request,"productDetails/product_list.html")

def product_order(request):
    if request.method == "GET":
        context = {'productdetails': productDetails.objects.all()}
        return render(request,"productDetails/product_order.html",context)
    else:
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/product/list/')

def product_form(request):
    if request.method == "GET":
        form = productForm()
        return render(request,"productDetails/product_form.html",{'form': form})
    else:
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/product/list/')

def suggestions(request):
    datalist = []
    try:
        data = productSuggestions.objects.all().order_by('-count')[0]
        data2 = productSuggestions.objects.all().order_by('-count')[1]
        ##res = list(data.values())[0] 
        proid = data.productId_id
        proid2 = data2.productId_id
        productdet = productDetails.objects.get(id = proid)
        productdet2 = productDetails.objects.get(id = proid2)
        datalist.append(productdet.product_Name)
        datalist.append(productdet.rack_No)
        datalist.append(data.count)
        datalist.append(productdet2.product_Name)
        datalist.append(productdet2.rack_No)
        datalist.append(data2.count)
    except:
        print("Some Error")
    
    return render(request,"productDetails/suggestions.html",{'datalist':datalist})

def product_delete(request):
    return

def manufacturer(request):
    if request.method == "GET":
        form = ManufacturerForm()
        return render(request,"productDetails/manufacturer.html",{'form': form})
    else:
        form = ManufacturerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/product/list/')

def category(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request,"productDetails/category.html",{'form': form})
    else:
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/product/list/')

def product_path(request, value):
    try:
        data = productSuggestions.objects.get(productId_id = value)
        data.count = data.count + 1
        data.save()
    except:
        data = productSuggestions()
        data.productId_id = value
        data.count = 1 
        data.save()
    rackdata = productDetails.objects.get(id = value)
    rackno = rackdata.rack_No
    print(rackno)
    def Dijkstra(graph,source,target):
    
        # These are all the nodes which have not been visited yet
        unvisited_nodes=graph
        # It will store the shortest distance from one node to another
        shortest_distance={}
        # This will store the Shortest path between source and target node 
        route=[] 
        # It will store the predecessors of the nodes
        predecessor={}
                
        # Iterating through all the unvisited nodes
        for nodes in unvisited_nodes:
                    
        # Setting the shortest_distance of all the nodes as infinty
            shortest_distance[nodes]=float('inf')
                    
        # The distance of a point to itself is 0.
        shortest_distance[source]=0
                
        # Running the loop while all the nodes have been visited
        while(unvisited_nodes):
                    
            # setting the value of min_node as None
            min_Node=None
                    
            # iterating through all the unvisited node
            for current_node in unvisited_nodes: 
                        
            # For the very first time that loop runs this will be called
                if min_Node is None:
                        
                    # Setting the value of min_Node as the current node
                    min_Node=current_node
                            
                elif shortest_distance[min_Node] > shortest_distance[current_node]:
                            
                    # I the value of min_Node is less than that of current_node, set 
                    #min_Node as current_node

                    min_Node=current_node
                            
            # Iterating through the connected nodes of current_node (for # 
            #example, a is connected with b and c having values 10 and 3 
            # respectively) and the weight of the edges

            for child_node,value in unvisited_nodes[min_Node].items():

                # checking if the value of the current_node + value of the edge 
                # that connects this neighbor node with current_node
                # is lesser than the value that distance between current nodes 
                # and its connections
                if value + shortest_distance[min_Node] < shortest_distance[child_node]:  
                            
        # If true  set the new value as the minimum distance of that connection
                    shortest_distance[child_node] = value + shortest_distance[min_Node]
                            
            # Adding the current node as the predecessor of the child node
                    predecessor[child_node] = min_Node
                    
                # After the node has been visited (also known as relaxed) remove it from unvisited node
            unvisited_nodes.pop(min_Node)
                    
            # Till now the shortest distance between the source node and target node 
            # has been found. Set the current node as the target node 
        node = target
                
            # Starting from the goal node, we will go back to the source node and 
        # see what path we followed to get the smallest distance
        while node != source:
                    
                # As it is not necessary that the target node can be reached from # the source node, we must enclose it in a try block
            try:
                route.insert(0,node)
                node = predecessor[node]
            except Exception:
                print('Path not reachable')
                break
            # Including the ssource in the path
        route.insert(0,source)
                
            # If the node has been visited,
        if shortest_distance[target] != float('inf'):
            # print the shortest distance and the path taken
            print('Shortest distance is ' + str(shortest_distance[target]))
            print('And the path is ' + str(route))
            return route
            # Remove the below comment if you want to show the the shortest distance 
            #from source to every other node
            # print(shortest_distance)

    graph = {'a':{'a':0,'b':2,'c':7,'g':4},'b':{'b':0,'a':2,'j':4,'d':6},'c':{'c':0,'a':7,'g':5,'h':3,'d':2},'d':{'d':0,'b':6,'c':2,'e':1},'e':{'e':0,'d':1,'j':8,'f':1,'h':2},'f':{'f':0,'e':1,'h':5,'i':4,'k':3},'g':{'g':0,'a':4,'c':5,'h':2},'h':{'h':0,'g':2,'c':3,'e':2,'f':5,'i':6},'i':{'i':0,'f':4,'h':6,'k':9},'j':{'j':0,'b':4,'e':8,'k':5},'k':{'k':0,'j':5,'f':3,'i':9}}
            #Calling the function with source as 'a' and target as 'e'.
    sa = Dijkstra(graph,'a',rackno)
    print(sa)
    link = ["Hello","Hai"]
    print(sa)
    return render(request,'productDetails/product_path.html',{'sa':sa})
    return redirect('/product/')
