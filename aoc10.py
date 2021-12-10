from collections import deque

# stacks = {'{':deque(), '[':deque(), '<':deque(), '(':deque()}
# stacks['}'] = stacks['{']
# stacks[']'] = stacks['[']
# stacks['>'] = stacks['<']
# stacks[')'] = stacks['(']

# stack = deque()
# table = {')':3, ']':57, '}':1197, '>':25137}
# closing = {'(':')', '[':']', '<':'>', '{':'}'}
#
# with open('input10') as f:
#     lines = [line.strip() for line in f.readlines()]
#
# score = 0
# for line in lines:
#     print('\n\n')
#     print(line)
#     for c in line:
#         print(stack)
#         if c == '(' or c == '{' or c == '<' or c == '[':
#             stack.append(c)
#         else:
#             try:
#                 x = stack.pop()
#                 print((c,x))
#                 if c != closing[x]:
#                     score += table[c]
#                     break
#             except IndexError:
#                 score += table[c]
#                 break
#
# print(score)

table = {')':1, ']':2, '}':3, '>':4}
closing = {'(':')', '[':']', '<':'>', '{':'}'}

with open('input10') as f:
    lines = [line.strip() for line in f.readlines()]

scores = []
for line in lines:
    stack = deque()
    valid = True
    for c in line:
        if c == '(' or c == '{' or c == '<' or c == '[':
            stack.append(c)
        else:
            try:
                x = stack.pop()
                if c != closing[x]:
                    valid = False
                    break
            except IndexError:
                valid = False
                break

    if valid:
        print(stack)
        score = 0
        while len(stack) > 0:
            x = stack.pop()
            print((x,score))
            score *= 5
            score += table[closing[x]]
        scores.append(score)

scores = sorted(scores)
print(scores[len(scores)//2])
