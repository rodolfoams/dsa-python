class UnionFind:
    def __init__(self, edges=[]):
        self.values = set()
        self.value_head = {}
        self.head_values = {}
        self.load_edges(edges)

    def load_edges(self, edges):
        for edge in edges:
            self.union(edge)

    def union(self, edge):
        value0, value1 = edge
        if not self.contains(value0):
            if not self.contains(value1):
                # Create a new "set" with value0 as the head
                self.value_head[value0] = value0
                self.value_head[value1] = value0
                self.head_values[value0] = set([value0, value1])
            else:
                # Add value0 to the same set as value1
                head = self.value_head[value1]
                self.value_head[value0] = head
                self.head_values[head].add(value0)
        elif not self.contains(value1):
            # Add value1 to the same set as value0
            head = self.value_head[value0]
            self.value_head[value1] = head
            self.head_values[head].add(value1)
        else:
            head0 = self.value_head[value0]
            head1 = self.value_head[value1]
            if head0 != head1:
                # Join two sets
                for value in self.head_values[head1]:
                    self.value_head[value] = head0
                    self.head_values[head0].add(value)
                self.head_values.pop(head1)

        self.values.add(value0)
        self.values.add(value1)

    def contains(self, value):
        return value in self.values

    def is_connected(self, value0, value1):
        if self.contains(value0) and self.contains(value1):
            return self.value_head[value0] == self.value_head[value1]
        return False

    def find(self, value):
        return self.value_head.get(value, value)


if __name__ == '__main__':
    edges = [(0, 1), (2, 0), (1, 3), (4, 8), (5, 7), (6, 5)]
    union_find = UnionFind(edges)
    assert(union_find.contains(0))
    assert(union_find.is_connected(2, 3))
    assert(not union_find.is_connected(0, 9))
    assert(union_find.find(3) == union_find.find(0))
    assert(union_find.find(9) == 9)
