import numpy as np
from collections import defaultdict

goal = '''\
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #########
'''

with open('input23') as f:
    board = [list(line.strip()) for line in f.readlines()]

def remove_lowest_dist_board(open_nodes, dists):
    b = 0
    m = np.inf
    for board in open_nodes:
        if dists[board] + h(board) < m:
            b = board
            m = dists[board] + h(board)

    open_nodes.remove(b)
    return b


hs = {}
def h(board):
    if board not in hs:
        hs[board] = 0

    return hs[board]

def _convert_letters_to_nums(board):
    board[board.index('A')] = '0'
    board[board.index('A')] = '1'
    board[board.index('B')] = '2'
    board[board.index('B')] = '3'
    board[board.index('C')] = '4'
    board[board.index('C')] = '5'
    board[board.index('D')] = '6'
    board[board.index('D')] = '7'

def _convert_nums_to_letters(board):
    board[board.index('0')] = 'A'
    board[board.index('1')] = 'A'
    board[board.index('2')] = 'B'
    board[board.index('3')] = 'B'
    board[board.index('4')] = 'C'
    board[board.index('5')] = 'C'
    board[board.index('6')] = 'D'
    board[board.index('7')] = 'D'

def find_neighbors(board):
    _convert_letters_to_nums(board)
    neighbors = []

    for a in range(0,8):
        a = str(a)


    _convert_nums_to_letters(board)

def shortest_path(board):
    open_nodes = set([board])
    dists = defaultdict(np.inf)
    dists[board] = 0

    while len(open_nodes) > 0:
        current = remove_lowest_dist_board(open_nodes)

        if current == goal:
            return dists[end]

        neighbors = find_neighbors(current)
        for (neighbor, dist) in neighbors: 
            tentative_score = dists[neighbor] + dist
            if tentative_score < dists[neighbor]:
                dists[neighbor] = tentative_score
                if neighbor not in open_nodes:
                    open_nodes.add(neighbor)


    raise ValueError('Could not reach goal')

