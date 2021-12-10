with open('input6') as f:
    fishes = [int(x) for x in f.readline().strip().split(',')]

fishes_dict = {n:0 for n in range(9)}
for fish in fishes:
    fishes_dict[fish] += 1
print(fishes_dict)

for i in range(256):
    new_gen = {n-1:x for (n,x) in fishes_dict.items() if n > 0}
    new_gen[6] += fishes_dict[0]
    new_gen[8] = fishes_dict[0]
    fishes_dict = new_gen
    print(new_gen)

print(sum(fishes_dict.values()))
