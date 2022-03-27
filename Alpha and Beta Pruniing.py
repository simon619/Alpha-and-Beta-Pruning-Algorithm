import random


def input_call():
    bool = False
    ID = str(input('Enter Your ID [It Has To Be 8 Digit]: '))
    lower = int(input('Enter Lower Range: '))
    upper = int(input('Enter Upper Range: '))
    if len(ID) == 8 and lower < upper:
        bool = True
    if bool:
        return ID, lower, upper
    else:
        return input_call()


s, l, u = input_call()
depth = 2 * int(s[0])
branching_factor = int(s[2])
print('Depth and Branches ratio is %d:%d' % (depth, branching_factor))
t = ''
t += s[-1]
t += s[-2]
init_life = int(t)
print('Initial Life: %d' % init_life)
node_number = 0
for i in range(0, depth):
    node_number += branching_factor ** i
print('%d Nodes Requires Without Leaf Node' % node_number)
nodes = []
for i in range(0, node_number):
    nodes.append(str(i))
print(nodes)
val = 0
for i in range(0, depth - 1):
    val += branching_factor ** i
dic = {}
dic2 = {}
j = 0
while j < val:
    dic[nodes[j]] = [str(branching_factor * j + k) for k in range(1, branching_factor + 1)]
    j += 1
j = val
# Leaf Nodes Creation
leaf_node = []
while j < len(nodes):
    dic[nodes[j]] = [str(random.randint(l, u)) for k in range(1, branching_factor + 1)]
    leaf_node.append(dic[nodes[j]])
    dic2[nodes[j]] = []
    j += 1

traversed_leaf_nodes = []
master_chief = ''
for t in leaf_node:
    for x in t:
        master_chief += x + ',' + ' '

print('Terminal States (leaf node values) are %s' % master_chief)
print('Initial State Of The Tree: ')
print(dic)


def minimax(node, depth, alpha, beta, maximizing, b_node):
    # print('Entered %s node' % node) # Uncomment This For Tracing  # Uncomment This For Tracing
    # print('Alpha = %d, Beta = %d' % (alpha, beta))
    global k, count
    # print('Depth = %d' % depth)
    if depth == 0:
        x = int(node)
        traversed_leaf_nodes.append(x)
        dic2[b_node] += [node]
        return x
    if maximizing:
        maxeval = - 1000
        for i in range(0, len(dic[node])):
            # print('Node = %s' % dic[node][i])
            count = 0
            eval = minimax(dic[node][i], depth - 1, alpha, beta, False, node)
            maxeval = max(maxeval, eval)
            alpha = max(alpha, eval)
            # print('Alpha = %d, Beta = %d maxeval = %d' % (alpha, beta, maxeval)) # Uncomment This For Tracing
            if beta <= alpha:
                break
        return maxeval
    else:
        mineval = 1000
        for i in range(0, len(dic[node])):
            # print(dic[node][i])
            eval = minimax(dic[node][i], depth - 1, alpha, beta, True, node)
            mineval = min(mineval, eval)
            beta = min(beta, eval)
            # print('Alpha = %d, Beta = %d mineval = %d' % (alpha, beta, mineval)) # Uncomment This For Tracing
            if beta <= alpha:
                break
        return mineval


n = 0
for i in dic:
    n = minimax(i, depth, -1000, 1000, True, i)
    break
print('Left life(HP) of the defender after maximum damage caused by the attacker is %d' % (init_life - n))
print('Leaf Nodes State After Alpha Beta Pruning: ')
print(dic2)
count = 0
for u in dic2:
    for v in range(0, len(dic2[u])):
        count += 1
print('After Alpha-Beta Pruning Leaf Node Comparisons %d' % count)
