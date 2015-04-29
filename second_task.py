from additional import *

__author__ = 'Maxim'


# Sets unoptimized labels to the nodes
def set_labels2(nodes, start, end, visited, to_visit):
    if not to_visit:
        return
    node = get_node_by_name(nodes, to_visit[0])
    visited.append(node)
    if to_visit[0] == start:
        node.label = 0
    elif to_visit[0] == end:
        return
    # else:
    for i in node.children_list:
        child_node = get_node_by_name(nodes, i['name'])
        if i['weight'] + node.label < child_node.label:
            child_node.label = i['weight'] + node.label
    for i in node.children_list:
        if not was_visited(visited, i['name']):
            to_visit.append(i['name'])
    to_visit.remove(to_visit[0])
    set_labels2(nodes, start, end, visited, to_visit)


# Returns list of nodes names
def get_nodes_names(graph):
    names = []
    for node in graph:
        names.append(node.name)
    return names


# Sets optimized labels to the nodes
def set_labels_breadth(nodes, start, end):
    labels_before = get_labels(nodes)
    set_labels2(nodes, start, end, [], [start])
    labels_after = get_labels(nodes)
    while labels_after != labels_before:
        # for i in nodes:
        #     print(i)
        # print()
        # print()
        labels_before = labels_after
        set_labels2(nodes, start, end, [], [start])
        labels_after = get_labels(nodes)


# Returns dictionary {'way': shorted way, 'cost': way cost}
# of founded way by search in depth
def breadth_first(graph, start_name, end_name):
    set_labels_breadth(graph, start_name, end_name)
    return {'way': restore_way(graph, start_name, end_name,
                               end_name, end_name, []),
            'cost': get_node_by_name(graph, end_name).label}
