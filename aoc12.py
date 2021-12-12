import numpy as np

class Cave():
    def __init__(self):
        self.paths = []

    def add_path(self, to):
        assert type(to) == str
        self.paths.append(to)

class VisitCounter():
    def __init__(self):
        self.visited = set()
        self.second_visit = None

    def add(self, cave_name):
        if cave_name.isupper():
            return
        assert cave_name.islower()

        if cave_name not in self.visited:
            self.visited.add(cave_name)
            return

        if self.second_visit is None and cave_name != 'start':
            self.second_visit = cave_name
            return
        
        raise ValueError(f'Can not add cave {cave_name}')

    def remove(self, cave_name):
        if cave_name.isupper():
            return
        assert cave_name.islower()

        if self.second_visit == cave_name:
            self.second_visit = None
            return

        if cave_name in self.visited:
            self.visited.remove(cave_name)
            return

        raise ValueError(f'Can not remove cave {cave_name}')

    def can_visit(self, cave_name):
        if cave_name.isupper():
            return True
        assert cave_name.islower()

        if cave_name == 'start':
            return cave_name not in self.visited

        if cave_name in self.visited:
            return self.second_visit is None

        return True


def visit(name, path, caves, second_visit):
    cave = caves[name]

    if name == 'end':
        print(path)
        return 1

    if not visit_counter.can_visit(name):
        return 0
    
    visit_counter.add(name) 

    if len(path) > 0:
        path += ','
    path += name

    num_paths = 0
    for to in cave.paths:
        num_paths += visit(to, path, caves, visit_counter)

    visit_counter.remove(name)

    return num_paths


with open('input12') as f:
    lines = [line.strip() for line in f.readlines()]

caves = {}
for line in lines:
    c0,c1 = line.split('-')

    if c0 not in caves:
        caves[c0] = Cave()
    if c1 not in caves:
        caves[c1] = Cave()

    caves[c0].add_path(c1)
    caves[c1].add_path(c0)

visit_counter = VisitCounter()

num_paths = visit('start', '', caves, visit_counter)
print(num_paths)
