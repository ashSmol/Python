class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        return f'({self.real_part}+{self.imaginary_part}j)'

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)

    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.imaginary_part * other.imaginary_part,
                             self.real_part * other.imaginary_part + self.imaginary_part*other.real_part)


num_1 = ComplexNumber(2, 3)
num_2 = ComplexNumber(4, 5)
print(num_1 + num_2)
print(num_1 * num_2)
print()
print(complex(2, 3) + complex(4, 5))
print(complex(2, 3) * complex(4, 5))
