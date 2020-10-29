class Cell:
    def __init__(self, segments_count):
        self.segments_count = segments_count

    def __add__(self, other):
        return Cell(self.segments_count + other.segments_count)

    def __sub__(self, other):
        return Cell(self.segments_count - other.segments_count if self.segments_count > other.segments_count else
                    other.segments_count - self.segments_count)

    def __mul__(self, other):
        return Cell(self.segments_count * other.segments_count)

    def __floordiv__(self, other):
        return Cell(self.segments_count // other.segments_count if self.segments_count > other.segments_count else
                    other.segments_count // self.segments_count)

    def __str__(self):
        return str(self.segments_count)

    def make_order(self, segments_in_row):
        if self.segments_count > segments_in_row:
            for _ in range(self.segments_count // segments_in_row):
                print('*' * segments_in_row)
            print('*' * (self.segments_count % segments_in_row))
        else:
            print('*' * self.segments_count)


c_1 = Cell(5)
c_2 = Cell(2)

print((c_1 + c_2))
print(c_1 * c_2)
print(c_1 - c_2)
print(c_2 - c_1)
print(c_1 // c_2)
print(c_2 // c_1)

c_1.make_order(2)
