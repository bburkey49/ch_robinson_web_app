from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CountryCodeForm
from .models import Country
import csv, sys


# dictionary simulation of map
code_dict = {
    'CAN': ['USA'],
    'USA': ['CAN', 'MEX'],
    'MEX': ['GTM', 'BLZ'], 
    'BLZ': ['MEX', 'GTM'],
    'GTM': ['MEX', 'BLZ', 'SLV', 'HND'],
    'SLV': ['GTM', 'HND'],
    'HND': ['GTM', 'SLV', 'NIC'],
    'NIC': ['HND', 'CRI'],
    'CRI': ['NIC', 'PAN'],
    'PAN': ['CRI']
}



def index(request):  
    form = CountryCodeForm()
    country_names = code_dict.keys()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CountryCodeForm(request.POST)

        if form.is_valid():
            entered_code = form.cleaned_data['code'].upper() # no time to deal with lowercase
            route = []
            if entered_code in country_names:
                    route = shortest_path_bfs(code_dict, 'USA', entered_code)
            else:
                    route.append('Country Code Not Found')

            return render(request, 'index.html', context={'countries': route, 'form': form})

    return render(request, 'index.html', context={'countries': country_names, 'form': form})


# rough implementation of BFS for shortest path
def shortest_path_bfs(graph, start, goal): 
    explored_nodes = []
    queue = [[start]] 

    if start == goal: 
        return [goal]

    while queue: 
        path = queue.pop(0) 
        curr_node = path[-1] 

        if curr_node not in explored_nodes: 
            adj = graph[curr_node]

            for a in adj: 
                new_path = list(path) 
                new_path.append(a) 
                queue.append(new_path) 

                if a == goal: 
                    return new_path

            explored_nodes.append(curr_node) 
    
    # no path found
    return None

