from additional import *

__author__ = 'Maxim'


# Returns node degree
def degree(graph, node_name):
    return len(get_parents(graph, node_name)) + \
           len(get_node_by_name(graph, node_name).children_list)


# Returns sorted by degree list of nodes
def nodes_list(graph):
    lst = []
    for node in graph:
        lst.append({'name': node.name, 'degree': degree(graph, node.name)})
    for i in range(1, len(lst)):
        for j in range(len(lst) - 1, i - 1, -1):
            if lst[j - 1]['degree'] < lst[j]['degree']:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst
