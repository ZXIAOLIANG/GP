import copy
import numpy as np
import matplotlib.pyplot as plt
import itertools
import random

terminal_set = ["x1", "x1", "x3", "x4", "x5", "x6", "x9","x10", "x11", "x12", "x13", "x14", "x15", "x16"]
function_set = ["AND", "OR", "NOT", "IF"]
all_set = function_set + terminal_set
g_max_depth = 8

class Node:
    def __init__(self, name, child_list, depth, height, max_depth, parent=None):
        self.name = name
        self.child_list = child_list
        self.parent = parent
        self.depth = depth
        self.height = height
        self.max_depth = max_depth
        self.node_list = []

    def evaluate(self, val_list):
        self.val_list = val_list
        if self.name == "x1":
            return self.val_list[0]
        elif self.name == "x2":
            return self.val_list[1]
        elif self.name == "x3":
            return self.val_list[2]
        elif self.name == "x4":
            return self.val_list[3]
        elif self.name == "x5":
            return self.val_list[4]
        elif self.name == "x6":
            return self.val_list[5]
        elif self.name == "x7":
            return self.val_list[6]
        elif self.name == "x8":
            return self.val_list[7]
        elif self.name == "x9":
            return self.val_list[8]
        elif self.name == "x10":
            return self.val_list[9]
        elif self.name == "x11":
            return self.val_list[10]
        elif self.name == "x12":
            return self.val_list[11]
        elif self.name == "x13":
            return self.val_list[12]
        elif self.name == "x14":
            return self.val_list[13]
        elif self.name == "x15":
            return self.val_list[14]
        elif self.name == "x16":
            return self.val_list[15]
        elif self.name == "AND":
            return self.child_list[0].evaluate(self.val_list) and self.child_list[1].evaluate(self.val_list)
        elif self.name == "OR":
            return self.child_list[0].evaluate(self.val_list) or self.child_list[1].evaluate(self.val_list)
        elif self.name == "NOT":
            return not self.child_list[0].evaluate(self.val_list)
        elif self.name == "IF":
            return self.child_list[1].evaluate(self.val_list) if self.child_list[0].evaluate(self.val_list)\
                     else self.child_list[2].evaluate(self.val_list)

    def print_program(self):
        
        if self.name == "x1":
            return self.name
        elif self.name == "x2":
            return self.name
        elif self.name == "x3":
            return self.name
        elif self.name == "x4":
            return self.name
        elif self.name == "x5":
            return self.name
        elif self.name == "x6":
            return self.name
        elif self.name == "x7":
            return self.name
        elif self.name == "x8":
            return self.name
        elif self.name == "x9":
            return self.name
        elif self.name == "x10":
            return self.name
        elif self.name == "x11":
            return self.name
        elif self.name == "x12":
            return self.name
        elif self.name == "x13":
            return self.name
        elif self.name == "x14":
            return self.name
        elif self.name == "x15":
            return self.name
        elif self.name == "x16":
            return self.name
        elif self.name == "AND":
            return "(" + self.child_list[0].print_program() + " AND " + self.child_list[1].print_program() +")"
        elif self.name == "OR":
            return "(" + self.child_list[0].print_program() + " OR " + self.child_list[1].print_program() +")"
        elif self.name == "NOT":
            return "(NOT " + self.child_list[0].print_program() + ")"
        elif self.name == "IF":
            return "(IF " + self.child_list[0].print_program() +" THEN "+ self.child_list[1].print_program()\
                    + " ELSE " + self.child_list[2].print_program() +")"
    def traverse(self):
        pass

def target_function(solution):
    '''
    solution = ["x1", "x1", "x3", "x4", "x5", "x6", "x9","x10", "x11", "x12", "x13", "x14", "x15", "x16"]
    '''
    sum_ = 0
    for x in solution:
        if x == True:
            sum_ += 1
    if sum_ <= 9 and sum_ >= 7:
        return True
    else:
        return False

def construct_test_set(n):
    test_set = [list(i) for i in itertools.product([True, False], repeat=n)]
    answer_list = []
    for i in range(len(test_set)):
        answer = target_function(test_set[i])
        answer_list.append(answer)
    return test_set, answer_list

def construct_partial_test_set(n):
    test_set = [list(i) for i in itertools.product([True, False], repeat=n)]
    partial_test_set = random.sample(test_set, 1000)
    # print(partial_test_set)
    # int(0.1*len(test_set))
    partial_answer_list = []
    for i in range(len(partial_test_set)):
        answer = target_function(partial_test_set[i])
        partial_answer_list.append(answer)
    return partial_test_set, partial_answer_list

def fitness_evaluation(test_set, answer_list, tree):
    correct_count = 0
    incorrect_count = 0
    for i in range(len(test_set)):
        res = tree.evaluate(test_set[i])
        if res == answer_list[i]:
            correct_count += 1
        else:
            incorrect_count += 1
    # print(incorrect_count)
    # print(correct_count)
    return float(correct_count) / float(correct_count + incorrect_count)

def construct_full_tree(height, parent=None):
    depth = 0 if parent is None else parent.depth + 1
    max_depth = g_max_depth
    if height == 0:
        terminal_node = Node(name=random.choice(terminal_set), child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
        if terminal_node.parent is not None:
            terminal_node.parent.node_list.append(terminal_node)
        return terminal_node
    else:
        name = random.choice(function_set)
        if name == "NOT":
            not_node = Node(name="NOT", child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
            if parent is not None:
                not_node.parent.node_list.append(not_node)
            child1 = construct_full_tree(height - 1, parent=not_node)
            not_node.child_list.append(child1)
            not_node.node_list += child1.node_list
            not_node.height = child1.height + 1
            return not_node
        elif name == "AND" or name == "OR":
            binary_node = Node(name=name, child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
            if parent is not None:
                binary_node.parent.node_list.append(binary_node)
            child1 = construct_full_tree(height - 1, parent=binary_node)
            child2 = construct_full_tree(height - 1, parent=binary_node)
            binary_node.child_list.append(child1)
            binary_node.child_list.append(child2)
            binary_node.node_list += child1.node_list
            binary_node.node_list += child2.node_list
            binary_node.height = max(child1.height + 1, child2.height + 1)
            return binary_node
        elif name == "IF":
            trinary_node = Node(name=name, child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
            if parent is not None:
                trinary_node.parent.node_list.append(trinary_node)
            child1 = construct_full_tree(height - 1, parent=trinary_node)
            child2 = construct_full_tree(height - 1, parent=trinary_node)
            child3 = construct_full_tree(height - 1, parent=trinary_node)
            trinary_node.child_list.append(child1)
            trinary_node.child_list.append(child2)
            trinary_node.child_list.append(child3)
            trinary_node.node_list += child1.node_list
            trinary_node.node_list += child2.node_list
            trinary_node.node_list += child3.node_list
            trinary_node.height = max(child1.height + 1, child2.height + 1, child3.height + 1)
            return trinary_node
            

def construct_grow_tree(height, parent=None):
    depth = 0 if parent is None else parent.depth + 1
    max_depth = g_max_depth
    if height == 0:
        terminal_node = Node(name=random.choice(terminal_set), child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
        if terminal_node.parent is not None:
            terminal_node.parent.node_list.append(terminal_node)
        return terminal_node
    else:
        name = random.choice(all_set)
        if name == "NOT":
            not_node = Node(name="NOT", child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
            if parent is not None:
                not_node.parent.node_list.append(not_node)
            child1 = construct_grow_tree(height - 1, parent=not_node)
            not_node.child_list.append(child1)
            not_node.node_list += child1.node_list
            not_node.height = child1.height + 1
            return not_node
        elif name == "AND" or name == "OR":
            binary_node = Node(name=name, child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
            if parent is not None:
                binary_node.parent.node_list.append(binary_node)
            child1 = construct_grow_tree(height - 1, parent=binary_node)
            child2 = construct_grow_tree(height - 1, parent=binary_node)
            binary_node.child_list.append(child1)
            binary_node.child_list.append(child2)
            binary_node.node_list += child1.node_list
            binary_node.node_list += child2.node_list
            binary_node.height = max(child1.height + 1, child2.height + 1)
            return binary_node
        elif name == "IF":
            trinary_node = Node(name=name, child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
            if parent is not None:
                trinary_node.parent.node_list.append(trinary_node)
            child1 = construct_grow_tree(height - 1, parent=trinary_node)
            child2 = construct_grow_tree(height - 1, parent=trinary_node)
            child3 = construct_grow_tree(height - 1, parent=trinary_node)
            trinary_node.child_list.append(child1)
            trinary_node.child_list.append(child2)
            trinary_node.child_list.append(child3)
            trinary_node.node_list += child1.node_list
            trinary_node.node_list += child2.node_list
            trinary_node.node_list += child3.node_list
            trinary_node.height = max(child1.height + 1, child2.height + 1, child3.height + 1)
            return trinary_node
        else:
            # terminal is chosen
            terminal_node = Node(name=name, child_list=[], depth=depth, height=0,\
                            max_depth=max_depth, parent=parent)
            if parent is not None:
                terminal_node.parent.node_list.append(terminal_node)
            return terminal_node
            

def full_method(pop_size, max_depth):
    tree_lst = []
    for i in range(pop_size):
        tree = construct_full_tree(max_depth)
        tree_lst.append(tree)
    return tree_lst

def grow_method(pop_size, max_depth):
    tree_lst = []
    for i in range(pop_size):
        tree = construct_grow_tree(max_depth)
        tree_lst.append(tree)
    return tree_lst


def initialize_population(pop_size, max_depth):
    full_tree_list = full_method(int(pop_size/2), max_depth)
    grow_tree_list = grow_method(int(pop_size/2), max_depth)
    return full_tree_list + grow_tree_list

def tournament_selection(pop, pop_fitness):
    index = [x for x in range(len(pop))]
    candidates_index = random.sample(index, 7)
    best_index = 0
    max_fitness = 0
    for i in range(7):
        val = pop_fitness[candidates_index[i]]
        if val > max_fitness:
            max_fitness = val
            best_index = candidates_index[i]
    return copy.deepcopy(pop[best_index])

def update_depth_of_subtree(subtree, depth):
    subtree.depth = depth
    for c in subtree.child_list:
        update_depth_of_subtree(c, depth+1)

def update_parent(p, old_subtree, new_subtree):
    while p is not None:
        for node in old_subtree.node_list:
            p.node_list.remove(node)
        p.node_list.remove(old_subtree)
        p.node_list += new_subtree.node_list
        p.node_list.append(new_subtree)
        max_c_height = 0
        for c in p.child_list:
            if c.height > max_c_height:
                max_c_height = c.height
        p.height = max_c_height+1
        p = p.parent

def recombine(p1, p2):
    # print("@@@@@@@@@@@@@@@@@@@@")
    # for noi in p1.node_list:
    #     print(noi.print_program())
    # print("@@@@@@@@@@@@@@@@@@@@")
    if len(p1.node_list) == 0:
        p1_subtree = p1
    else:
        p1_subtree = random.choice(p1.node_list)
    p2_max_depth = p1.max_depth - p1_subtree.height
    p1_max_height = p1.max_depth - p1_subtree.depth
    # print("p2_max_depth : {}".format(p2_max_depth))
    p2_candidate =[]
    for i in range(len(p2.node_list)):
        if p2.node_list[i].depth <= p2_max_depth and p2.node_list[i].height <= p1_max_height:
            p2_candidate.append(p2.node_list[i])
    if len(p2_candidate) == 0:
        p2_subtree = p2
    else:
        p2_subtree = random.choice(p2_candidate)

    p1_subtree_parent = p1_subtree.parent
    p2_subtree_parent = p2_subtree.parent
    # print("p1_subtree: {}".format(p1_subtree.print_program()))
    # print("p2_subtree: {}".format(p2_subtree.print_program()))
    # print("p1_subtree_parent: {}".format(p1_subtree_parent.print_program() if p1_subtree_parent is not None else "None"))
    # print("p2_subtree_parent: {}".format(p2_subtree_parent.print_program() if p2_subtree_parent is not None else "None"))
    # update depth of subtree
    if p1_subtree_parent is None:
        p2_subtree_depth = 0
    else:
        p2_subtree_depth = p1_subtree_parent.depth + 1
    if p2_subtree_parent is None:
        p1_subtree_depth = 0
    else:
        p1_subtree_depth = p2_subtree_parent.depth + 1
    update_depth_of_subtree(p1_subtree, p1_subtree_depth)
    update_depth_of_subtree(p2_subtree, p2_subtree_depth)
    # update child list, node list, height of parent
    if p1_subtree_parent is None:
        p1 = p2_subtree
    else:
        p2_subtree.parent = p1_subtree_parent
        p1_subtree_parent.child_list.append(p2_subtree)
        p1_subtree_parent.child_list.remove(p1_subtree)
        update_parent(p1_subtree_parent, p1_subtree, p2_subtree)
    if p2_subtree_parent is None:
        p2 = p1_subtree
    else:
        p1_subtree.parent = p2_subtree_parent
        p2_subtree_parent.child_list.append(p1_subtree)
        # p2_subtree_parent.child_list.remove(p2_subtree)
        try:
            p2_subtree_parent.child_list.remove(p2_subtree)
        except ValueError:
            print(p2_subtree_parent.name)
            print(len(p2_subtree_parent.child_list))
            for h in p2_subtree_parent.child_list:
                print("child name: {}".format(h.name))
            p2_subtree.print_program()


        update_parent(p2_subtree_parent, p2_subtree, p1_subtree)
    # if p1.height > p1.max_depth:
    #     print("wrong child p1!")
    #     print(p1.print_program())
    #     print(p2.print_program())
    #     exit()
    # if p1.height > p1.max_depth:
    #     print("wrong child p2!")
    #     print(p1.print_program())
    #     print(p2.print_program())
    #     exit()
    return p1, p2

def mutate(p):
    if len(p.node_list) == 0:
        p_subtree = p
    else:
        p_subtree = random.choice(p.node_list)
    max_h = p.max_depth - p_subtree.depth
    new_tree = construct_grow_tree(max_h, parent=p_subtree.parent)
    p_subtree_parent = p_subtree.parent
    # update child list, node list, height of parent
    if p_subtree_parent is None:
        p = new_tree
    else:
        p_subtree_parent.child_list.append(new_tree)
        p_subtree_parent.child_list.remove(p_subtree)
        p_subtree_parent.node_list.remove(new_tree)
        update_parent(p_subtree_parent, p_subtree, new_tree)
    return p

if __name__ == "__main__":
    max_iteration = 500
    max_depth = g_max_depth
    pop_size = 100
    crossover_p = 0.95
    n = 16
    test_set, answer_list = construct_test_set(n)
    partial_test_set, partial_answer_list = construct_partial_test_set(n)
    pop = initialize_population(pop_size, max_depth)
    pop_fitness = []
    best_fitness_list = []
    final_program = None
    for i in range(pop_size):
        pop_fitness.append(fitness_evaluation(partial_test_set, partial_answer_list, pop[i]))
    # print(pop_fitness)
    # print(pop[0].print_program())
    # print(pop[1].print_program())
    # print(fitness_evaluation(test_set, answer_list, Node(name="a0", child_list=[], depth=0, height=0, max_depth=0)))

    # print(pop[0].child_list[0].depth)
    # print(pop[0].child_list[0].height)



    for i in range(max_iteration):
        print("iteration: {}".format(i))
        pool_size = 0
        pool = []
        while pool_size < pop_size:
            # prepare partial test
            partial_test_set, partial_answer_list = construct_partial_test_set(n)
            # select 10% from parent
            for m in range(int(0.1 * pop_size)):
                pool.append(tournament_selection(pop, pop_fitness))
                pool_size += 1
            # mutaiton or crossover
            r = np.random.uniform()
            if r < crossover_p:
                # recombination
                p1 = tournament_selection(pop, pop_fitness)
                p2 = tournament_selection(pop, pop_fitness)
                # print("recombine")
                # print("p1 :{}".format(p1.print_program()))
                # print("p2 :{}".format(p2.print_program()))
                c1, c2 = recombine(p1, p2)
                # print(c1.print_program())
                # print(c2.print_program())
                # exit()
                pool.append(c1)
                pool.append(c2)
                pool_size += 2
            else:
                # mutation
                p = tournament_selection(pop, pop_fitness)
                c = mutate(p)
                pool.append(c)
                pool_size += 1
        pop = pool[:pop_size]
        # for prog in pop:
        #     print(prog.print_program())
        # optimize based on partial test set
        pop_fitness = []
        best_fitness = 0
        best_index = 0 
        for k in range(pop_size):
            fitness = fitness_evaluation(partial_test_set, partial_answer_list, pop[k])
            # print(fitness)
            if fitness > best_fitness:
                best_fitness = fitness
                best_index = k
            pop_fitness.append(fitness)
        # print(pop_fitness)
        # evaluate based on full test set
        best_fitness_list.append(fitness_evaluation(test_set, answer_list, pop[best_index]))
        final_program = pop[best_index]
        
    print("final program: {}".format(final_program.print_program()))
    itr = [x for x in range(max_iteration)]
    plt.plot(itr, best_fitness_list)
    plt.title("16 middle 3 GP best fitness progress")
    plt.xlabel("Iteration")
    plt.ylabel("Best fitness")
    plt.show()

        


            
