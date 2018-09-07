class Indices(object):

    @classmethod
    def for_space(cls, *index):
        return cls.indices(cls.of(*index))

    @classmethod
    def without_space(cls, *index):
        indices = cls.for_space(*index)
        indices.remove(index)
        return indices

    @classmethod
    def all(cls):
        return [
            (i, j)
            for i in xrange(9)
            for j in xrange(9)]

    @classmethod
    def same(cls, indices):
        return all(
            cls.of(*index) == cls.of(*indices[0])
            for index in indices)


class Row(Indices):

    @classmethod
    def of(cls, *index):
        return index[0]

    @classmethod
    def indices(cls, row):
        return [(row, k) for k in xrange(9)]


class Column(Indices):

    @classmethod
    def of(cls, *index):
        return index[1]

    @classmethod
    def indices(cls, column):
        return [(k, column) for k in xrange(9)]


class Nonant(Indices):

    @classmethod
    def of(cls, *index):
        return ((index[1] / 3) * 3) + (index[0] / 3)

    @classmethod
    def indices(cls, nonant):
        nonant_x = (nonant % 3) * 3
        nonant_y = (nonant / 3) * 3

        return [
            (x, y)
            for x in xrange(nonant_x, nonant_x + 3)
            for y in xrange(nonant_y, nonant_y + 3)]
