# python3

import sys
import threading
import numpy as np



def compute_height(n, parents):
    # adjacency list
    adj_list = [[] for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            adj_list[parents[i]].append(i)

    # rekursija
    def dfs(node):
        height = 0
        for child in adj_list[node]:
            height = max(height, dfs(child))
        return height + 1

    # aprekina augstumu
    return dfs(root)


def main():
    # I vai F
    input_type = input().strip().upper()
    if input_type == 'I':
        n = int(input().strip())
        parents = list(map(int, input().strip().split()))
        print(compute_height(n, parents))
    elif input_type == 'F':
        filename = input().strip()
        if 'a' not in filename:
            with open(filename, 'r') as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().strip().split()))
                print(compute_height(n, parents))
    else:
        print('Invalid input')


    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
print(np.array([1,2,3]))