import numpy as np
from collections import namedtuple

State = namedtuple('State', 'turn p0_score p1_score p0_loc p1_loc')

f = np.array([0,1,1,1])
f = np.convolve(np.convolve(f, f), f)

lookup = {}

def new_loc(loc, dice_roll):
    return ((loc + dice_roll - 1) % 10) + 1


def num_ways_to_win(state):
    if state.p0_score >= 21:
        assert state.p1_score < 21 
        return 1

    if state.p1_score >= 21:
        return 0

    if state in lookup:
        return lookup[state]

    if state.turn % 2 == 0: # p0 rolls three times
        ways_to_win = np.zeros(shape=f.shape)
        for i,freq in enumerate(f):
            if freq == 0:
                continue

            p0_new_loc = new_loc(state.p0_loc, i)
            p0_new_score = state.p0_score + p0_new_loc
            s = State(state.turn + 1, p0_new_score, state.p1_score, p0_new_loc, state.p1_loc)
            n = num_ways_to_win(s)

            ways_to_win[i] = freq * n

        res = int(np.sum(ways_to_win))
        lookup[state] = res
        return res

    else:
        ways_to_win = np.zeros(shape=f.shape)
        for i,freq in enumerate(f):
            if freq == 0:
                continue

            p1_new_loc = new_loc(state.p1_loc, i)
            p1_new_score = state.p1_score + p1_new_loc
            s = State(state.turn + 1, state.p0_score, p1_new_score, state.p0_loc, p1_new_loc)
            n = num_ways_to_win(s)

            ways_to_win[i] = freq * n

        res = int(np.sum(ways_to_win))
        lookup[state] = res
        return res


start_0 = State(0, 0, 0, 10, 6)
start_1 = State(0, 0, 0, 6, 10)

print(num_ways_to_win(start_0))
print(num_ways_to_win(start_1))
