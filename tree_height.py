# python3

import sys
import threading


def compute_height(n, parents):
    # Construct adjacency list
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            adj_list[parents[i]].append(i)

    # BFS to calculate height
    max_height = 0
    q = [(root, 1)]
    while q:
        node, height = q.pop(0)
        if height > max_height:
            max_height = height
        for child in adj_list[node]:
            q.append((child, height+1))

    return max_height


def main():
    # get input type (I or F)
    input_type = input().strip().upper()

    # handle keyboard input
    if input_type == 'I':
        n = int(input().strip())
        parents = list(map(int, input().strip().split()))
        print(compute_height(n, parents))

    # handle file input
    elif input_type == 'F':
        filename = input().strip()
        if 'a' not in filename:
            try:
                with open('test/' + filename, 'r') as f:
                    n = int(f.readline().strip())
                    parents = list(map(int, f.readline().strip().split()))
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


