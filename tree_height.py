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

    # recursion
    def dfs(node):
        height = 0
        for child in adj_list[node]:
            height = max(height, dfs(child))
        return height + 1

    # calculate height
    return dfs(root)


def main():
    # get input type (I or F)
    input_type = input().strip().upper()

    # handle keyboard input
    if input_type == 'I':
        n = int(input().strip())
        parents = np.array(list(map(int, input().strip().split())))
        print(compute_height(n, parents))

    # handle file input
    elif input_type == 'F':
        filename = input().strip()
        if 'a' not in filename:
            try:
                with open(filename, 'r') as f:
                    n = int(f.readline().strip())
                    parents = np.array(list(map(int, f.readline().strip().split())))
                    print(compute_height(n, parents))
            except FileNotFoundError:
                print(f'Error: File {filename} not found')
        else:
            print('Error: File name cannot contain letter "a"')

    # handle invalid input
    else:
        print('Error: Invalid input')


# increase recursion depth limit and thread stack size
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

# print test array
print(np.array([1,2,3]))
