from first_task import *
from second_task import *
from third_task import *

__author__ = 'Maxim'


# input_lst = [['k', [], [0]], ['m', ['q'], [7]], ['p', ['m', 'q'], [5, 9]]]
# input_lst = [['a', ['b', 'c'], [1, 2]], ['b', ['c', 'd'], [3, 1]],
#  ['c', ['a', 'b', 'd'], [1, 3, 1]], ['d', [], []]]
input_list = [['a', ['b', 'c', 'd'], [5, 1, 2]],
              ['b', ['e'], [1]],
              ['c', ['b', 'd', 'g'], [4, 1, 2]],
              ['d', ['g', 'f'], [1, 1]],
              ['e', [], []],
              ['f', ['b', 'h', 'f'], [1, 4, 1]],
              ['g', ['c', 'f', 'h'], [2, 2, 7]],
              ['h', ['f'], [4]],
              ['z', [], []]
              ]


# Just a menu
def menu(input_list):
    graph = get_nodes(input_list)

    work = True
    while work:
        choise = input('\nEnter number:\n'
                       '1. Search shortest way by search in depth\n'
                       '2. Search shortest way by search in breadth\n'
                       '3. Write node degree\n'
                       '4. Write sorted nodes degree\n'
                       '5. Exit\n')

        if choise == '1':
            _from = input("\nenter start node\n")
            if get_node_by_name(graph, _from) is None:
                print("No node with this name")
            else:
                _to = input("\nenter end node\n")
                if get_node_by_name(graph, _to) is None:
                    print("No node with this name")
                else:
                    shortest_way = depth_first(graph, _from, _to)
                    print(shortest_way['way'])
                    print(shortest_way['cost'])
                    reset_data(graph)
        elif choise == '2':
            _from = input("\nenter start node\n")
            if get_node_by_name(graph, _from) is None:
                print("No node with this name")
            else:
                _to = input("\nenter end node\n")
                if get_node_by_name(graph, _to) is None:
                    print("No node with this name")
                else:
                    shortest_way = breadth_first(graph, _from, _to)
                    print(shortest_way['way'])
                    print(shortest_way['cost'])
                    reset_data(graph)
        elif choise == '3':
            node_name = input("\nenter start node\n")
            if get_node_by_name(graph, node_name) is None:
                print("No node with this name")
            else:
                print(degree(graph, node_name))
        elif choise == '4':
            print(nodes_list(graph))
        elif choise == '5' or choise == 'exit':
            break


menu(input_list)
