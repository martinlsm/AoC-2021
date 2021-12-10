import numpy as np

def dist(crab, mean):
    dist = np.abs(crab - mean)
    return (dist + 1) * dist / 2

# with open('input7') as f:
#     crabs = np.array(f.readline().strip().split(','), dtype=np.int64)
crabs = np.array([0, 1000, 1000])

max_crab = np.max(crabs)
min_crab = np.min(crabs)

best_score = np.inf

for i in range(min_crab, max_crab + 1):
    dists = np.array([dist(crab, i) for crab in crabs], dtype=np.int64)
    score = np.sum(dists)
    if score < best_score:
        best_score = score

print(best_score)

mean = np.round(np.mean(crabs))
print(mean)
dists = np.array([dist(crab, mean) for crab in crabs], dtype=np.int64)
score = np.sum(dists)
print(score)
