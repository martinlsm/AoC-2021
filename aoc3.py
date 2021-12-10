# bit_width = 12
#
# ones = [0 for _ in range(bit_width)]
# num_lines = 0
#
# with open('input') as f:
#     for line in f:
#         for i,c in enumerate(line):
#             print(c)
#             if c == '1':
#                 ones[i] += 1
#         num_lines += 1
#
# gamma_rate = 0
# epsilon_rate = 0
# for i,x in enumerate(ones):
#     if x > num_lines - x:
#         gamma_rate = gamma_rate | (1 << (bit_width - i - 1))
#     else:
#         epsilon_rate = epsilon_rate | (1 << (bit_width - i - 1))
#
# print(gamma_rate * epsilon_rate)


bit_width = 12
data = []
num_lines = 0
num_ones = []

with open('input') as f:
    for line in f:
        num_lines += 1
        data.append(line.strip())

for col in range(len(data[0])):
    ones = 0
    for row in range(len(data)):
        if data[row][col] == '1':
            ones += 1
    num_ones.append(ones)

oxy_rating_rows = set([x for x in range(num_lines)])
co2_rating_rows = set([x for x in range(num_lines)])

for col in range(len(data[0])):
    print([data[x] for x in oxy_rating_rows])

    if len(oxy_rating_rows) == 1:
        break

    ones_count = len([1 for r in oxy_rating_rows if data[r][col] == '1'])
    zeros_count = len(oxy_rating_rows) - ones_count

    most_common = '1' if (ones_count >= zeros_count) else '0'
    for row in range(len(data)):
        if len(co2_rating_rows) == 1:
            break

        if data[row][col] != most_common and row in oxy_rating_rows:
            oxy_rating_rows.remove(row)

for col in range(len(data[0])):
    if len(co2_rating_rows) == 1:
        break

    ones_count = len([1 for r in co2_rating_rows if data[r][col] == '1'])
    zeros_count = len(co2_rating_rows) - ones_count

    least_common = '0' if (ones_count >= zeros_count) else '1'
    for row in range(len(data)):
        if len(co2_rating_rows) == 1:
            break

        if data[row][col] != least_common and row in co2_rating_rows:
            co2_rating_rows.remove(row)

x = data[list(oxy_rating_rows)[0]]
y = data[list(co2_rating_rows)[0]]

print(int(x, 2) * int(y, 2))
