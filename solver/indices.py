class Indices(object):

    @classmethod
    def all(cls):
        return [
            (i, j)
            for i in xrange(9)
            for j in xrange(9)]

    @classmethod
    def row_of(cls, *index):
        return index[0]

    @classmethod
    def column_of(cls, *index):
        return index[1]

    @classmethod
    def nonant_of(cls, *index):
        return ((index[1] / 3) * 3) + (index[0] / 3)

    @classmethod
    def row_indices(cls, row):
        return [(row, k) for k in xrange(9)]

    @classmethod
    def column_indices(cls, column):
        return [(k, column) for k in xrange(9)]

    @classmethod
    def nonant_indices(cls, nonant):
        nonant_x = (nonant % 3) * 3
        nonant_y = (nonant / 3) * 3

        return [
            (x, y)
            for x in xrange(nonant_x, nonant_x + 3)
            for y in xrange(nonant_y, nonant_y + 3)]

    @classmethod
    def row_indices_for_space(cls, *index):
        return cls.row_indices(cls.row_of(*index))

    @classmethod
    def column_indices_for_space(cls, *index):
        return cls.column_indices(cls.column_of(*index))

    @classmethod
    def nonant_indices_for_space(cls, *index):
        return cls.nonant_indices(cls.nonant_of(*index))

    @classmethod
    def row_indices_without_space(cls, *index):
        indices = cls.row_indices_for_space(*index)
        indices.remove(index)
        return indices

    @classmethod
    def column_indices_without_space(cls, *index):
        indices = cls.column_indices_for_space(*index)
        indices.remove(index)
        return indices

    @classmethod
    def nonant_indices_without_space(cls, *index):
        indices = cls.nonant_indices_for_space(*index)
        indices.remove(index)
        return indices
