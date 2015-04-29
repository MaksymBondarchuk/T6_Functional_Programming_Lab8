from additional import *

__author__ = 'Maxim'


# Sets unoptimized labels to the nodes
def set_labels(nodes, start, end, curr, visited):
    node = get_node_by_name(nodes, curr)
    visited.append(node)
    if curr == start:
        node.label = 0
    elif curr == end:
        return
    for i in node.children_list:
        child_node = get_node_by_name(nodes, i['name'])
        if i['weight'] + node.label < child_node.label:
            child_node.label = i['weight'] + node.label
    for i in node.children_list:
        if not was_visited(visited, i['name']):
            set_labels(nodes, start, end, i['name'], visited)


# Sets optimized labels to the nodes
def set_labels_depth(nodes, start, end):
    labels_before = get_labels(nodes)
    set_labels(nodes, start, end, start, [])
    labels_after = get_labels(nodes)
    while labels_after != labels_before:
        labels_before = labels_after
        set_labels(nodes, start, end, start, [])
        labels_after = get_labels(nodes)


# Returns dictionary {'way': shorted way, 'cost': way cost}
# of founded way by search in depth
def depth_first(graph, start_name, end_name):
    set_labels_depth(graph, start_name, end_name)
    return {'way': restore_way(graph, start_name, end_name,
                               end_name, end_name, []),
            'cost': get_node_by_name(graph, end_name).label}
