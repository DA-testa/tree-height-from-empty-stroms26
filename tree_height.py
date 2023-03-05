# python3

import sys
import threading


def compute_height(n, parents):
    # adjacency saraksts
    adj_list = [[] for _ in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            adj_list[parents[i]].append(i)

    # BFS to augstuma noteiksanai
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
    # (I vai F)
    input_type = input().strip().upper()

    #  keyboard input
    if input_type == 'I':
        n = int(input().strip())
        parents = list(map(int, input().strip().split()))
        print(compute_height(n, parents))

    # file input
    elif input_type == 'F':
        filename = input().strip()
        if 'a' not in filename:
            try:
                with open(filename, 'r') as f:
                    n = int(f.readline().strip())
                    parents = list(map(int, f.readline().strip().split()))
                    print(compute_height(n, parents))
            except FileNotFoundError:
                print(f'Error: File {filename} not found')
        else:
            print('nedrikst saturet "a"')

    # invalid input
    else:
        print('nepareiza ievade')


# rekursijas limits
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()

