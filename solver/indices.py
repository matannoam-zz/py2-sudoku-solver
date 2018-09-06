class Indices(object):

    @classmethod
    def all(cls):
        return [
            (i, j)
            for i in xrange(9)
            for j in xrange(9)]

    @classmethod
    def row_indices_for_space(cls, i, j):
        return [(i, k) for k in xrange(9)]

    @classmethod
    def column_indices_for_space(self, i, j):
        return [(k, j) for k in xrange(9)]

    @classmethod
    def nonant_indices_for_space(self, i, j):
        nonant_x = (i / 3) * 3
        nonant_y = (j / 3) * 3

        return [
            (x, y)
            for x in xrange(nonant_x, nonant_x + 3)
            for y in xrange(nonant_y, nonant_y + 3)]

    @classmethod
    def row_indices_without_space(cls, i, j):
        return [(i, k) for k in xrange(9) if k != j]

    @classmethod
    def column_indices_without_space(self, i, j):
        return [(k, j) for k in xrange(9) if k != i]

    @classmethod
    def nonant_indices_without_space(self, i, j):
        nonant_x = (i / 3) * 3
        nonant_y = (j / 3) * 3

        return [
            (x, y)
            for x in xrange(nonant_x, nonant_x + 3)
            for y in xrange(nonant_y, nonant_y + 3)
            if x != i or y != j]
