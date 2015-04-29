__author__ = 'Maxim'


# One node in graph (with extended data)
class Node:
    # Adds new child to current node
    def add_to_children_list(self, name, weight):
        self.children_list.append({"name": name, "weight": weight})

    # For print
    def __str__(self):
        return self.name + "   label: " + str(self.label)

    # def __str__(self):
    #     return self.name + "   " + str(self.children_list)

    def __init__(self, name):
        self.name = name
        self.children_list = []
        self.label = 20000000000
        self.used_label = False
        self.cannot_go_here_from = []


# Returns node from input list (need for initialization)
def get_node(lst):
    node = Node(lst[0])
    for i in range(0, len(lst[1])):
        node.children_list.append({"name": lst[1][i], "weight": lst[2][i]})
    return node


# Converts input list to list of classes
def get_nodes(lst):
    nodes = []
    for i in lst:
        nodes.append(get_node(i))
    return nodes


# Return class for node with name
def get_node_by_name(nodes, name):
    for i in nodes:
        if i.name == name:
            return i


# Looks for is the node with name in classes list
def was_visited(nodes, name):
    for i in nodes:
        if i.name == name:
            return True
    return False


# Returns list of labels from list of classes
def get_labels(nodes):
    labels = []
    for i in nodes:
        labels.append(i.label)
    return labels


# Returns [nodes] where nodes is parents of node
def get_parents(nodes, node_name):
    ret = []
    for i in nodes:
        for j in i.children_list:
            if j['name'] == node_name:
                ret.append(i)
                break
    return ret


# Return cost of going from parent to child
def weight_to_child(parent_node, child_name):
    for i in parent_node.children_list:
        if i['name'] == child_name:
            return i['weight']


# Answers can we come from one node to other
# (for restoring way (we can have some wrong ways))
def can_go_some_from_some(nodes, _from_name, _to_name):
    for i in get_node_by_name(nodes, _from_name).cannot_go_here_from:
        if i == _to_name:
            return False
    return True


# Restores way from start node to end node
def restore_way(nodes, start, end, curr, prev_name, way):
    if curr == start:
        way.append(start)
        way.reverse()
        return way
    else:
        node = get_node_by_name(nodes, curr)
        for i in get_parents(nodes, curr):
            if can_go_some_from_some(nodes, i.name, node.name) and \
                     weight_to_child(get_node_by_name(nodes, i.name),
                                    node.name) + i.label == node.label:
                way.append(node.name)
                return restore_way(nodes, start, end, i.name, node.name, way)
        node.cannot_go_here_from.append(prev_name)
        way.remove(node.name)


# Resets data for new search
def reset_data(graph):
    for node in graph:
        node.label = 200000
        node.used_label = False
        node.cannot_go_here_from = []
